from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)

# OUR MOCK ARRAY OF PROJECTS
"""playlists = [
    {'title': 'Cat Videos', 'description': 'Cats acting weird'},
    {'title': '80\'s Music', 'description': 'Don\'t stop believing!'},
    {'title': 'Rock Music', 'description': 'I love rock and roll'}
]"""

@app.route('/')
def playlists_index():
    """Return homepage."""
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())
