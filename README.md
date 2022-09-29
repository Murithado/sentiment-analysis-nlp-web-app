# Sentiment Analysis Web Application

## Description
Sentiment Analysis classifying input sentences based on emotion as either anger, disgust, fear, joy, sadness or surprise. The datasets used to train the model were an extract of tweets, Googles goemotions dataset and a suitable kaggle dataset. The model was trained with the Stanfords glove word embeddings. The dataset was highly imbalanced with the joy labesls making about 35% of the dataset, a problem I plan to rectify.The model consists of the input layer connected to an embedding layer, a dropout layer connected to a Bidirectional LSTM layer, then a Convolutional layer connected to two pooling layers that were concatenated and connected to a softmax output layer. The notebooks for the dataset preparation and models are in the ipynb folder.

## How to Use
The URL is

>https://sentiment-analysis-nlp-web-app.herokuapp.com/

Input your sentence in the box and click Submit to get a prediction