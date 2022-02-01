# process flow
"""
Step 1: Log into Youtube
Step 2: Fetch liked videos
Step 3: Create a new playlist
Step 4: Search for the song
Step 5: Add this song into the new Spotify playlist
"""

import json
import requests
from secrets import spotify_user_id, spotify_token


class CreatePlaylist:

    def __init__(self):
        self.user_id = spotify_user_id
        self.token = spotify_token

    # Step 1: Log into Youtube
    def get_youtube_client(self):
        pass

    # Step 2: Fetch Liked Videos
    def get_liked_videos(self):
        pass

    # Step 3: Create a New Playlist
    def create_playlist(self):
        request_body = json.dumps({
            'name': 'Liked Youtube Music ',
            'description': 'Liked music videos from Youtube',
            'public': 'True'
        })

        query = "https://api.spotify.com/v1/users/{user_id}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json['id']

    # Step 4: Search for the song
    def get_spotify_uri(self, song_name, artis):
        pass

    # Step 5: Add Song to New Spotify Playlist
    def add_song_to_playlist(self):
        pass
