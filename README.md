# Spotify DL

dl for "download"

## Get Started

1. Install the executable from the releases page (if it's out there) or fork/clone the repo.
2. Move to the repo's directory
3. Test the executable using `./dl-spotify test`. You should see the version in the response.
4. Get a client secret and a client id from [spotify developer dashboard](https://developer.spotify.com/) and store them in a .env file under the names `CLIENT_ID` and `CLIENT_SECRET`, respectively.

```
CLIENT_ID = <Your client id here>
CLIENT_SECRET = <Your client secret here>
```

5. Now, to download a playlist simply use the following command

```console
foo@bar:~$ ./dl-spotify download <playlist_link> <output_directory>
```

Voila!

## Reporting/Contributing

This repo is open to issues and pull requests for improvement is welcome !
