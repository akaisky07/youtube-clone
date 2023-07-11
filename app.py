from flask import Flask, render_template, request
from googleapiclient.discovery import build

app = Flask(__name__)

api_key = 'AIzaSyAih2wQ1A1-agIh6mGue532pZltf3l27Hk'
youtube = build('youtube', 'v3', developerKey=api_key)


@app.route('/')
def index():
    # Fetch the list of YouTube videos
    videos = youtube.search().list(
        part='snippet',
        type='video',
        maxResults=10,
        q='cats'  # You can change the search query here
    ).execute()
    
    return render_template('index.html', videos=videos['items'])
    
@app.route('/search')
def search():
    query = request.args.get('query')  # Get the search query from the URL parameters

    # Fetch the list of YouTube videos based on the search query
    videos = youtube.search().list(
        part='snippet',
        type='video',
        maxResults=10,
        q=query
    ).execute()

    return render_template('index.html', videos=videos['items'])




if __name__ == '__main__':
    app.run()

