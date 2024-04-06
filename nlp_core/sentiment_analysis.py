import pandas as pd
from nlp_id.lemmatizer import Lemmatizer
from nlp_id.tokenizer import Tokenizer, PhraseTokenizer
from nlp_id.stopword import StopWord
import nltk
from nlp_core.text_processing import TextProcessing
from pandas import DataFrame
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk import ngrams
from tqdm import tqdm
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
from nlp_core.text_processing import TextProcessing
import streamlit as st

class Sentiment_Analysis:
    def __init__(self) -> None:
        # self.model_path = config['PATH_MODEL_ML']
        # self.dataset_path = config['PATH_DATASET']
        self.model_path = st.secrets['path_configuration']['path_model']
        self.dataset_path = st.secrets['path_configuration']['path_dataset']
        self.dataset_name = "lrt_jabodebek_labeled.csv"
        self.model_filename = "model.sav"
        self.vectorizer_filename = "vector.sav"
    
    def train_model(self):
        print("Mengawali proses")
        raw_data = pd.read_csv(f"{self.dataset_path}/{self.dataset_name}", sep = ";")
        raw_data.rename({"full_text": "review", "sentiment": "sentimen"}, axis = 1, inplace = True)
        df = raw_data.loc[:, ['review', 'sentimen']]

        length = len(df['review'])
        divider = 100
        nums = length//divider

        print("Jalankan proses cleaning")
        results = pd.Series()
        for index in tqdm(range(nums + 1)):
            result = df['review'][index*divider:(index+1)*divider].apply(lambda x: self.cleaning_service(str(x)))
            results = pd.concat([results, result])
        
        df['text_cleaned'] = results

        print('Jalankan proses encode pada sentimen')
        lb = LabelEncoder()
        df['label'] = lb.fit_transform(df['sentimen'])
        df.dropna(inplace = True)

        df_p = df[df["sentimen"] == 'positif']
        df_ne = df[df["sentimen"] == 'negatif']
        df_n = df[df["sentimen"] == 'netral']
        # df_p = df_p.sample(400)
        # df_ne = df_ne.sample(400)
        _ = pd.concat([df_p, df_ne])

        print("Jalankan proses TFIDF")
        vectorizer = TfidfVectorizer()
        v_data = vectorizer.fit_transform(_['text_cleaned']).toarray()

        X_train, X_test, y_train, y_test = train_test_split(v_data, _['sentimen'], test_size = 0.3, random_state = 42)

        print("Jalankan proses melatih model")
        model_rf = RandomForestClassifier(max_depth = 5, n_estimators = 10, random_state = 42)
        model_rf.fit(X_train, y_train)

        print("Jalankan proses menyimpan model")
        pickle.dump(model_rf, open(f"{self.model_path}/{self.model_filename}", 'wb'))
        pickle.dump(vectorizer, open(f"{self.model_path}/{self.vectorizer_filename}", 'wb'))
        
    def cleaning_service(self, data:str):
        tp = TextProcessing(self.dataset_path)
        hasil = tp.lowercase(data)
        hasil = tp.text_cleaning(hasil)
        # hasil = tp.tokenization(hasil, lib = "kumparan")
        hasil = tp.slang_transforming(hasil)
        hasil = tp.stopword_removal(hasil, lib = "kumparan")
        # hasil = tp.lemmatize(hasil)
        return hasil
    
    def predict_sentiment(self, data):
        vector = pickle.load(open(f"{self.model_path}/{self.vectorizer_filename}", 'rb'))
        model = pickle.load(open(f"{self.model_path}/{self.model_filename}", 'rb'))
        
        data = [self.cleaning_service(data)]

        vector_data = vector.transform(data).toarray()
        hasil = model.predict(vector_data)

        if hasil[0] == 'negatif':
            sentiment = "Negatif"
        else:
            sentiment = "Positif"
        
        return sentiment