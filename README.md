# Youtube playlist to HTML table generator

It takes a public/unlisted playlist (probably private/special playlists too, read below) and renders out an HTML page with list of videos, basic info and thumbnails on hover

## Usage

Requires yt-dlp. `python3 -m pip install yt-dlp`

Add your playlist link at line 12 in script.py, then run script.py. It will create `output` directory in your current working directory with all necessary files. Copy it over to your webserver/ webhost and thats all

## Private/special playlists

You can (probably, I haven't tested it yet!) make pages from private playlists or playlists like your "Watch later" or "Liked videos" by exporting your youtube cookies and adding it as a file with `cookiefile = "cookiefile.txt` into ydl_opts at line 13.
Be aware that the youtube cookies seem to expire very quickly, reference https://github.com/yt-dlp/yt-dlp/issues/8227#issuecomment-1867184804 for more info and workarounds

## Todos

* Using actual template engine instead of whatever it is now, for better genericizing
* Being able to pass more than one playlist at once and generate them on one page
* Config file for playlists, choosing table fields and whatever
* Fun stats about your playlist
