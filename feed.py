import datetime, os, re
from importlib import import_module

"""
Code to generate RSS feed
"""

def feedgen(local=False):
    # delete existing file
    if os.path.exists("build/feed.xml"):
        os.remove("build/feed.xml")
    # write header
    header = open("build/feed.xml", "a")
    header.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<rss version=\"2.0\" xmlns:atom=\"http://www.w3.org/2005/Atom\">\n<channel>\n<atom:link href=\"https://tre.praze.net/fic/feed.xml\" rel=\"self\" type=\"application/rss+xml\" />\n<title>Tré’s fic archive</title>\n<link>https://tre.praze.net/fic</link>\n<description>All my fanfiction</description>\n<language>en-gb</language>\n")
    header.close()
    datelist = []
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
            for instalment in fileread.datewords:
                datelist.append(instalment["date"])
        elif os.path.exists("translationsmeta/" + ficcountstring + ".py"):
            ficfile = "translationsmeta." + ficcountstring
            fileread = import_module(ficfile)
            for instalment in fileread.datewords:
                datelist.append(instalment["date"])
    newlist = []
    for date in datelist:
        if date not in newlist:
            newlist.append(date)
    newlist = sorted(newlist,reverse=True)
    for date in newlist:
        ficcount = 500
        while ficcount > 0:
            ficcount -= 1
            if ficcount < 10:
                ficcountstring = "00" + str(ficcount)
            elif ficcount < 100:
                ficcountstring = "0" + str(ficcount)
            else:
                ficcountstring = str(ficcount)
            targetfile = 0
            if os.path.exists("originalsmeta/" + ficcountstring + ".py"):
                ficfile = "originalsmeta." + ficcountstring
                fileread = import_module(ficfile)
                for instalment in fileread.datewords:
                    if instalment["date"] == date:
                        if targetfile == 0:
                            targetfile = ficfile
            elif os.path.exists("translationsmeta/" + ficcountstring + ".py"):
                transfile = "translationsmeta." + ficcountstring
                transread = import_module(transfile)
                for instalment in transread.datewords:
                    if instalment["date"] == date:
                        if targetfile == 0:
                            targetfile = transfile
            else:
                targetfile = 0
            if targetfile:
                thefile = import_module(targetfile)
                filewrite = open("build/feed.xml", "a")
                filewrite.write("<item>\n<title>")
                if (thefile.datewords[0])["date"] != date:
                    filewrite.write("Updated: ")
                filewrite.write("Fic " + ficcountstring)
                if thefile.language == "fr":
                    filewrite.write (" (French)")
                filewrite.write(": ")
                try:
                    origfile = "originalsmeta." + str(thefile.original)
                    origread = import_module(origfile)
                    try:
                        filewrite.write(origread.fandomtext)
                    except:
                        filewrite.write("/".join(origread.fandom))
                    try:
                        filewrite.write(", " + origread.ship[0])
                    except:
                        try:
                            filewrite.write(", " + ", ".join(origread.charpov))
                        except:
                            pass
                        try:
                            filewrite.write(", " + ", ".join(origread.charmain))
                        except:
                            pass
                    if origread.rating == "g":
                        therating = "G"
                    elif origread.rating == "t":
                        therating = "T"
                    elif origread.rating == "m":
                        therating = "M"
                    elif origread.rating == "e":
                        therating = "X"
                    filewrite.write(", rated " + therating)
                    if len(origread.genre) > 1:
                        genred = False
                        for thegenre in origread.genre:
                            if genred == False:
                                if thegenre == "gen" or thegenre == "slash" or thegenre == "pre-slash" or thegenre == "poly slash" or thegenre == "het" or thegenre == "pre-het" or thegenre == "femslash" or thegenre == "poly" or thegenre == "masturbation":
                                    pass
                                else:
                                    filewrite.write(", " + thegenre)
                                    genred = True
                except:
                    try:
                        filewrite.write(thefile.fandomtext)
                    except:
                        filewrite.write("/".join(thefile.fandom))
                    try:
                        filewrite.write(", " + thefile.ship[0])
                    except:
                        try:
                            filewrite.write(", " + ", ".join(thefile.charpov))
                        except:
                            pass
                        try:
                            filewrite.write(", " + ", ".join(thefile.charmain))
                        except:
                            pass
                    if thefile.rating == "g":
                        therating = "G"
                    elif thefile.rating == "t":
                        therating = "T"
                    elif thefile.rating == "m":
                        therating = "M"
                    elif thefile.rating == "e":
                        therating = "X"
                    filewrite.write(", rated " + therating)
                    if len(thefile.genre) > 1:
                        genred = False
                        for thegenre in thefile.genre:
                            if genred == False:
                                if thegenre == "gen" or thegenre == "slash" or thegenre == "pre-slash" or thegenre == "poly slash" or thegenre == "het" or thegenre == "pre-het" or thegenre == "femslash" or thegenre == "poly" or thegenre == "masturbation":
                                    pass
                                else:
                                    filewrite.write(", " + thegenre)
                                    genred = True
                filewrite.write("</title>\n<pubDate>")
                futuredate = date + datetime.timedelta(days=2)
                filewrite.write(futuredate.strftime("%a, %-d %b %Y"))
                filewrite.write(" 00:00:00 UT</pubDate>\n<link>")
                if local:
                    filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/masterlist")
                else:
                    filewrite.write("https://tre.praze.net/fic/masterlist")
                filewrite.write("#fic" + ficcountstring + "</link>\n<guid isPermaLink=\"false\">praze-fic-" + ficcountstring)
                datecount = 0
                dateindex = 0
                for instalment in thefile.datewords:
                    if date == instalment["date"]:
                        dateindex = datecount
                    datecount += 1
                if dateindex > 0:
                    filewrite.write("-" + str(dateindex + 1))
                filewrite.write("</guid>\n<description>")
                filewrite.write(str((thefile.datewords[dateindex])["words"]) + " words")
                if dateindex > 0:
                    filewrite.write(" in this update")
                filewrite.write(".")
                try:
                    filewrite.write(" " + re.sub("<[^<]+?>", "", thefile.summary))
                except:
                    filewrite.write(" No summary provided.")
                try:
                    filewrite.write(" A translation of fic " + str(thefile.original) + ".")
                except:
                    pass
                filewrite.write("</description>\n</item>\n")
                filewrite.close()
    # write footer
    footer = open("build/feed.xml", "a")
    footer.write("</channel>\n</rss>")
    footer.close()

if __name__ == "__main__":
    feedgen()
