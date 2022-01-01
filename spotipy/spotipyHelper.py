import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import cred
import os
import json
from json.decoder import JSONDecodeError
import pprint

def printRecentlyPlayedTracks():
    scope = "user-read-recently-played"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))

    results = sp.current_user_recently_played()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " - ", track['name'])

def get_playlist_uri(playlistName):
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
    playlist = sp.current_user_playlists(limit=50, offset=0)
    for item in playlist['items']:
        if item['name'] == playlistName:
            return item

def triggerPlayTrack():
    username = '12121511576'
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'

    '''
    try:
        token = util.prompt_for_user_token(username, scope)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)
    '''
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
    
    devices = sp.devices()
    print(json.dumps(devices, sort_keys=True, indent=4))
    deviceID = devices['devices'][0]['id']

    # Get track information
    track = sp.current_user_playing_track()
    print(json.dumps(track, sort_keys=True, indent=4))
    print()
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']

    if artist !="":
        print("Currently playing " + artist + " - " + track) 
    sp.start_playback(uris=['spotify:track:7Apgw38C1TgzSaVNpUx1TX'])

    track = sp.current_user_playing_track()
    print(track['item']['duration_ms'])
    #print(sp.current_user_playlists(limit=50, offset=0))
    print(get_playlist_uri('Food Songs')['name'])

triggerPlayTrack()
