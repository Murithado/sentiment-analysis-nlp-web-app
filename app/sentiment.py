import tensorflow as tf
import pickle as pkl
import numpy as np

reverse_emotion_dict = {0: 'anger', 1: 'disgust', 2: 'fear', 3: 'joy', 4: 'sadness', 5: 'surprise'}

def load_saved_model():
    '''Loads the pretrained models'''
    model = tf.keras.models.load_model('app/saved_model/my_model.h5')
    with open('app/saved_model/vectorizer.pkl', 'rb') as f:
        vectorizer_dict = pkl.load(f)
    vectorizer = tf.keras.layers.TextVectorization.from_config(vectorizer_dict['config'])
#    vectorizer.adapt(tf.data.Dataset.from_tensor_slices([' ']).batch(200))
    vectorizer.set_weights(vectorizer_dict['weights'])
    return model, vectorizer

def predict_emotion(user_input_sentence):
    model, vectorizer = load_saved_model()
    prediction = np.argmax(model.predict(vectorizer([user_input_sentence])))
    return reverse_emotion_dict[prediction]
