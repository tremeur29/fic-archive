import datetime, os
from importlib import import_module

fffandoms = ["FF1","FF2","FF3","FF4","FF5","FF6","FF7","FF8","FF9","FFX","FF11","FF12","FF13","FF14","FF15"]

import makeheader
import headerfooter

def charlist(local=False):
    # delete existing file
    if os.path.exists("build/ff/characters/index.html"):
        os.remove("build/ff/characters/index.html")
    # write header
    headerfooter.headerwrite("build/ff/characters/index.html","FF fics by character","FF fics by character","<p>Click on each bar to see fics about that character, organised according to the character’s prominence and then from newest to oldest.</p>\n<p>Key to categories:</p>\n<ul><li><b>POV character:</b> some or all of the fic is in this character’s POV</li>\n<li><b>Main character:</b> the character is part of the main ship, or their actions are significant for the plot</li>\n<li><b>Secondary character:</b> the character appears saying or doing something specific</li>\n<li><b>Mentioned:</b> the character appears as part of a group, or they’re alluded to by another character or in the narration</li></ul>",False,local)
    # iterate through fandoms
    characters = []
    numbers = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen"]
    for fandom in fffandoms:
        thecharacters = []
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
                    if len(fileread.fandom) == 1:
                        if fandom in fileread.fandom:
                            try:
                                thecharacters.extend(fileread.charpov)
                            except:
                                pass
                            try:
                                thecharacters.extend(fileread.charmain)
                            except:
                                pass
                            try:
                                thecharacters.extend(fileread.charsecondary)
                            except:
                                pass
                            try:
                                thecharacters.extend(fileread.charmention)
                            except:
                                pass
        thecharacters = sorted(list(dict.fromkeys(thecharacters)))
        for character in thecharacters:
            if character != "OCs":
                chardict = {"name":character,"game":(fffandoms.index(fandom) + 1)}
                characters.append(chardict)
    charlist = sorted(characters, key=lambda d: d["name"])
    for person in charlist:
        povcount = []
        maincount = []
        secondarycount = []
        mentioncount = []
        character = person["name"]
        searchfandom = fffandoms[(person["game"]) - 1]
        cssgame = numbers[(person["game"]) - 1]
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
                try:
                    if fileread.revealdate > datetime.datetime.now():
                        revealed = False
                    else:
                        revealed = True
                except:
                    revealed = True
                if revealed == True:
                    if searchfandom in fileread.fandom:
                        # append to lists
                        try:
                            if character in fileread.charpov:
                                povcount.append(ficcount)
                        except:
                            pass
                        try:
                            if character in fileread.charmain:
                                maincount.append(ficcount)
                        except:
                            pass
                        try:
                            if character in fileread.charsecondary:
                                secondarycount.append(ficcount)
                        except:
                            pass
                        try:
                            if character in fileread.charmention:
                                mentioncount.append(ficcount)
                        except:
                            pass
        # write details element
        output = "build/ff/characters/index.html"
        filewrite = open(output, "a")
        filewrite.write("<details><summary><span class=\"character " + cssgame + "\">" + character + "</span> ")
        # write statistics
        if len(povcount) > 0:
            filewrite.write("<span class=\"pov\">" + str(len(povcount)) + "</span>")
        if len(maincount) > 0:
            filewrite.write("<span class=\"main\">" + str(len(maincount)) + "</span>")
        if len(secondarycount) > 0:
            filewrite.write("<span class=\"secondary\">" + str(len(secondarycount)) + "</span>")
        if len(mentioncount) > 0:
            filewrite.write("<span class=\"mention\">" + str(len(mentioncount)) + "</span>")
        filewrite.write("</summary>\n")
        filewrite.close()
        # write fic headers in each category
        if len(povcount) > 0:
            filewrite = open(output, "a")
            filewrite.write("<h1>POV character</h1>\n")
            filewrite.close()
            for fic in povcount:
                makeheader.ficgen(fic,False,output,local)
        if len(maincount) > 0:
            filewrite = open(output, "a")
            filewrite.write("<h1>Main character</h1>\n")
            filewrite.close()
            for fic in maincount:
                makeheader.ficgen(fic,False,output,local)
        if len(secondarycount) > 0:
            filewrite = open(output, "a")
            filewrite.write("<h1>Secondary character</h1>\n")
            filewrite.close()
            for fic in secondarycount:
                makeheader.ficgen(fic,False,output,local)
        if len(mentioncount) > 0:
            filewrite = open(output, "a")
            filewrite.write("<h1>Mentioned</h1>\n")
            filewrite.close()
            for fic in mentioncount:
                makeheader.ficgen(fic,False,output,local)
        filewrite = open(output, "a")
        filewrite.write("</details>\n")
        filewrite.close()
    # write footer
    headerfooter.footerwrite("build/ff/characters/index.html",False,local)

if __name__ == "__main__":
    charlist()
