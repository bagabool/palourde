# Spotify Playlist Generator

---

<br>

### Get Artist

---
> Request

```
GET https://api.spotify.com/v1/artists/{{id}}
```

### Get Related Artists

---
> Request

```
GET https://api.spotify.com/v1/artists/{{id}}/related-artists
```

### Create a Playlist

---
> Request

```
POST https://api.spotify.com/v1/users/{{user_id}}/playlists
```


> Body

```json
{
  "name": "{{artist_name}} Mix",
  "public": false
}
```

### Get Artist Top Tracks

---
> Request

```
GET https://api.spotify.com/v1/artists/{{artist_id}}/top-tracks?country={{country_code}}
```

### Add Tracks to Playlist

---
> Request

```
POST https://api.spotify.com/v1/users/{{user_id}}/playlists/{{playlist_id}}/tracks?uris={{uris}}
```

