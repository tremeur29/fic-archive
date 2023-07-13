import datetime, os
from importlib import import_module

import headerfooter

def statslist(local=False):
    yearlist = []
    ficcount = 500
    while ficcount > 0:
        ficcount -= 1
        if ficcount < 10:
            ficcountstring = "00" + str(ficcount)
        elif ficcount < 100:
            ficcountstring = "0" + str(ficcount)
        else:
            ficcountstring = str(ficcount)
        if os.path.exists("originalsmeta/" + ficcountstring + ".py"):
            ficfile = "originalsmeta." + ficcountstring
            fileread = import_module(ficfile)
        elif os.path.exists("translationsmeta/" + ficcountstring + ".py"):
            ficfile = "translationsmeta." + ficcountstring
            fileread = import_module(ficfile)
        else:
            fileread = False
        if fileread:
            try:
                if fileread.revealdate > datetime.datetime.now():
                    revealed = False
                else:
                    revealed = True
            except:
                revealed = True
            if revealed == True:
                for date in fileread.datewords:
                    yearlist.append(date["date"].year)
                    yearlist = sorted(list(dict.fromkeys(yearlist)))
    linkedyears = []
    for year in yearlist:
        statstring = ""
        if local == True:
            statspath = "/home/mdd/Documents/drive/proj/fic-archive/build/stats/" + str(year) + "/index.html"
        else:
            statspath = "/fic/stats/" + str(year)
        if yearlist.index(year) > 0:
            statstring += "&nbsp;• "
        statstring += "<a href=\"" + statspath + "\">" + str(year)
        if year == (datetime.datetime.now()).year:
            statstring += " (so far)"
        statstring += "</a>"
        linkedyears.append(statstring)
    listofyears = "".join(linkedyears)
    return listofyears

def indexgen(local=False):
    # delete existing file
    if os.path.exists("build/index.html"):
        os.remove("build/index.html")
    # write header
    headerfooter.headerwrite("build/index.html","Tré’s fic archive","Tré’s fic archive","",True,local)
    filewrite = open("build/index.html", "a")
    filewrite.write("<p>Here is all my fanfiction! Much of it is also archived at AO3 under the name <span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://archiveofourown.org/users/ovely/profile\"><img src=\"https://p.dreamwidth.org/b164c54b26e4/-/archiveofourown.org/favicon.ico\" alt=\"[archiveofourown.org profile]\" width=\"16\" height=\"16\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" /></a><a href=\"https://archiveofourown.org/users/ovely/pseuds/ovely\"><b>ovely</b></a></span>.</p>\n<p>I’ve recently implemented comments – read about that <a href=\"")
    if local:
        filewrite.write("comments/index.html")
    else:
        filewrite.write("/fic/comments")
    filewrite.write("\">here</a>.</p>\n<p>You can also subscribe to <a href=\"")
    if not local:
        filewrite.write("/fic/")
    filewrite.write("feed.xml\">the RSS feed</a> to be notified of new fics and updates to existing ones.</p>\n<div class=\"fic\">\n<h2>Masterlist</h2>\n<p>Every fic I’ve written since the age of five. You can view these:\n<ul>\n<li><a href=\"")
    if local:
        filewrite.write("masterlist/index.html")
    else:
        filewrite.write("/fic/masterlist")
    filewrite.write("\">chronologically</a></li>\n<li><a href=\"")
    if local:
        filewrite.write("byfandom/index.html")
    else:
        filewrite.write("/fic/byfandom")
    filewrite.write("\">by fandom</a></li>\n</ul>\n</div>\n<div class=\"fic\">\n<h2>Final Fantasy</h2>\n<p>Most of the fics I write are in FF fandoms these days. You can browse them:</p>\n<ul>\n<li><a href=\"")
    if local:
        filewrite.write("ff/characters/index.html")
    else:
        filewrite.write("/fic/ff/characters")
    filewrite.write("\">by character</a></li>\n<li><a href=\"")
    if local:
        filewrite.write("ff/ships/index.html")
    else:
        filewrite.write("/fic/ff/ships")
    filewrite.write("\">by ship</a></li>\n<li><a href=\"")
    if local:
        filewrite.write("ff/bywords/index.html")
    else:
        filewrite.write("/fic/ff/bywords")
    filewrite.write("\">by length</a></li>\n</ul>\n</div>\n<div class=\"fic\">\n<h2><a href=\"")
    if local:
        filewrite.write("events/index.html")
    else:
        filewrite.write("/fic/events")
    filewrite.write("\">Events</a></h2>\n<p>I’ve been participating in fandom exchanges and other events since late 2020. Most fics I write these days that aren’t in FF fandoms are in this category (although a lot of the FF ones are as well).</p>\n</div>\n<div class=\"fic\">\n<h2>Other</h2>\n<ul>\n<li>Stats by year: " + (str(statslist(local))) + "</li>\n</ul>\n</div>\n")
    filewrite.close()
    headerfooter.footerwrite("build/index.html",True,local)

if __name__ == "__main__":
    statslist(True)
    indexgen(True)
