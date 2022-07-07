from urllib.request import pathname2url
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from pytube import Search
import typer

app = typer.Typer()


load_dotenv("E:\code\spotify-playlist-downloader\.env")
cid = os.environ.get("CLIENT_ID")
secret = os.environ.get("CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def do_stuff(playlist_link : str, destination : str):
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    playlist_name = "".join(c for c in sp.playlist(playlist_URI)["name"] if c.isalpha())
    black_list = ['<', '>', ':', '"', '/', '|', '?', '*']
    playlist = sp.playlist_tracks(playlist_URI)
    results = [{"name" : "".join(c for c in x["track"]["name"] + ' by '+ x["track"]["artists"][0]["name"] + '.mp3' if c not in black_list), "result" : Search(x["track"]["name"] + ' by '+ x["track"]["artists"][0]["name"]).results[0], "artist" : x["track"]["artists"][0]["name"], "cover_art" : x["track"]["album"]["images"][0]["url"]} for x in playlist["items"]]

    for i in results:
        streams = i["result"].streams.filter(only_audio = True)
        file_location = destination + playlist_name
        streams[0].download(file_location, i["name"])
        # change_album_details(file_location+ '/' + i["name"], i["artist"],i["cover_art"])
        typer.echo(i["name"])

@app.command()
def test():
    typer.echo("Hey there ! This is v1.0.0")

@app.command()
def download(playlist_link, folder_to_save):
    typer.echo(f"Starting to download songs. Please wait ⏱️...\n===========================")
    do_stuff(playlist_link, folder_to_save)
    typer.echo(f"===========================\nDone downloading all songs. Enjoy 🎧!")

if __name__ == "__main__":
    app()


