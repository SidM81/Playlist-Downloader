from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url,headers=headers,data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_tracks(playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)["items"]
    return json_result

def get_list(Tracks):
    f = open("Songs.txt","w")
    for idx, track in enumerate(Tracks):
        f.write(f"{idx+1}. {track['track']['name']}\n")
    f.close()

token = get_token()

def main():
    Playlist = input("Paste the Playlist link\n")
    # https://open.spotify.com/playlist/2k2bpZ8OGRT6DHpawW5Ejg?si=e71891c67e7a4b9d
    # https://open.spotify.com/playlist/6JUfHVDExHgtIAQZUFvwOt?si=4036fe117cda4451
    playlist_id = Playlist[34:56]
    Tracks = get_tracks(playlist_id)
    get_list(Tracks)

if __name__ == '__main__' :
    main()