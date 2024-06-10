
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=YOUR_API_KEY')
    news_articles = response.json()['articles']
    return render_template('index.html', news_articles=news_articles)

if __name__ == '__main__':
    app.run(debug=True)
