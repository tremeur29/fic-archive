import datetime, os, shutil
from importlib import import_module

"""
Warning: code in this file is /particularly/ bizarre and non-optimised.
"""

"""
Write the wee blurb for each fic
"""

def ficsum(ficcount,year,month=0,showfandom=True,local=False):
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
            theorig = "originalsmeta." + str(fileread.original)
            origfile = import_module(theorig)
        except:
            pass
        try:
            fandom = "/".join(origfile.fandom)
        except:
            fandom = "/".join(fileread.fandom)
        thechars = ""
        try:
            if "OW" not in origfile.fandom:
                if "gen" not in origfile.genre:
                    try:
                        thechars = origfile.ship[0]
                    except:
                        chars = []
                        try:
                            chars.extend(origfile.charpov)
                        except:
                            pass
                        try:
                            chars.extend(origfile.charmain)
                        except:
                            pass
                        if chars != []:
                            thechars = ", ".join(chars)
                        else:
                            thechars = ""
                else:
                    chars = []
                    try:
                        chars.extend(origfile.charpov)
                    except:
                        pass
                    try:
                        chars.extend(origfile.charmain)
                    except:
                        pass
                    if chars != []:
                        thechars = ", ".join(chars)
                    else:
                        thechars = ""
            else:
                thechars = ""
        except:
            if "OW" not in fileread.fandom:
                if "gen" not in fileread.genre:
                    try:
                        thechars = fileread.ship[0]
                    except:
                        chars = []
                        try:
                            chars.extend(fileread.charpov)
                        except:
                            pass
                        try:
                            chars.extend(fileread.charmain)
                        except:
                            pass
                        if chars != []:
                            thechars = ", ".join(chars)
                        else:
                            thechars = ""
                else:
                    chars = []
                    try:
                        chars.extend(fileread.charpov)
                    except:
                        pass
                    try:
                        chars.extend(fileread.charmain)
                    except:
                        pass
                    if chars != []:
                        thechars = ", ".join(chars)
                    else:
                        thechars = ""
            else:
                thechars = ""
        if thechars == "":
            thechars = "no characters specified"
        if fileread.language == "fr":
            language = "French"
        else:
            language = ""
        try:
            rating = origfile.rating
        except:
            rating = fileread.rating
        genre = []
        try:
            for thegenre in origfile.genre:
                if thegenre == "gen":
                    genre.append(thegenre)
                elif thegenre == "het" or thegenre == "pre-het":
                    genre.append("het")
                elif thegenre == "slash" or thegenre == "pre-slash" or thegenre == "poly slash":
                    genre.append("slash")
                elif thegenre == "femslash":
                    genre.append("femslash")
                elif thegenre == "poly":
                    genre.append("multi")
                elif thegenre == "masturbation":
                    genre.append("other")
        except:
            for thegenre in fileread.genre:
                if thegenre == "gen":
                    genre.append(thegenre)
                elif thegenre == "het" or thegenre == "pre-het":
                    genre.append("het")
                elif thegenre == "slash" or thegenre == "pre-slash" or thegenre == "poly slash":
                    genre.append("slash")
                elif thegenre == "femslash":
                    genre.append("femslash")
                elif thegenre == "poly":
                    genre.append("multi")
                elif thegenre == "masturbation":
                    genre.append("other")
        try:
            if origfile.warnings:
                warnings = "?!"
        except:
            try:
                if fileread.warnings:
                    warnings = "?!"
            except:
                warnings = ""
        words = 0
        for datewords in fileread.datewords:
            if month:
                if int((datewords["date"]).year) == year:
                    if int((datewords["date"]).month) == month:
                        words += datewords["words"]
            else:
                if int((datewords["date"]).year) == year:
                    words += datewords["words"]
        ficstring = ""
        ficstring += "<a href=\""
        if local:
            ficstring += "/home/mdd/Documents/drive/proj/fic-archive/build/masterlist/index.html"
        else:
            ficstring += "/fic/masterlist"
        ficstring += "#fic"
        try:
            ficstring += str(fileread.original)
        except:
            ficstring += ficcountstring
        ficstring +="\">"
        if showfandom:
            ficstring += fandom
            if thechars or language:
                ficstring += ", "
        if thechars:
            ficstring += thechars
            if language:
                ficstring += ", "
        if language:
            ficstring += language
        ficstring += "</a>"
        if rating == "g":
            ficstring += "&nbsp;<span style=\"background-color:#8ab60b;color:white; font-family:serif\">&nbsp;G&nbsp;</span>"
        elif rating == "t":
            ficstring += "&nbsp;<span style=\"background-color:#e8d405;color:white; font-family:serif\">&nbsp;T&nbsp;</span>"
        elif rating == "m":
            ficstring += "&nbsp;<span style=\"background-color:#eb7d10;color:white; font-family:serif\">&nbsp;M&nbsp;</span>"
        elif rating == "e":
            ficstring += "&nbsp;<span style=\"background-color:#9c0000;color:white; font-family:serif\">&nbsp;E&nbsp;</span>"
        for thegenre in genre:
            if thegenre == "gen":
                ficstring += "&nbsp;<span style=\"background-color:#8ab60b;color:white; font-family:serif\">&nbsp;☉&nbsp;</span>"
            elif thegenre == "slash":
                ficstring += "&nbsp;<span style=\"background-color:#1256b6;color:white; font-family:serif\">&nbsp;♂&nbsp;</span>"
            elif thegenre == "het":
                ficstring += "&nbsp;<span style=\"background-color:#670840;color:white; font-family:serif\">&nbsp;⚤&nbsp;</span>"
            elif thegenre == "femslash":
                ficstring += "&nbsp;<span style=\"background-color:#d50636;color:white; font-family:serif\">&nbsp;♀&nbsp;</span>"
            elif thegenre == "poly":
                ficstring += "&nbsp;<span><span style=\"background:linear-gradient(0deg, rgba(160,0,24,1) 0%, rgba(160,0,24,1) 49%, rgba(171,203,0,1) 50%, rgba(171,203,0,1) 100%);\">&nbsp;&nbsp;</span><span style=\"background: linear-gradient(0deg, rgba(0,51,148,1) 0%, rgba(0,51,148,1) 49%, rgba(129,0,108,1) 50%, rgba(129,0,108,1) 100%);\">&nbsp;&nbsp;</span></span>"
            elif thegenre == "other":
                ficstring += "&nbsp;<span style=\"background-color:black;color:white; font-family:serif\">&nbsp;☿&nbsp;</span>"
        if warnings:
            ficstring += "&nbsp;<span style=\"background-color:#eb7d10;color:white; font-family:serif\">&nbsp;!<small>?</small>&nbsp;</span>"
        ficstring += "&nbsp;<code>" + str(words) + "</code>"
        return ficstring

