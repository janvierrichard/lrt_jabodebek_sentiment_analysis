import re, string, json
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from typing import List
from nlp_id.lemmatizer import Lemmatizer
from nlp_id.tokenizer import Tokenizer, PhraseTokenizer
from nlp_id.postag import PosTag
from nlp_id.stopword import StopWord

class TextProcessing:
    def __init__(self, dataset_path) -> None:
        self.stopword_en = stopwords.words('english')
        self.stopword_id = stopwords.words('indonesian')
        self.dataset_path = dataset_path

    def lowercase(self, data):
        data = data.lower()
        return data

    def tokenization(self, data, lib= "standar"):
        if lib == "standar":
            result = word_tokenize(data)
        elif lib == "kumparan":
            token = Tokenizer()
            result = token.tokenize(data)
        return result

    def text_cleaning(self, data):
        #number
        data = re.sub(r"\d+", "", data)
        #@pattern
        at_pattern = re.compile(r'@\S+')
        data = at_pattern.sub(r'', data)
        #url
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        data = url_pattern.sub(r'', data)
        #punctuation
        data = data.translate(str.maketrans("","",string.punctuation))
        #whitespace
        hasil = data.strip()
        return hasil

    def stopword_removal(self, data:List[str], lib= "standar"):
        if lib == "standar":
            stopwords = self.stopword_en
            resultwords = [word for word in data if word not in stopwords]
            result = ' '.join(resultwords)
        elif lib == "kumparan":
            sw = StopWord()
            result = sw.remove_stopword(data)
        return result

    def stemming(self, data:str):
        st = PorterStemmer()
        return st.stem(data)
    
    def lemmatize(self, data:str):
        lemmatizer = Lemmatizer()
        result = lemmatizer.lemmatize(data)
        return data
    
    def slang_transforming(self, data:str):
        with open(f"{self.dataset_path}/slang.json") as f:
            slang_dict = json.load(f)
        tokens = self.tokenization(data)

        result = []
        for token in tokens:
            if token in slang_dict:
                token = slang_dict[token]
            result.append(token)
        
        result = ' '.join(result)
        return result

if __name__ == "__main__":
    test = "AMZING ISYANAA!! Jujur aku amazed banget dengan skill dan minat Isyana dalam bermusik. Ga Cuma bernyanyi tapi main alat musik pun jago banget"

    mod = TextProcessing()
    hasil = mod.lowercase(test)
    # hasil = mod.text_cleaning(hasil)
    # # hasil = mod.tokenization(hasil, lib = "kumparan")
    # hasil = mod.stopword_removal(hasil, lib = "kumparan")
    # hasil = mod.stemming(hasil)

    hasil = mod.slang_transforming(hasil)

    print(hasil)