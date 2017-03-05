#####
# Author: Maria Sandrikova
# Based on https://github.com/williamsmj/sentiment/blob/master/sentiment.ipynb
# Copyright 2017
#####

import os
import pandas as pd
import joblib
import time

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import LogisticRegressionCV
from sklearn.pipeline import Pipeline

WORKING_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(WORKING_DIR, 'train_data')
training_csv_file = os.path.join(DATA_DIR, 'training.1600000.processed.noemoticon.csv')
MODEL_OUTPUT = os.path.join(WORKING_DIR, 'model.pkl')


def train():
    names = ('polarity', 'id', 'date', 'query', 'author', 'text')
    df = pd.read_csv(training_csv_file, encoding='latin1', names=names)
    df['polarity'].replace({0: -1, 4: 1}, inplace=True)
    text = df['text']
    target = df['polarity'].values

    vectorizer = CountVectorizer(ngram_range=(1, 2), max_features=100000)
    feature_selector = SelectKBest(chi2, k=5000)
    classifier = LogisticRegressionCV(n_jobs=-1)

    sentiment_pipeline = Pipeline((
        ('v', vectorizer),
        ('f', feature_selector),
        ('c', classifier)
    ))

    sentiment_pipeline.fit(text, target)
    joblib.dump(sentiment_pipeline, MODEL_OUTPUT)


def load_model():
    return joblib.load(MODEL_OUTPUT)


def classify(text: str, model) -> bool:
    predicted = model.predict([text])
    return predicted[0] == 1