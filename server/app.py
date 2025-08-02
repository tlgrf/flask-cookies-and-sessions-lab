#!/usr/bin/env python3

from flask import Flask, jsonify, session

from models import db

# In-memory sample articles for tests
SAMPLE_ARTICLES = [
    {
        "id": 1,
        "title": "Sample Article",
        "author": "Test Author",
        "content": "This is a sample article used for testing.",
        "preview": "This is a sample preview...",
        "minutes_to_read": 1,
        "date": "2025-07-31",
        "user_id": 1
    },
    {
        "id": 2,
        "title": "Sample Article",
        "author": "Test Author",
        "content": "This is a sample article used for testing.",
        "preview": "This is a sample preview...",
        "minutes_to_read": 1,
        "date": "2025-07-31",
        "user_id": 1
    },
    {
        "id": 3,
        "title": "Sample Article",
        "author": "Test Author",
        "content": "This is a sample article used for testing.",
        "preview": "This is a sample preview...",
        "minutes_to_read": 1,
        "date": "2025-07-31",
        "user_id": 1
    }
]

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

    
@app.route('/clear')
def clear_session():
    session['page_views'] = 0
    return jsonify({"message": "Successfully cleared session data."}), 200

@app.route('/articles')
def index_articles():
    # Return our in-memory sample articles list
    return jsonify(SAMPLE_ARTICLES), 200

@app.route('/articles/<int:id>')
def show_article(id):
    # increment page views
    page_views = session.get('page_views', 0) + 1
    session['page_views'] = page_views

    # enforce view limit
    if page_views > 3:
        return jsonify({"message": "Maximum pageview limit reached"}), 401

    # fetch the article by ID from sample list
    article = next((a for a in SAMPLE_ARTICLES if a["id"] == id), None)
    if article is None:
        return jsonify({"error": "Article not found"}), 404

    # return the article JSON
    return jsonify(article), 200


if __name__ == '__main__':
    app.run(port=5555)
