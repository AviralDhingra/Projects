import os
import sys

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# try:
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials())
# except spotipy.oauth2.SpotifyOauthError:
#     clientId = input('Please ENter CLient ID: ')
#     clientScretId = input('Please enter client secret ID: ')
#     os.system(f'export SPOTIPY_CLIENT_ID={clientId}')
#     os.system(f'export SPOTIPY_CLIENT_ID={clientScretId}')
#     # os.system(f'export SPOTIPY_REDIRECT_URI=http://localhost:8888/callback')
#     spotify = spotipy.Spotify(
#         client_credentials_manager=SpotifyClientCredentials())


def listAlbumsOfArtisti(artist_uri):
    artist_uri = artist_uri
    # Birdy >> spotify:artist:2WX2uTcsvV5OnS0inACecP

    results = spotify.artist_albums(artist_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])


def Top10TracksOfArtist(artistURI):
    """
    https://open.spotify.com/artist/58lV9VcRSjABbAbfWS6skp?si=zIksO03sTb2dc3aql_YJFw&dl_branch=1
                =>
    spotify:artist:58lV9VcRSjABbAbfWS6skp
    """
    artistURI = artistURI
    # Led Zeplin: spotify:artist:36QJpDe2go2KgaRleHCDTp
    # Bon Jovi: spotify:artist:58lV9VcRSjABbAbfWS6skp

    results = spotify.artist_top_tracks(artistURI)

    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()


def getArtistPFP(artist_name):
    artist_name = artist_name
    name = ' '.join(artist_name)

    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        print(artist['name'], artist['images'][0]['url'])


# listAlbumsOfArtisti('spotify:artist:2WX2uTcsvV5OnS0inACecP')
# Top10TracksOfArtist('spotify:artist:36QJpDe2go2KgaRleHCDTp')
getArtistPFP('Bryan Adams')

# topPlayedSongsUser = spotify.getCategoryPlaylists('toplists')
# print(topPlayedSongsUser)
# print(type(topPlayedSongsUser))
