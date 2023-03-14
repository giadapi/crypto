from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig, TextClassificationPipeline
from transformers import pipeline
import numpy as np
import pandas as pd
from scipy.special import softmax
import datetime
import pandas as pd
from datetime import datetime
# from model import preprocess, run_model, remove_spam
from crypto.snsscrape_scripter_live import snscrape_expert, snscrape, get_usernames
from data import update_prices

def remove_spam(data):
    dup_tweets = data[data['text'].duplicated()]
    blacklist = []
    for name in dup_tweets['username']:
        blacklist.append(name)
    blacklist = list(set(blacklist))
    def to_remove(x):
        if x in blacklist:
            return True
        else:
            return False
    data['to_remove'] = data['username'].apply(to_remove)
    mask = data['to_remove']
    data2 = data[~mask]
    return data2

def preprocess(text):
    new_text = []
    text = str(text)
    text = text.replace("\n", " ")
    for t in text.split(" "):
        t = '' if t.startswith('@') and len(t) > 1 else t
        t = '' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)



def run_model(data):
    data = data[['text', 'date','datetime']]
    data['process_text'] = data.text
    data['negative_bert'] = data.text
    data['neutral_bert'] = data.text
    data['positive_bert'] = data.text

    #use the preprocess to clean the data
    data['process_text'] = data['text'].apply(preprocess)

    MODEL_bert = f"ElKulako/cryptobert"
    tokenizer_bert = AutoTokenizer.from_pretrained(MODEL_bert)
    tokenizer_bert.model_max_length = 512 #solve the error: RuntimeError: The expanded size of the tensor (562) must match the existing size (514) at non-singleton dimension
    config_bert = AutoConfig.from_pretrained(MODEL_bert)
    # PT
    model_bert = AutoModelForSequenceClassification.from_pretrained(MODEL_bert)
    model_bert.config.max_position_embeddings = 512

    def scores_bert(sample_text):
        encoded_input_bert = tokenizer_bert(sample_text, return_tensors='pt')
        output_bert = model_bert(**encoded_input_bert)
        scores_bert = output_bert[0][0].detach().numpy()
        scores_bert = softmax(scores_bert) #1st score is negative, 2nd score is netural, 3rd score is positive
        return scores_bert

    data['text'] = data['process_text'].apply(scores_bert)
    for i in range(len(data)):
        data['negative_bert'][i] = data['text'][i][0]
        data['neutral_bert'][i] = data['text'][i][1]
        data['positive_bert'][i] = data['text'][i][2]

    data = data[['date','datetime', 'process_text', 'negative_bert', 'neutral_bert','positive_bert']]
    return data






def update_dataframe(data_path = '../raw_data/cleaned_tweets_without_dupes_120323.csv', num_tweets=149):
    data = pd.read_csv(data_path)
    data['datetime'] = pd.to_datetime(data['datetime'])
    length = (data.shape[0]-1)
    latest_time = data['datetime'][length].date()
    now = datetime.now().date()
    difference = (now - latest_time).days

    if difference > 0:
        print('Updating!')
        now = pd.Timestamp(now).isoformat('_', 'seconds')+'_UTC'
        latest_time = pd.Timestamp(latest_time).isoformat('_', 'seconds')+'_UTC'

        #scrape and process experts
        #define a custom remove spam function fof experts
        experts = get_usernames(file_csv='raw_data/Usernames - Sheet1.csv')
        expert_df_updates = snscrape_expert(start_date=latest_time,end_date=None,filename=f'raw_data/experts_{latest_time}_{now}.csv',users_name=experts,make_csv=True)
        expert_df_updates = remove_spam(expert_df_updates)
        expert_df_updates = preprocess(expert_df_updates)
        expert_df_updates = run_model(expert_df_updates)
        expert_df_updates['date'] = expert_df_updates['datetime'].date()

        #we are now assuming we want acerage daily sentiment but we might not
        expert_df_updates = expert_df_updates.groupby(by='date').mean()

        all_df_updates = snscrape(num_tweets=num_tweets,start_date=latest_time,end_date=None, hour_delta=8,min_gap=10,filename=f'raw_data/{latest_time}_{now}.csv',make_csv=True)

        #scrape and process all
        all_df_updates = remove_spam(all_df_updates)
        all_df_updates = preprocess(all_df_updates)
        all_df_updates = run_model(all_df_updates)
        all_df_updates['date'] = all_df_updates['datetime'].date()
        all_df_updates = all_df_updates.groupby(by='date').mean()

        #add the bitcoin data
        data2 = update_prices(latest_time, now)

        #moving average sentiment included in df



    else:
        print('Up to date already!')

    return data

if __name__ == '__main__':
    update_dataframe()
