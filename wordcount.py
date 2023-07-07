import datetime, os
from importlib import import_module

fffandoms = ["FF1","FF2","FF3","FF4","FF5","FF6","FF7","FF8","FF9","FFX","FF11","FF12","FF13","FF14","FF15","FF16"]

import makeheader
import headerfooter

def bywords(local=False):
    # delete existing file
    if os.path.exists("build/ff/bywords/index.html"):
        os.remove("build/ff/bywords/index.html")
    # write header
    headerfooter.headerwrite("build/ff/bywords/index.html","FF fics by word count","FF fics by word count","<p>On this page, my FF fics are sorted from longest to shortest. (Fics with translations are listed according to the wordcount of the original version; the wordcount for the translation is normally pretty close to this.)</p>",False,local)
    # iterate through fandoms
    ficlist = []
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
                fffic = False
                for fandom in fileread.fandom:
                    if fandom in fffandoms:
                        fffic = True
                if fffic == True:
                    sumwords = 0
                    for instalment in fileread.datewords:
                        sumwords = sumwords + instalment["words"]
                    ficlist.append({"ficno":ficcount,"length":sumwords})
    ficlist = sorted(ficlist, key=lambda d: d["length"],reverse=True)
    # write fic headers
    for fic in ficlist:
        makeheader.ficgen(fic["ficno"],False,"build/ff/bywords/index.html",local)
    # write footer
    headerfooter.footerwrite("build/ff/bywords/index.html",False,local)

if __name__ == "__main__":
    bywords(True)
