import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '84ef05fc5f084a8cb0a368d030c2f3d4'
secret = '63938954d0c04976894cabc84eb381f9'

client_credentials_manager = SpotifyClientCredentials(client_id=cid,
client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,10000,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

print(artist_name)
print(popularity)