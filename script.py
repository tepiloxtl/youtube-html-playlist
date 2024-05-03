import yt_dlp, json, pprint, requests, os, datetime, shutil

if not os.path.exists("output"):
    os.makedirs("output/thumbs")

thumbslist = [os.path.splitext(filename)[0] for filename in os.listdir("output/thumbs")]
newthumbslist = []
#print(thumbslist)

#URL = "https://youtube.com/playlist?list=PLsx_B-fRIIQj4ystOGcuDdc408WSkDXF2"
#URL = 'https://www.youtube.com/playlist?list=PLsx_B-fRIIQhXHhWeK-1cDqG6uX9vLkpU'
URL = "https://www.youtube.com/playlist?list=PLsx_B-fRIIQhZMqBqEhBxXxzIMjLh12f9"
ydl_opts = {}
playlists = []
#f = open("output.json", "w", encoding="utf-8")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    playlistinfo = {}
    info = ydl.sanitize_info(ydl.extract_info(URL, download=False))
    #json.dump(info, ensure_ascii=False, indent=4, fp=f)
    playlistinfo["title"] = info["title"]
    playlistinfo["id"] = info["id"]
    playlistinfo["entries"] = {}
    print(info["title"])
    for item in info["entries"]:
        playlistinfo["entries"][str(item["id"])] = {"title": item["title"], "category": item["categories"][0], "duration": item["duration"], "channel": item["channel"], "uploaddate": item["upload_date"]}
    pprint.pprint(playlistinfo, indent = 4)
    playlists.append(playlistinfo)
#f.close()

thumbelement = """<script language=JavaScript src="thumb.js" type=text/javascript></script>
<div id=thumb style="Z-INDEX: 333; left: 0px; VISIBILITY: hidden; POSITION: absolute; top: 0px"></div>"""

tablestart = """<table style="width:100%">
<tbody><tr>
<th style="width:10%">Category</th>
<th style="width:5%">Length</th>
<th style="width:3%">Link</th>
<th style="width:45%">Title</th>
<th style="width:22%">Uploader</th>
<th style="width:15%">Upload date</th>
</tr>"""

tableentry = """<tr onmouseover="showthumb('{}',1)" 
onmouseout="showthumb('',0)"><td>{}</td>
<td><b>{}</b></td>
<td><a href="https://www.youtube.com/watch?v={}">🔗</a></td>
<td>{}</td>
<td>{}</td>
<td>{}</td></tr>"""

tableend = """</tbody></table>"""

contentbody = ""
for playlist in playlists:
    title = """<h2><a href="https://www.youtube.com/playlist?list={}">{}</a></h2>""".format(str(playlist["id"]), str(playlist["title"]))
    table = []
    for video in playlist["entries"]:
        videodata = playlist["entries"][str(video)]
        table.append(tableentry.format(str(video), str(videodata["category"]), str(datetime.timedelta(seconds=videodata["duration"])), str(video), str(videodata["title"]), str(videodata["channel"]), str(videodata["uploaddate"][0:4] + "-" + videodata["uploaddate"][4:6] + "-" + videodata["uploaddate"][6:8])))
        newthumbslist.append(str(video))
        if str(video) not in thumbslist:
            thumbslist.append(str(video))
            open("output/thumbs/" + str(video) + ".jpg", 'wb').write(requests.get("https://i.ytimg.com/vi/" + str(video) + "/hqdefault.jpg", allow_redirects=True).content)
    contentbody = contentbody + "\n".join([title, tablestart, *table, tableend])

#f = open("content.html", "w", encoding = "utf-8")
#f.write(contentbody)
#f.close
f = open("template.html", "r", encoding="utf-8")
template = f.read().split("<!-- !content goes here! -->")
f.close()

f = open("output/index.html", "w", encoding="utf-8")
f.write("\n".join([template[0], contentbody, thumbelement, template[1]]))
f.close()

shutil.copy("thumb.js", "output/")
shutil.copy("table.css", "output/")