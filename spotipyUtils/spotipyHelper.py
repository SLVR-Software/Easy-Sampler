import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import cred
import os
import json
from json.decoder import JSONDecodeError
import pprint
import time

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

def get_all_playlist():
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
    return (sp.current_user_playlists(limit=50, offset=0))['items']

def get_track_time_ms(track):
    return(track['duration_ms'])

def get_list_of_playlist_tracks(playlist):
    tracks = []
    for song in playlist['tracks']['items']:
        tracks.append(song['track'])
    return tracks

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
    #sp.start_playback(uris=['spotify:track:7Apgw38C1TgzSaVNpUx1TX'])

    track = sp.current_user_playing_track()
    print(track['item']['duration_ms'])
    #print(sp.current_user_playlists(limit=50, offset=0))
    playlist = get_playlist_uri('Synthetic Rhythms Playlist')
    playlist = (sp.playlist(playlist['id']))
    tracks = get_list_of_playlist_tracks(playlist)
    for track in tracks:
        sp.start_playback(uris=[track['uri']])
        #time.sleep(track['duration_ms'] / 1000)
        time.sleep(10)

def trigger_playback(sp,track):
    sp.start_playback(uris=[track['uri']])
    wait_duration_of_track(track)
    
def wait_duration_of_track(track):
    print("Waiting " + str(track['duration_ms'] / 1000) + " seconds")
    print(track['name'] + ' by ' + track['artists'][0]['name'] + ' is playing....')
    time.sleep(track['duration_ms'] / 1000)


def test():

    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))

    playlist = get_playlist_uri('Synthetic Rhythms Playlist')
    playlist = (sp.playlist(playlist['id']))
    tracks = get_list_of_playlist_tracks(playlist)
    count =0
    for track in tracks:
        trigger_playback(sp, track)

test()
#triggerPlayTrack()

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")