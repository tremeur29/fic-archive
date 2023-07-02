import datetime, os
from importlib import import_module

import makeheader
import headerfooter

def fandomlist(local=False):
    # delete existing file
    if os.path.exists("build/byfandom/index.html"):
        os.remove("build/byfandom/index.html")
    # write header
    headerfooter.headerwrite("build/byfandom/index.html","Fics by fandom","Fics by fandom","<p>On this page, you’ll find basically everything I’ve ever written that is a. fanfiction and b. extant, grouped by fandom and then sorted newest to oldest; quality may vary. RPF and things I wrote before 2020 require a username and password to access.</p>",False,local)
    # get list of fandoms
    fandoms = []
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
            try:
                if fileread.revealdate > datetime.datetime.now():
                    revealed = False
                else:
                    revealed = True
            except:
                revealed = True
            if revealed == True:
                for fandom in fileread.fandom:
                    fandoms.append(fandom)
    newlist = []
    for fandom in fandoms:
        if fandom not in newlist:
            newlist.append(fandom)
    fandomlist = []
    for fandom in newlist:
        if "FF" in fandom:
            if fandom == "FFX":
                newfandom = "FF10"
            elif len(fandom) == 3:
                newfandom = "FF0" + fandom[-1]
            else:
                newfandom = fandom
            fandomlist.append({"searchname":fandom,"sortname":newfandom.replace("FF","Final Fantasy ").lower(),"displayname":fandom.replace("FF","Final Fantasy ")})
        else:
            fandomlist.append({"searchname":fandom,"sortname":fandom.lower(),"displayname":fandom})
    fandomlist = sorted(fandomlist, key=lambda d: d["sortname"])
    for fandom in fandomlist:
        fandomfics = []
        # check which fics are in the fandom
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
                countfile = "originalsmeta." + ficcountstring
                fileread = import_module(countfile)
                try:
                    if fileread.revealdate > datetime.datetime.now():
                        revealed = False
                    else:
                        revealed = True
                except:
                    revealed = True
                if revealed == True:
                    if fandom["searchname"] in fileread.fandom:
                        fandomfics.append(ficcount)
        firstfic = fandomfics[-1]
        if firstfic < 10:
            firstficstring = "00" + str(firstfic)
        elif firstfic < 100:
            firstficstring = "0" + str(firstfic)
        else:
            firstficstring = str(firstfic)
        firstfile = "originalsmeta." + firstficstring
        firstread = import_module(firstfile)
        firstyear = (firstread.datewords[0])["date"].year
        lastfic = fandomfics[0]
        if lastfic < 10:
            lastficstring = "00" + str(lastfic)
        elif lastfic < 100:
            lastficstring = "0" + str(lastfic)
        else:
            lastficstring = str(lastfic)
        lastfile = "originalsmeta." + lastficstring
        lastread = import_module(lastfile)
        lastyear = (lastread.datewords[0])["date"].year
        if lastyear == firstyear:
            yearstring = str(firstyear)
        else:
            yearstring = str(firstyear) + "–" + str(lastyear)
        # write details element
        output = "build/byfandom/index.html"
        filewrite = open(output, "a")
        filewrite.write("<details><summary><b>" + fandom["displayname"] + "</b> (" + str(len(fandomfics)) + " fic")
        if len(fandomfics) > 1:
            filewrite.write("s")
        filewrite.write(", " + yearstring + ")</summary>\n")
        filewrite.close()
        for fic in fandomfics:
            makeheader.ficgen(fic,False,output,local)
        filewrite = open(output, "a")
        filewrite.write("</details>\n")
        filewrite.close()
    # write footer
    headerfooter.footerwrite("build/byfandom/index.html",False,local)

if __name__ == "__main__":
    fandomlist(True)
