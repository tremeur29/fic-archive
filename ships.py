import os
from importlib import import_module

fffandoms = ["FF1","FF2","FF3","FF4","FF5","FF6","FF7","FF8","FF9","FFX","FF11","FF12","FF13","FF14","FF15"]

import makeheader
import headerfooter

def shiplist(local=False):
    # delete existing file
    if os.path.exists("build/ff/ships/index.html"):
        os.remove("build/ff/ships/index.html")
    # write header
    headerfooter.headerwrite("build/ff/ships/index.html","FF fics by ship","FF fics by ship","<p>Click on each bar to see fics involving that ship, organised according to whether it’s the main ship or a secondary one and then from newest to oldest.</p>",False,local)
    # iterate through fandoms
    ships = []
    numbers = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen"]
    for fandom in fffandoms:
        theships = []
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
                if len(fileread.fandom) == 1:
                    if fandom in fileread.fandom:
                        try:
                            theships.extend(fileread.ship)
                        except:
                            pass
        for ship in theships:
            if ship == None:
                theships.remove(ship)
        theships = sorted(list(dict.fromkeys(theships)))
        for ship in theships:
            shipdict = {"pairing":ship,"game":(fffandoms.index(fandom) + 1)}
            ships.append(shipdict)
    shiplist = sorted(ships, key=lambda d: d["pairing"])
    for aship in shiplist:
        maincount = []
        secondarycount = []
        ship = aship["pairing"]
        searchfandom = fffandoms[(aship["game"]) - 1]
        cssgame = numbers[(aship["game"]) - 1]
        # check all fics in specified fandom
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
                if searchfandom in fileread.fandom:
                    # append to lists
                    try:
                        if fileread.ship[0] == ship:
                            maincount.append(ficcount)
                        elif ship in fileread.ship:
                            secondarycount.append(ficcount)
                    except:
                        pass
        # write details element
        output = "build/ff/ships/index.html"
        filewrite = open(output, "a")
        filewrite.write("<details><summary><span class=\"character " + cssgame + "\">" + ship + "</span> ")
        # write statistics
        if len(maincount) > 0:
            filewrite.write("<span class=\"main\">" + str(len(maincount)) + "</span>")
        if len(secondarycount) > 0:
            filewrite.write("<span class=\"secondary\">" + str(len(secondarycount)) + "</span>")
        filewrite.write("</summary>\n")
        filewrite.close()
        # write fic headers in each category
        if len(maincount) > 0:
            filewrite = open(output, "a")
            filewrite.write("<h1>Main ship</h1>\n")
            filewrite.close()
            for fic in maincount:
                makeheader.ficgen(fic,False,output,local)
        if len(secondarycount) > 0:
            filewrite = open(output, "a")
            filewrite.write("<h1>Secondary ship</h1>\n")
            filewrite.close()
            for fic in secondarycount:
                makeheader.ficgen(fic,False,output,local)
        filewrite = open(output, "a")
        filewrite.write("</details>\n")
        filewrite.close()
    # write footer
    headerfooter.footerwrite("build/ff/ships/index.html",False,local)

if __name__ == "__main__":
    shiplist()
