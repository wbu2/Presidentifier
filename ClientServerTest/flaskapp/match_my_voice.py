from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

import pandas as pd
import numpy as np
import csv

class Model:
    
    def __init__(self):
        path_to_train = "training_data.csv"
        training = pd.read_csv(path_to_train, encoding='utf-8')[['v1', 'v2']]

        training = training.drop(training[training['v2'].isnull()].index)
        text = training['v2']

        label = training['v1']

        
        
  
        self.corpus = list(text)
        self.tfidf = TfidfVectorizer(max_features = 6000) 
        self.tfidf.fit(self.corpus)
        tfidf_features = self.tfidf.transform(self.corpus)


        
        
        self.svm_model_linear = SVC(kernel = 'linear', C = 1).fit(tfidf_features, label)
        
    def predict(self, str):
        path_to_test = 'testing_data.csv'
        
        with open(path_to_test, mode='w') as csv_file:
            fieldnames = ['v1','v2']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'v1': 'User', 'v2': str})
    
        testing = pd.read_csv(path_to_test, encoding='utf-8')[['v1', 'v2']]
        tweet = testing['v2']
        user = testing['v1']
        user_tweets = list(tweet)
        test_data = self.tfidf.transform(user_tweets)
        svm_predictions = self.svm_model_linear.predict(test_data)
        return(svm_predictions[0])
       # return self.svm_model_linear.predict(test_data)

