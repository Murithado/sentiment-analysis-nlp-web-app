from flask import Flask, render_template, request
import sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def user_input():
    if request.method == 'GET':
        return render_template('index.html')
        
    else:
        emotion = sentiment.predict_emotion(request.form['text'])
        return render_template('index_pic.html', href=f'static/{emotion}.svg')