"""
Generate stats page for each year
"""

def yeargen(local=False):
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
    for year in yearlist:
        yearpath = "build/stats/" + str(year)
        if not os.path.isdir(yearpath):
            os.mkdir(yearpath)
        if os.path.exists(yearpath + "/index.html"):
            os.remove(yearpath + "/index.html")
        filewrite = open(yearpath + "/index.html", "a")
        filewrite.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title>Fic stats " + str(year) + "</title>\n<link rel=\"stylesheet\" href=\"")
        if local:
            filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/")
        else:
            filewrite.write("/fic/")
        filewrite.write("fic4.css\">\n<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Fugaz+One&family=Inconsolata&family=Lato:ital,wght@0,400;0,700;1,400;1,700&display=swap\">\n<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/charts.css/dist/charts.min.css\">\n</head>\n<body style=\"--colourone: #a70000; --colourtwo: #f5c1c1;\">\n<div id=\"site-wrapper\">\n<h1>Fic stats for " + str(year) + "</h1>\n")
        allfics = []
        ficdeets = []
        datesplit = []
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
                        if (date["date"]).year == year:
                            allfics.append(ficcountstring)
        allfics = sorted(list(dict.fromkeys(allfics)))
        for fic in allfics:
            if os.path.exists("originalsmeta/" + fic + ".py"):
                ficfile = "originalsmeta." + fic
                fileread = import_module(ficfile)
            elif os.path.exists("translationsmeta/" + fic + ".py"):
                ficfile = "translationsmeta." + fic
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
                    try:
                        fandom = fileread.fandom
                        event = fileread.event
                        eventname = fileread.eventname
                        try:
                            eventlocation = fileread.eventlocation
                        except:
                            eventlocation = False
                    except:
                        try:
                            if fileread.original:
                                theorig = "originalsmeta." + str(fileread.original)
                                origfile = import_module(theorig)
                                try:
                                    fandom = origfile.fandom
                                    event = origfile.event
                                    eventname = origfile.eventname
                                    try:
                                        eventlocation = fileread.eventlocation
                                    except:
                                        eventlocation = False
                                except:
                                    event = False
                                    eventname = False
                                    eventlocation = False
                        except:
                            event = False
                            eventname = False
                            eventlocation = False
                    ficwords = 0
                    for dateword in fileread.datewords:
                        if (dateword["date"]).year == year:
                            ficwords = (dateword["words"])
                        ficdict = {"number":fic,"words":ficwords,"fandom":fandom,"event":event,"eventname":eventname,"eventlocation":eventlocation,"date":dateword["date"]}
                        ficdeets.append(ficdict)
                        datesplit.append(ficdict)
        combinedeets = []
        for fic in ficdeets:
            if combinedeets == []:
                ficlogged = True
                combinedeets.append(fic)
            else:
                ficlogged = False
                for newfic in combinedeets:
                    if ficlogged == False:
                        if fic["number"] == newfic["number"]:
                            ficlogged = True
                            newfic["words"] += fic["words"]
                if ficlogged == False:
                    combinedeets.append(fic)
        ficdeets = combinedeets
        totalwords = 0
        for fic in ficdeets:
            totalwords += fic["words"]
        if len(allfics) == 1:
            filewrite.write("<p>Total: " + str(len (allfics)) + " fic, " + str(totalwords) + " words</p>\n")
        else:
            filewrite.write("<p>Total: " + str(len (allfics)) + " fics, " + str(totalwords) + " words</p>")
        prompts = []
        for fic in ficdeets:
            if fic["event"] == "prompt":
                prompts.append(fic)
        if prompts:
            promptwords = 0
            for fic in prompts:
                promptwords += fic["words"]
            promptdict = {"type":"Prompt fills","fics":len(prompts),"words":promptwords,"list":prompts}
        else:
            promptdict = False
        unprompted = []
        for fic in ficdeets:
            if fic["event"] == False:
                unprompted.append(fic)
        if unprompted:
            unpromptedwords = 0
            for fic in unprompted:
                unpromptedwords += fic["words"]
            unprompteddict = {"type":"Unprompted","fics":len(unprompted),"words":unpromptedwords,"list":unprompted}
        else:
            unprompteddict = False
        challenges = []
        for fic in ficdeets:
            if fic["event"] == "challenge":
                challenges.append(fic)
        if challenges:
            challengewords = 0
            for fic in challenges:
                challengewords += fic["words"]
            challengedict = {"type":"Challenges","fics":len(challenges),"words":challengewords,"list":challenges}
        else:
            challengedict = False
        exchanges = []
        for fic in ficdeets:
            if fic["event"] == "exchange" or fic["event"] == "ao3exchange":
                exchanges.append(fic)
        if exchanges:
            exchangewords = 0
            for fic in exchanges:
                exchangewords += fic["words"]
            exchangedict = {"type":"Exchanges","fics":len(exchanges),"words":exchangewords,"list":exchanges}
        else:
            exchangedict = False
        byevent = []
        if promptdict:
            byevent.append(promptdict)
        if unprompteddict:
            byevent.append(unprompteddict)
        if challengedict:
            byevent.append(challengedict)
        if exchangedict:
            byevent.append(exchangedict)
        byevent = sorted(byevent,key=lambda d: d["words"],reverse=True)
        filewrite.write("<h2>By type</h2>\n<table class=\"charts-css column hide-data show-labels show-primary-axis data-spacing-2\" style=\"height:200px;max-width:" + str(len(byevent) * 200) + "px;\">\n<caption>Words per fic type</caption>\n<thead>\n<tr>\n<th scope=\"col\">Type</th>\n<th scope=\"col\">Words</th>\n</tr>\n</thead>\n<tbody>\n")
        for event in byevent:
            filewrite.write("<tr>\n<th>" + event["type"] + "</th>\n<td style=\"--size:calc(" + str(event["words"]) + " / " + str((byevent[0])["words"]) + ");\"><span class=\"data\">" + str(event["words"]) + "</span><span class=\"tooltip\">" + str(event["fics"]) + " fic")
            if event["fics"] > 1:
                filewrite.write("s")
            filewrite.write(", " + str(event["words"]) + " words</span></td>\n</tr>\n")
        filewrite.write("</tbody>\n</table>\n<details><summary>Breakdown</summary>\n")
        for eventtype in byevent:
            filewrite.write("<h3>" + eventtype["type"] + "</h3>\n")
            eventslist = []
            for fic in eventtype["list"]:
                if fic["eventname"]:
                    eventdeets = {"eventname":fic["eventname"],"eventlocation":fic["eventlocation"],"ficno":fic["number"],"words":fic["words"]}
                else:
                    eventdeets = {"ficno":fic["number"],"words":fic["words"]}
                eventslist.append(eventdeets)
            neweventslist = []
            if eventtype["type"] == "Unprompted":
                neweventslist = eventslist
            else:
                for fic in eventslist:
                    if neweventslist == []:
                        ficlogged = True
                        neweventslist.append(fic)
                    else:
                        ficlogged = False
                        for newfic in neweventslist:
                            if ficlogged == False:
                                if fic["eventname"] == newfic["eventname"]:
                                    ficlogged = True
                                    newfic["words"] = newfic["words"] + fic["words"]
                                    if type(newfic["ficno"]) == str:
                                        newfic["ficno"] = newfic["ficno"].split()
                                    if type(fic["ficno"]) == str:
                                        newfic["ficno"].append(fic["ficno"])
                    if ficlogged == False:
                        neweventslist.append(fic)
            if eventtype["type"] != "Unprompted":
                for fic in neweventslist:
                    if type(fic["ficno"]) == str:
                        fic["ficno"] = fic["ficno"].split()
                neweventslist = sorted(neweventslist,key=lambda d: d["words"],reverse=True)
            else:
                neweventslist = sorted(neweventslist,key=lambda d: d["ficno"])
            if eventtype["type"] == "Unprompted":
                filewrite.write("<details><summary>List</summary>\n<ol>\n")
                for fic in neweventslist:
                    filewrite.write("<li>" + str(ficsum(int(fic["ficno"]),year,local=local)) + "</li>")
                filewrite.write("</ol>\n</details>\n")
            else:
                filewrite.write("<table class=\"charts-css column hide-data show-labels show-primary-axis data-spacing-2\" style=\"height:200px;max-width:" + str(len(neweventslist) * 200) + "px;\">\n<caption>Words per event</caption>\n<thead>\n<tr>\n<th scope=\"col\">Event</th>\n<th scope=\"col\">Words</th>\n</tr>\n</thead>\n<tbody>\n")
                for event in neweventslist:
                    filewrite.write("<tr>\n<th>")
                    if event["eventlocation"] == "dwcomm":
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + (event["eventname"]).replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/community.png\" alt=\"[community profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://" + (event["eventname"]).replace("_","-") + ".dreamwidth.org/\"><b>" + (event["eventname"]).replace("-","_") + "</b></a></span>")
                    elif event["eventlocation"] == "dwjournal":
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + (event["eventname"]).replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/user.png\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ (event["eventname"]).replace("_","-") + ".dreamwidth.org/\"><b>" + (event["eventname"]).replace("-","_")+ "</b></a></span>")
                    elif event["eventlocation"] == "ljjournal":
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + (event["eventname"]).replace("_","-") + ".livejournal.com/profile\"><img src=\"https://www.dreamwidth.org/img/external/lj-userinfo.gif\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ (event["eventname"]).replace("_","-") + ".livejournal.com/\"><b>" + (event["eventname"]).replace("-","_")+ "</b></a></span>")
                    else:
                        filewrite.write(event["eventname"])
                    filewrite.write("</th>\n<td style=\"--size:calc(" + str(event["words"]) + " / " + str((neweventslist[0])["words"]) + ");\"><span class=\"data\">" + str(event["words"]) + "</span><span class=\"tooltip\">" + str(len(event["ficno"])) + " fic")
                    if len(event["ficno"]) > 1:
                        filewrite.write("s")
                    filewrite.write(", " + str(event["words"]) + " words</span></td>\n</tr>\n")
                filewrite.write("</tbody>\n</table>\n<details><summary>List</summary>\n")
                for event in neweventslist:
                    filewrite.write("<h3>")
                    if event["eventlocation"] == "dwcomm":
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + (event["eventname"]).replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/community.png\" alt=\"[community profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://" + (event["eventname"]).replace("_","-") + ".dreamwidth.org/\"><b>" + (event["eventname"]).replace("-","_") + "</b></a></span>")
                    elif event["eventlocation"] == "dwjournal":
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + (event["eventname"]).replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/user.png\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ (event["eventname"]).replace("_","-") + ".dreamwidth.org/\"><b>" + (event["eventname"]).replace("-","_")+ "</b></a></span>")
                    elif event["eventlocation"] == "ljjournal":
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + (event["eventname"]).replace("_","-") + ".livejournal.com/profile\"><img src=\"https://www.dreamwidth.org/img/external/lj-userinfo.gif\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ (event["eventname"]).replace("_","-") + ".livejournal.com/\"><b>" + (event["eventname"]).replace("-","_")+ "</b></a></span>")
                    else:
                        filewrite.write(event["eventname"])
                    filewrite.write("</h3>\n<ol>\n")
                    for fic in event["ficno"]:
                        filewrite.write("<li>" + str(ficsum(int(fic),year,local=local)) + "</li>\n")
                    filewrite.write("</ol>\n")
                filewrite.write("</details>\n")
        fandomlist = []
        for fic in ficdeets:
            fandomlist.extend(fic["fandom"])
        fandomlist = sorted(list(dict.fromkeys(fandomlist)))
        filewrite.write("</details>\n<h2>By fandom</h2>\n<table class=\"charts-css column hide-data show-labels show-primary-axis data-spacing-2\" style=\"height:400px;max-width:" + str(len(fandomlist) * 200) + "px;\">\n<caption>Words per fandom</caption>\n<thead>\n<tr>\n<th scope=\"col\"> Fandom</th>\n<th scope=\"col\"> Words</th>\n</tr>\n</thead>\n<tbody>\n")
        fandomdeets = []
        for fandom in fandomlist:
            fandomdict = {"name":fandom,"ficno":[],"words":0}
            for fic in ficdeets:
                if fandom in fic["fandom"]:
                    fandomdict["ficno"].append(fic["number"])
                    fandomdict["words"] += fic["words"]    
            fandomdeets.append(fandomdict)
        fandomdeets = sorted(fandomdeets,key=lambda d: d["words"],reverse=True)
        for fandom in fandomdeets:
            filewrite.write("<tr>\n<th>" + fandom["name"] + "</th>\n<td style=\"--size:calc(" + str(fandom["words"]) + " / " + str((fandomdeets[0])["words"]) + ");\"><span class=\"data\">" + str(fandom["words"]) + "</span><span class=\"tooltip\">" + str(len(fandom["ficno"])) + " fic")
            if len(fandom["ficno"]) > 1:
                filewrite.write("s")
            filewrite.write(", " + str(fandom["words"]) + " words</span></td>\n</tr>")
        filewrite.write("</tbody>\n</table>\n<details><summary>List</summary>")
        for fandom in fandomdeets:
            filewrite.write("<h3>" + fandom["name"] + "</h3>\n<ol>\n")
            for fic in fandom["ficno"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,showfandom=False,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        filewrite.write("</details>\n<h2>By month</h2>\n<table class=\"charts-css column hide-data show-labels show-primary-axis data-spacing-2\" style=\"height:200px;max-width:2400px;\">\n<caption>Words per month</caption>\n<thead>\n<tr>\n<th scope=\"col\">Month</th>\n<th scope=\"col\">Words</th>\n</tr>\n</thead>\n<tbody>")
        monthcombine = []
        for fic in datesplit:
            # read the file back in to get the right word count, because dicts are dynamic somehow??
            thedate = fic["date"]
            thefic = fic["number"]
            if os.path.exists("originalsmeta/" + thefic + ".py"):
                ficfile = "originalsmeta." + thefic
                fileread = import_module(ficfile)
            elif os.path.exists("translationsmeta/" + thefic + ".py"):
                ficfile = "translationsmeta." + thefic
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
                    for datewords in fileread.datewords:
                        if datewords["date"] == thedate:
                            thewords = datewords["words"]
                            fic["words"] = thewords
                ficlogged = False
                if monthcombine == []:
                    if ficlogged == False:
                        ficlogged = True
                        monthcombine.append(fic)
                else:
                    ficlogged = False
                    for newfic in monthcombine:
                        if ficlogged == False:
                            if fic["number"] == newfic["number"]:
                                if (fic["date"]).month == (newfic["date"]).month:
                                    ficlogged = True
                                    newfic["words"] += fic["words"]
                    if ficlogged == False:
                        monthcombine.append(fic)
        jan = {"fics":[],"words":0}
        feb = {"fics":[],"words":0}
        mar = {"fics":[],"words":0}
        apr = {"fics":[],"words":0}
        may = {"fics":[],"words":0}
        jun = {"fics":[],"words":0}
        jul = {"fics":[],"words":0}
        aug = {"fics":[],"words":0}
        sep = {"fics":[],"words":0}
        octo = {"fics":[],"words":0}
        nov = {"fics":[],"words":0}
        dec = {"fics":[],"words":0}
        for fic in monthcombine:
            if (fic["date"]).month == 1:
                jan["fics"].append(fic["number"])
                jan["words"] += fic["words"]
            elif (fic["date"]).month == 2:
                feb["fics"].append(fic["number"])
                feb["words"] += fic["words"]
            elif (fic["date"]).month == 3:
                mar["fics"].append(fic["number"])
                mar["words"] += fic["words"]
            elif (fic["date"]).month == 4:
                apr["fics"].append(fic["number"])
                apr["words"] += fic["words"]
            elif (fic["date"]).month == 5:
                may["fics"].append(fic["number"])
                may["words"] += fic["words"]
            elif (fic["date"]).month == 6:
                jun["fics"].append(fic["number"])
                jun["words"] += fic["words"]
            elif (fic["date"]).month == 7:
                jul["fics"].append(fic["number"])
                jul["words"] += fic["words"]
            elif (fic["date"]).month == 8:
                aug["fics"].append(fic["number"])
                aug["words"] += fic["words"]
            elif (fic["date"]).month == 9:
                sep["fics"].append(fic["number"])
                sep["words"] += fic["words"]
            elif (fic["date"]).month == 10:
                octo["fics"].append(fic["number"])
                octo["words"] += fic["words"]
            elif (fic["date"]).month == 11:
                nov["fics"].append(fic["number"])
                nov["words"] += fic["words"]
            elif (fic["date"]).month == 12:
                dec["fics"].append(fic["number"])
                dec["words"] += fic["words"]
        wordlist = []
        wordlist.append(jan["words"])
        wordlist.append(feb["words"])
        wordlist.append(mar["words"])
        wordlist.append(apr["words"])
        wordlist.append(may["words"])
        wordlist.append(jun["words"])
        wordlist.append(jul["words"])
        wordlist.append(aug["words"])
        wordlist.append(sep["words"])
        wordlist.append(octo["words"])
        wordlist.append(nov["words"])
        wordlist.append(dec["words"])
        mostwords = max(wordlist)
        filewrite.write("<tr>\n<th>Jan</th>\n<td style=\"--size:calc(" + str(jan["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(jan["words"]) + "</span><span class=\"tooltip\">" + str(len(jan["fics"])) + " fic")
        if len(jan["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(jan["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Feb</th>\n<td style=\"--size:calc(" + str(feb["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(feb["words"]) + "</span><span class=\"tooltip\">" + str(len(feb["fics"])) + " fic")
        if len(feb["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(feb["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Mar</th>\n<td style=\"--size:calc(" + str(mar["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(mar["words"]) + "</span><span class=\"tooltip\">" + str(len(mar["fics"])) + " fic")
        if len(mar["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(mar["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Apr</th>\n<td style=\"--size:calc(" + str(apr["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(apr["words"]) + "</span><span class=\"tooltip\">" + str(len(apr["fics"])) + " fic")
        if len(apr["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(apr["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>May</th>\n<td style=\"--size:calc(" + str(may["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(may["words"]) + "</span><span class=\"tooltip\">" + str(len(may["fics"])) + " fic")
        if len(may["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(may["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Jun</th>\n<td style=\"--size:calc(" + str(jun["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(jun["words"]) + "</span><span class=\"tooltip\">" + str(len(jun["fics"])) + " fic")
        if len(jun["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(jun["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Jul</th>\n<td style=\"--size:calc(" + str(jul["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(jul["words"]) + "</span><span class=\"tooltip\">" + str(len(jul["fics"])) + " fic")
        if len(jul["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(jul["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Aug</th>\n<td style=\"--size:calc(" + str(aug["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(aug["words"]) + "</span><span class=\"tooltip\">" + str(len(aug["fics"])) + " fic")
        if len(aug["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(aug["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Sep</th>\n<td style=\"--size:calc(" + str(sep["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(sep["words"]) + "</span><span class=\"tooltip\">" + str(len(sep["fics"])) + " fic")
        if len(sep["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(sep["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Oct</th>\n<td style=\"--size:calc(" + str(octo["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(octo["words"]) + "</span><span class=\"tooltip\">" + str(len(octo["fics"])) + " fic")
        if len(octo["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(octo["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Nov</th>\n<td style=\"--size:calc(" + str(nov["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(nov["words"]) + "</span><span class=\"tooltip\">" + str(len(nov["fics"])) + " fic")
        if len(nov["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(nov["words"]) + " words</span></td>\n</tr>\n<tr>\n<th>Dec</th>\n<td style=\"--size:calc(" + str(dec["words"]) + " / " + str(mostwords) + ");\"><span class=\"data\">" + str(dec["words"]) + "</span><span class=\"tooltip\">" + str(len(dec["fics"])) + " fic")
        if len(dec["fics"]) != 1:
               filewrite.write("s")
        filewrite.write(", " + str(dec["words"]) + " words</span></td>\n</tr>\n</tbody>\n</table>\n<details><summary>List</summary>\n")
        if len(jan["fics"]) > 0:
            filewrite.write("<h3>January</h3>\n<ol>\n")
            for fic in jan["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,1,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(feb["fics"]) > 0:
            filewrite.write("<h3>February</h3>\n<ol>\n")
            for fic in feb["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,2,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(mar["fics"]) > 0:
            filewrite.write("<h3>March</h3>\n<ol>\n")
            for fic in mar["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,3,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(apr["fics"]) > 0:
            filewrite.write("<h3>April</h3>\n<ol>\n")
            for fic in apr["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,4,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(may["fics"]) > 0:
            filewrite.write("<h3>May</h3>\n<ol>\n")
            for fic in may["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,5,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(jun["fics"]) > 0:
            filewrite.write("<h3>June</h3>\n<ol>\n")
            for fic in jun["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,6,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(jul["fics"]) > 0:
            filewrite.write("<h3>July</h3>\n<ol>\n")
            for fic in jul["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,7,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(aug["fics"]) > 0:
            filewrite.write("<h3>August</h3>\n<ol>\n")
            for fic in aug["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,8,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(sep["fics"]) > 0:
            filewrite.write("<h3>September</h3>\n<ol>\n")
            for fic in sep["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,9,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(octo["fics"]) > 0:
            filewrite.write("<h3>October</h3>\n<ol>\n")
            for fic in octo["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,10,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(nov["fics"]) > 0:
            filewrite.write("<h3>November</h3>\n<ol>\n")
            for fic in nov["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,11,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        if len(dec["fics"]) > 0:
            filewrite.write("<h3>December</h3>\n<ol>\n")
            for fic in dec["fics"]:
                filewrite.write("<li>" + str(ficsum(int(fic),year,12,local=local)) + "</li>\n")
            filewrite.write("</ol>\n")
        filewrite.write("</details>\n<p>")
        listposition = yearlist.index(year)
        if year != 1998:
            prevyear = yearlist[listposition - 1]
            filewrite.write("<span style=\"float:left;\"><a href=\"")
            if local:
                filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/stats/" + str(prevyear) + "/index.html")
            else:
                filewrite.write("/fic/stats/" + str(prevyear))
            filewrite.write("\">« " + str(prevyear) + "</a></span>")
        thisyear = int(datetime.datetime.now().strftime("%Y"))
        if year < thisyear:
            nextyear = yearlist[listposition + 1]
            filewrite.write("<span style=\"float:right;\"><a href=\"")
            if local:
                filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/stats/" + str(nextyear) + "/index.html")
            else:
                filewrite.write("/fic/stats/" + str(nextyear))
            filewrite.write("\">" + str(nextyear) + " »</a></span>")
        filewrite.write("</p>\n</div>\n</body>\n</html>")
        filewrite.close()        

if __name__ == "__main__":
    yeargen(True)
