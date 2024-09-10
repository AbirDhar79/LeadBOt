from flask import Flask, render_template, request
from scrape import scrape_posts
from notification import send_email_notification

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape_and_notify():
    industry = request.form.get('industry')
    keywords = request.form.get('keywords').split(',')
    country = request.form.get('country')

    # Scrape posts
    posts = scrape_posts(industry, keywords, country)

    # Send notifications
    if posts:
        send_email_notification(posts)

    return render_template('results.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
