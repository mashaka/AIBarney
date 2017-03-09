#####
# Author: Maria Sandrikova
# Copyright 2017
#####

from algo import classify, load_model

TEST_MSGS = [
    'Oh, yeah, I am fan of Lisa',
    'I like Rising Hope. What is your favorite?',
    'It is horrible'
]

sentiment_model = None

def test_predict(msg):
    global sentiment_model
    if sentiment_model is None:
        sentiment_model = load_model()
    is_positive = classify(msg, sentiment_model)
    print('{}:\t{}'.format(is_positive, msg))

def test_all():
    for msg in TEST_MSGS:
        test_predict(msg)


test_all()