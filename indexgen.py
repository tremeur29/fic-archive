import os

import headerfooter

def indexgen(local=False):
    # delete existing file
    if os.path.exists("build/index.html"):
        os.remove("build/index.html")
    # write header
    headerfooter.headerwrite("build/index.html","Tré’s fic archive","Tré’s fic archive","",True,local)
    filewrite = open("build/index.html", "a")
    filewrite.write("<p>Here is all my fanfiction! It’s also archived at AO3 under the name <span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://archiveofourown.org/users/ovely/profile\"><img src=\"https://p.dreamwidth.org/b164c54b26e4/-/archiveofourown.org/favicon.ico\" alt=\"[archiveofourown.org profile]\" width=\"16\" height=\"16\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" /></a><a href=\"https://archiveofourown.org/users/ovely/pseuds/ovely\"><b>ovely</b></a></span>.</p>\n<p><strong>Warning:</strong> some of my fanfiction is NSFW (ranging from slightly obscene language to explicit sex scenes), some is RPF, and some of it contains mature or potentially objectionable themes (death, suicide, mental illness, incest …). Ratings and warnings are given accordingly, <strong>don’t like don’t read</strong>. If you happen to be under 18, kindly gtfo and <em>read some real literature instead</em>. Honestly, it will be much more edifying.</p>\n<p>I’ve recently implemented comments – read about that <a href=\"")
    if local:
        filewrite.write("comments/index.html")
    else:
        filewrite.write("/fic/comments")
    filewrite.write("\">here</a>.</p>\n<p>You can also subscribe to <a href=\"")
    if not local:
        filewrite.write("/fic/")
    filewrite.write("feed.xml\">the RSS feed</a> to be notified of new fics and updates to existing ones.</p>\n<div class=\"fic\">\n<h2><a href=\"")
    if local:
        filewrite.write("masterlist/index.html")
    else:
        filewrite.write("/fic/masterlist")
    filewrite.write("\">Masterlist</a></h2>\n<p>Every fic I’ve ever written since the age of five, sorted newest to oldest.</p>\n</div>\n<div class=\"fic\">\n<h2>Final Fantasy</h2>\n<p>Most of the fics I write are in FF fandoms these days. You can browse them:</p>\n<ul>\n<li><a href=\"")
    if local:
        filewrite.write("ff/characters/index.html")
    else:
        filewrite.write("/fic/ff/characters")
    filewrite.write("\">by character</a></li>\n<li><a href=\"")
    if local:
        filewrite.write("ff/ships/index.html")
    else:
        filewrite.write("/fic/ff/ships")
    filewrite.write("\">by ship</a></li>\n</ul>\n</div>\n<div class=\"fic\">\n<h2><a href=\"")
    if local:
        filewrite.write("events/index.html")
    else:
        filewrite.write("/fic/events")
    filewrite.write("\">Events</a></h2>\n<p>I’ve been participating in fandom exchanges and other events since late 2020. Most fics I write these days that aren’t in FF fandoms are in this category (although a lot of the FF ones are as well).</p>\n</div>\n")
    filewrite.close()
    headerfooter.footerwrite("build/index.html",True,local)

if __name__ == "__main__":
    indexgen()
