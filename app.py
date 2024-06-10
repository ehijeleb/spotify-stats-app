from flask import Flask, render_template, redirect, url_for, request, session
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import Counter
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Load configuration from config.py
app.config.from_object('config')

# Spotify credentials and scopes
CLIENT_ID = app.config['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = app.config['SPOTIPY_CLIENT_SECRET']
REDIRECT_URI = app.config['SPOTIPY_REDIRECT_URI']
SCOPE = "user-top-read user-library-read user-read-private"

@app.route('/')
def index():
    # Clear the session data to force login each time
    session.clear()
    return render_template('index.html')

@app.route('/login')
def login():
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect(url_for('top_tracks'))

def get_top_items(sp, item_type, time_range):
    if item_type == 'tracks':
        items = sp.current_user_top_tracks(limit=50, time_range=time_range)['items']
        return items
    if item_type == 'artists':
        items = sp.current_user_top_artists(limit=50, time_range=time_range)['items']
        return items

@app.route('/top_tracks')
def top_tracks():
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('index'))

    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
    token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    session['token_info'] = token_info

    sp = spotipy.Spotify(auth=token_info['access_token'])
    time_ranges = ['short_term', 'medium_term', 'long_term']
    top_tracks = {time_range: get_top_items(sp, 'tracks', time_range) for time_range in time_ranges}

    return render_template('top_tracks.html', top_tracks=top_tracks)

@app.route('/top_artists/<time_range>')
def top_artists(time_range):
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('index'))

    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
    token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    session['token_info'] = token_info

    sp = spotipy.Spotify(auth=token_info['access_token'])
    top_artists = get_top_items(sp, 'artists', time_range)

    return render_template('top_artists.html', top_artists=top_artists, time_range=time_range)

@app.route('/top_albums/<time_range>')
def top_albums(time_range):
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('index'))

    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
    token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    session['token_info'] = token_info

    sp = spotipy.Spotify(auth=token_info['access_token'])
    top_tracks = get_top_items(sp, 'tracks', time_range)

    # Aggregate album occurrences
    album_counter = Counter()
    album_info = {}

    for track in top_tracks:
        album = track['album']
        album_id = album['id']
        album_name = album['name']
        album_counter[album_id] += 1
        if album_id not in album_info:
            album_info[album_id] = {
                'name': album_name,
                'images': album['images'],
                'artist': album['artists'][0]['name'] if album['artists'] else ''
            }

    # Create a sorted list of albums based on occurrence counts
    top_albums = [
        {'id': album_id, 'name': album_info[album_id]['name'], 'count': count, 'images': album_info[album_id]['images'], 'artist': album_info[album_id]['artist']}
        for album_id, count in album_counter.most_common()
    ]

    return render_template('top_albums.html', top_albums=top_albums, time_range=time_range)

if __name__ == '__main__':
    app.run(debug=True)
