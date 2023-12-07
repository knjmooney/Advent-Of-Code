Scripts for parsing data from the leaderboard API.
==================================================

## Cookie.json
You need a cookie.json file in your current working directory. It should be of
the form

    -> cat cookie.json
    {
      "session": "<YOUR SESSION COOKIE>"
    }

You should be able to get your session cookie from your browser's developer
console (F12?).

## Leaderboard code
You also need to pass your leaderboard code, which you can get from the URL of
your leaderboard.

## Caching
The requests are cached in http_cache.sqlite, so you may need to clear the cache
if the data is out of date.
