import datetime, os
from importlib import import_module

import makeheader
import headerfooter

def eventlist(local=False):
    # delete existing file
    if os.path.exists("build/events/index.html"):
        os.remove("build/events/index.html")
    # write header
    headerfooter.headerwrite("build/events/index.html","Events","Events","<p>Here’s a list of the fics I’ve written for events (exchanges, prompt memes/fests, challenges, etc.). Fics in this section are organised chronologically by year, <b>from oldest to newest</b>.</p>",False,local)
    # get list of events
    events = []
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
                try:
                    events.append({"name":fileread.eventname,"location":fileread.eventlocation,"sortname":fileread.eventname.lower()})
                except:
                    try:
                        events.append({"name":fileread.eventname,"location":"","sortname":fileread.eventname.lower()})
                    except:
                        pass
    newlist = []
    for event in events:
        if event not in newlist:
            newlist.append(event)
    eventlist = sorted(newlist, key=lambda d: d["sortname"])
    for event in eventlist:
        evententries = []
        theevent = event["name"]
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
                    try:
                        if fileread.eventname == theevent:
                            evententries.append({"ficno":ficcount,"year":(fileread.datewords[0])["date"].year,"fandom":fileread.fandom})
                    except:
                        pass
        eventfandoms = []
        for entry in evententries:
            eventfandoms.extend(entry["fandom"])
        eventfandoms = sorted(list(dict.fromkeys(eventfandoms)))
         # write details element
        output = "build/events/index.html"
        filewrite = open(output, "a")
        filewrite.write("<details><summary><b>")
        position = 0
        while (eventlist[position])["name"] != theevent:
            position += 1
        eventlocation = (eventlist[position])["location"]
        if eventlocation == "dwjournal":
            filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + theevent.replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/user.png\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ theevent.replace("_","-") + ".dreamwidth.org/\"><b>" + theevent.replace("-","_")+ "</b></a></span>")
        elif eventlocation == "dwcomm":
            filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + theevent.replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/community.png\" alt=\"[community profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://" + theevent.replace("_","-") + ".dreamwidth.org/\"><b>" + theevent.replace("-","_") + "</b></a></span>")
        elif eventlocation == "ljjournal":
            filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + theevent.replace("_","-") + ".livejournal.com/profile\"><img src=\"https://www.dreamwidth.org/img/external/lj-userinfo.gif\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ theevent.replace("_","-") + ".livejournal.com/\"><b>" + theevent.replace("-","_")+ "</b></a></span>")
        else:
            filewrite.write(theevent)
        filewrite.write("</b> (" + str(len(evententries)) + ": " + ", ".join(eventfandoms) + ")</summary>\n")
        filewrite.close()
        startyear = 2014
        thisyear = int(datetime.datetime.now().strftime("%Y"))
        while startyear < thisyear:
            startyear += 1
            yearlist = []
            for entry in evententries:
                if int(entry["year"]) == startyear:
                    yearlist.append(entry["ficno"])
            if len(yearlist) > 0:
                yearlist = sorted(yearlist)
                filewrite = open(output, "a")
                filewrite.write("<h1>" + str(startyear) + "</h1>\n")
                filewrite.close()
                for fic in yearlist:
                    makeheader.ficgen(fic,False,output,local)
        filewrite = open(output, "a")
        filewrite.write("</details>\n")
        filewrite.close()
    # write footer
    headerfooter.footerwrite("build/events/index.html",False,local)

if __name__ == "__main__":
    eventlist()
