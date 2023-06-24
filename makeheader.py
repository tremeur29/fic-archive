import datetime
from importlib import import_module
from dateutil.relativedelta import relativedelta

"""
Remove test file
"""

fffandoms = ["FF1","FF2","FF3","FF4","FF5","FF6","FF7","FF8","FF9","FFX","FF11","FF12","FF13","FF14","FF15","FF16"]    

"""
Code to generate the fic header div
"""

def ficgen(ficno,unique=False,output="output.html",local=False):
    # convert to three-digit number
    if ficno < 10:
        ficnostring = "00" + str(ficno)
    elif ficno < 100:
        ficnostring = "0" + str(ficno)
    else:
        ficnostring = str(ficno)
    # open the file
    ficfile = "originalsmeta." + ficnostring
    fileread = import_module(ficfile)
    # open translation file if there is one
    try:
        if fileread.translation:
            if fileread.translation < 10:
                translationstring = "00" + str(fileread.translation)
            elif fileread.translation < 100:
                translationstring = "0" + str(fileread.translation)
            else:
                translationstring = str(fileread.translation)
            translationfile = "translationsmeta." + translationstring
            transread = import_module(translationfile)
    except:
        pass
    try:
        if fileread.revealdate > datetime.datetime.now():
            revealed = False
        else:
            revealed = True
    except:
        revealed = True
    if revealed == True:
        # write to output file
        filewrite = open(output, "a")
        filewrite.write("<div class=\"fic\"")
        # give the div an id if requested
        if unique:
            filewrite.write(" id=\"fic" + ficnostring + "\"")
        filewrite.write(">\n<h1><span class=\"ficno\">" + ficnostring)
        # write ficno including translation if there is one
        try:
            filewrite.write("/" + translationstring)
        except:
            pass
        filewrite.write("</span>")
        # write title if requested
        if fileread.showtitle:
            filewrite.write(" <span class=\"fictitle\">" + fileread.title)
            try:
                if transread.showtitle:
                    filewrite.write("/" + transread.title)
            except:
                pass
            filewrite.write("</span>")
        else:
            try:
                if transread.showtitle:
                    filewrite.write(" <span class=\"fictitle\">" + transread.title)
            except:
                pass
        if fileread.status == "abandoned":
            filewrite.write(" <span class=\"abandoned\"></span>")
        filewrite.write("</h1>\n<ul class=\"ficmeta\">\n<li class=\"ficdate\">")
        # write date, date range if ranged or translation
        if fileread.status == "incomplete":
            filewrite.write((fileread.datewords[0])["date"].strftime("%-d %B %Y") + "–")
        else:
            try:
                if transread.status == "incomplete":
                    filewrite.write((fileread.datewords[0])["date"].strftime("%-d %B %Y") + "–")
                else:
                    if fileread.translation:
                        if (transread.datewords[-1])["date"].year == (fileread.datewords[0])["date"].year:
                            if (transread.datewords[-1])["date"].month == (fileread.datewords[0])["date"].month:
                                if (transread.datewords[-1])["date"].date == (fileread.datewords[0])["date"].date:
                                    filewrite.write((fileread.datewords[0])["date"].strftime("%-d %B %Y"))
                                else:
                                    filewrite.write((fileread.datewords[0])["date"].strftime("%-d") + "–" + (transread.datewords[-1])["date"].strftime("%-d %B %Y"))
                            else:
                                filewrite.write((fileread.datewords[0])["date"].strftime("%-d %B") + "–" + (transread.datewords[-1])["date"].strftime("%-d %B %Y"))
                        else:
                            filewrite.write((fileread.datewords[0])["date"].strftime("%-d %B %Y") + "–" + (transread.datewords[-1])["date"].strftime("%-d %B %Y"))
            except:
                try:
                    filewrite.write(fileread.approxdate)
                except:
                    if (fileread.datewords[0])["date"].year == (fileread.datewords[-1])["date"].year:
                        if (fileread.datewords[0])["date"].month == (fileread.datewords[-1])["date"].month:
                            if (fileread.datewords[0])["date"] == (fileread.datewords[-1])["date"]:
                                filewrite.write((fileread.datewords[-1])["date"].strftime("%-d %B %Y"))
                            else:
                                filewrite.write((fileread.datewords[0])["date"].strftime("%-d") + "–" + (fileread.datewords[-1])["date"].strftime("%-d %B %Y"))
                        else:
                            filewrite.write((fileread.datewords[0])["date"].strftime("%-d %B") + "–" + (fileread.datewords[-1])["date"].strftime("%-d %B %Y"))
                    else:
                        filewrite.write((fileread.datewords[0])["date"].strftime("%-d %B %Y") + "–" + (fileread.datewords[-1])["date"].strftime("%-d %B %Y"))
        # write wordcount
        sumwords = 0
        for instalment in fileread.datewords:
            sumwords = sumwords + instalment["words"]
        filewrite.write("</li>\n<li class=\"wordcount\">" + str(sumwords))
        transwords = 0
        try:
            for instalment in transread.datewords:
                transwords = transwords + instalment["words"]
            filewrite.write(" + " + str(transwords))
        except:
            pass
        # write rating
        filewrite.write("</li>\n<li class=\"rating\"><span class=\"" + fileread.rating + "\">")
        # write reason for rating if there is one
        try:
            filewrite.write(" (" + fileread.ratingreason + ")")
        except:
            pass
        filewrite.write("</span></li>\n<li class=\"fandom\">")
        # write fandom
        try:
            filewrite.write(fileread.fandomtext)
        except:
            filewrite.write("/".join(fileread.fandom))
        filewrite.write("</li>\n")
        # write characters in pov, main, secondary categories, if they exist
        try:
            filewrite.write("<li class=\"characters\">" + fileread.charactertext + "</li>\n")
        except:
            try:
                filewrite.write("<li class=\"characters\">" + ", ".join(fileread.charpov))
                try:
                    filewrite.write(", " + ", ".join(fileread.charmain))
                except:
                    pass
                try:
                    filewrite.write(", " + "<small>" + ", ".join(fileread.charsecondary) + "</small>")
                except:
                    pass
                filewrite.write("</li>\n")
            except:
                try:
                    filewrite.write("<li class=\"characters\">" + ", ".join(fileread.charmain))
                    try:
                        filewrite.write(", " + "<small>" + ", ".join(fileread.charsecondary) + "</small>")
                    except:
                        pass
                    filewrite.write("</li>\n")
                except:
                    try:
                        filewrite.write("<li class=\"characters\">" + ", ".join(fileread.charsecondary) + "</li>\n")
                    except:
                        pass
        # write genre
        filewrite.write("<li class=\"genre\">" + ", ".join(fileread.genre) + "</li>\n")
        # write warnings if they exist
        try:
            filewrite.write("<li class=\"warnings\">" + fileread.warnings + "</li>\n")
        except:
            pass
        # write point in canon if there is one
        try:
            filewrite.write("<li class=\"time\">" + fileread.time + "</li>\n")
        except:
            pass
        # write locations if there are any
        try:
            filewrite.write("<li class=\"location\">" + fileread.locationtext + "</li>\n")
        except:
            try:
                filewrite.write("<li class=\"location\">" + ", ".join(fileread.location) + "</li>\n")
            except:
                pass
        filewrite.write("</ul>\n")
        # write summary if there is one
        try:
            if transread.language == "en":
                try:
                    filewrite.write("<p class=\"summary\">" + transread.summary)
                    try:
                        filewrite.write(" " + fileread.summary + "</p>\n")
                    except:
                        filewrite.write("</p>\n")
                except:
                    try:
                        filewrite.write("<p class=\"summary\">" + fileread.summary + "</p>\n")
                    except:
                        pass
            elif transread.language == "fr":
                try:
                    filewrite.write("<p class=\"summary\">" + fileread.summary)
                    try:
                        filewrite.write(" " + transread.summary + "</p>\n")
                    except:
                        filewrite.write("</p>\n")
                except:
                    try:
                        filewrite.write("<p class=\"summary\">" + transread.summary + "</p>\n")
                    except:
                        pass
        except:
            try:
                filewrite.write("<p class=\"summary\">" + fileread.summary + "</p>\n")
            except:
                pass
        # set up notes paragraph if required
        if (fileread.datewords[0])["date"].year < 2011:
            juvenilia = True
        else:
            juvenilia = False
        try:
            if fileread.notes:
                filewrite.write("<p class=\"note\">")
        except:
            try:
                if fileread.event:
                    filewrite.write("<p class=\"note\">")
            except:
                if juvenilia:
                    filewrite.write("<p class=\"note\">")
        # if juvenilia, add age
        if juvenilia:
            age = relativedelta((fileread.datewords[0])["date"], datetime.datetime(1993,6,28)).years
            filewrite.write("Age at time of writing: " + str(age) + ".")
            try:
                if fileread.notes:
                    filewrite.write(" ")
            except:
                pass
        # write event details if there are any
        try:
            if fileread.eventname == "fail-fandomanon":
                filewrite.write("In response to prompt at <span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://fail-fandomanon.dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/community.png\" alt=\"[community profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://fail-fandomanon.dreamwidth.org/\"><b>fail_fandomanon</b></a></span>: <i>" + fileread.prompt + "</i>.")
                try:
                    if fileread.notes:
                        filewrite.write(" ")
                except:
                    pass
            elif fileread.eventname == "robotsoup":
                filewrite.write("Written for <span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://kalloway.dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/user.png\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://kalloway.dreamwidth.org/\"><b>kalloway</b></a></span>’s " + fileread.eventdeets + " fest.")
                try:
                    if fileread.notes:
                        filewrite.write(" ")
                except:
                    pass
            else:
                filewrite.write("Written for ")
                try:
                    if fileread.eventlocation == "dwcomm":
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + fileread.eventname.replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/community.png\" alt=\"[community profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://" + fileread.eventname.replace("_","-") + ".dreamwidth.org/\"><b>" + fileread.eventname.replace("-","_") + "</b></a></span>")
                    elif fileread.eventlocation == "dwjournal":
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + fileread.eventname.replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/user.png\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ fileread.eventname.replace("_","-") + ".dreamwidth.org/\"><b>" + fileread.eventname.replace("-","_")+ "</b></a></span>")
                    elif fileread.eventlocation == "ljjournal":
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + fileread.eventname.replace("_","-") + ".livejournal.com/profile\"><img src=\"https://www.dreamwidth.org/img/external/lj-userinfo.gif\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ fileread.eventname.replace("_","-") + ".livejournal.com/\"><b>" + fileread.eventname.replace("-","_")+ "</b></a></span>")
                except:
                    if fileread.eventname == "Semaine de la fic française":
                        filewrite.write("<i>Semaine de la fic française</i>")
                    else:
                        filewrite.write(fileread.eventname)
                try:
                    if fileread.eventfrequency == "annual":
                        filewrite.write(" " + str((fileread.datewords[0])["date"].year))
                    else:
                        filewrite.write(" " + fileread.eventfrequency)
                except:
                    pass
                if fileread.event == "prompt":
                    filewrite.write(", in response to ")
                    try:
                        if fileread.recip:
                            try:
                                if fileread.recipsite == "dw":
                                    filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + fileread.recip.replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/user.png\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ fileread.recip.replace("_","-") + ".dreamwidth.org/\"><b>" + fileread.recip.replace("-","_") + "</b></a></span>")
                                elif fileread.recipsite == "ao3":
                                    try:
                                        if fileread.recippseud:
                                            filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://archiveofourown.org/users/" + fileread.recip + "/profile\"><img src=\"https://p.dreamwidth.org/b164c54b26e4/-/archiveofourown.org/favicon.ico\" alt=\"[archiveofourown.org profile]\" width=\"16\" height=\"16\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://archiveofourown.org/users/"+ fileread.recip + "/pseuds/" + fileread.recippseud.replace(" ","%20") + "\"><b>" + fileread.recippseud + " (" + fileread.recip + ")</b></a></span>")
                                    except:
                                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://archiveofourown.org/users/" + fileread.recip + "/profile\"><img src=\"https://p.dreamwidth.org/b164c54b26e4/-/archiveofourown.org/favicon.ico\" alt=\"[archiveofourown.org profile]\" width=\"16\" height=\"16\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://archiveofourown.org/users/"+ fileread.recip + "\"><b>" + fileread.recip + "</b></a></span>")
                                elif fileread.recipsite == "tumblr":
                                    filewrite.write("<span style=\"white-space: nowrap;\"><a href=\"https://" + fileread.recip + ".tumblr.com\"><img src=\"https://www.tumblr.com/favicon.ico\" alt=\"[tumblr.com profile]\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" width=\"16\" height=\"16\"></a><a href=\"https://" + fileread.recip + ".tumblr.com\"><b>" + fileread.recip + "</b></a></span>")
                            except:
                                filewrite.write(fileread.recip)
                            filewrite.write("’s ")
                    except:
                        pass
                    filewrite.write("prompt, <i>" + fileread.prompt + "</i>.")
                    try:
                        if fileread.notes:
                            filewrite.write(" ")
                    except:
                        pass
                elif fileread.event == "exchange" or fileread.event == "ao3exchange":
                    filewrite.write(", a gift for ")
                    try:
                        if fileread.recipsite == "dw":
                            filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + fileread.recip.replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/user.png\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://"+ fileread.recip.replace("_","-") + ".dreamwidth.org/\"><b>" + fileread.recip.replace("-","_") + "</b></a></span>")
                        elif fileread.recipsite == "ao3":
                            try:
                                if fileread.recippseud:
                                    filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://archiveofourown.org/users/" + fileread.recip + "/profile\"><img src=\"https://p.dreamwidth.org/b164c54b26e4/-/archiveofourown.org/favicon.ico\" alt=\"[archiveofourown.org profile]\" width=\"16\" height=\"16\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://archiveofourown.org/users/"+ fileread.recip + "/pseuds/" + fileread.recippseud.replace(" ","%20") + "\"><b>" + fileread.recippseud + " (" + fileread.recip + ")</b></a></span>")
                            except:
                                filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://archiveofourown.org/users/" + fileread.recip + "/profile\"><img src=\"https://p.dreamwidth.org/b164c54b26e4/-/archiveofourown.org/favicon.ico\" alt=\"[archiveofourown.org profile]\" width=\"16\" height=\"16\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\"></a><a href=\"https://archiveofourown.org/users/" + fileread.recip + "\"><b>" + fileread.recip + "</b></a></span>")
                        elif fileread.recipsite == "tumblr":
                            filewrite.write("<span style=\"white-space: nowrap;\"><a href=\"https://" + fileread.recip + ".tumblr.com\"><img src=\"https://www.tumblr.com/favicon.ico\" alt=\"[tumblr.com profile]\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" width=\"16\" height=\"16\"></a><a href=\"https://" + fileread.recip + ".tumblr.com\"><b>" + fileread.recip + "</b></a></span>")
                    except:
                        filewrite.write(fileread.recip)
                    filewrite.write(".")
                    try:
                        if fileread.notes:
                            filewrite.write(" ")
                    except:
                        pass
                else:
                    filewrite.write(".")
                    try:
                        if fileread.notes:
                            filewrite.write(" ")
                    except:
                        pass
        except:
            pass
        # write notes if there are any
        try:
            filewrite.write(fileread.notes + "</p>\n")
        except:
            try:
                if fileread.event:
                    filewrite.write("</p>\n")
            except:
                if juvenilia:
                    filewrite.write("</p>\n")
        filewrite.write("<ul class=\"ficlinks")
        # specify language if necessary
        try:
            if fileread.translation:
                if fileread.language == "en":
                    filewrite.write(" english")
                elif fileread.language == "fr":
                    filewrite.write (" french")
        except:
            pass
        filewrite.write("\">\n")
        # write html link if there is one
        if fileread.html:
            filewrite.write("<li class=\"prazelink\"><a ")
            if fileread.locked:
                filewrite.write("class=\"locked\" href=\"")
                if local:
                    filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/secret/")
                else:
                    filewrite.write("/fic/secret/")
            else:
                if local:
                    filewrite.write("href=\"/home/mdd/Documents/drive/proj/fic-archive/build/files/")
                else:
                    filewrite.write("href=\"/fic/files/")
            filewrite.write(ficnostring + ".html\">HTML</a></li>\n")
        # write pdf link if there is one
        if fileread.pdf:
            filewrite.write("<li class=\"prazelink\"><a ")
            if fileread.locked:
                filewrite.write("class=\"locked\" href=\"")
                if local:
                    filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/secret/")
                else:
                    filewrite.write("/fic/secret/")
            else:
                if local:
                    filewrite.write("href=\"/home/mdd/Documents/drive/proj/fic-archive/build/files/")
                else:
                    filewrite.write("href=\"/fic/files/")
            filewrite.write(ficnostring + ".pdf\">PDF</a></li>\n")
        # write epub link if there is one
        if fileread.epub:
            filewrite.write("<li class=\"prazelink\"><a ")
            if fileread.locked:
                filewrite.write("class=\"locked\" href=\"")
                if local:
                    filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/secret/")
                else:
                    filewrite.write("/fic/secret/")
            else:
                if local:
                    filewrite.write("href=\"/home/mdd/Documents/drive/proj/fic-archive/build/files/")
                else:
                    filewrite.write("href=\"/fic/files/")
            filewrite.write(ficnostring + ".epub\">EPUB</a></li>\n")
        # write ao3 link if there is one
        try:
            if fileread.ao3slug:
                filewrite.write("<li class=\"ao3link\"><a ")
                if fileread.locked:
                    filewrite.write("class=\"locked\" ")
                filewrite.write("href=\"https://archiveofourown.org/works/" + str(fileread.ao3slug) + "\">AO3</a></li>\n")
        except:
            pass
        # determine if comments page
        if any(item in fffandoms for item in fileread.fandom):
            filewrite.write("<li class=\"prazelink\"><a href=\"")
            if local:
                filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/comments/" + ficnostring + "/index.html")
            else:
                filewrite.write("/fic/comments/" + ficnostring)
            filewrite.write("\">comments</a></li>\n")
        else:
            timeelapsed = datetime.datetime.now() - (fileread.datewords[-1])["date"]
            if timeelapsed.days < 730:
                filewrite.write("<li class=\"prazelink\"><a href=\"")
                if local:
                    filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/comments/" + ficnostring + "/index.html")
                else:
                    filewrite.write("/fic/comments/" + ficnostring)
                filewrite.write("\">comments</a></li>\n")
            else:
                try:
                    if fileread.event == "ao3exchange" and (fileread.datewords[0])["date"].year > 2019:
                        filewrite.write("<li class=\"prazelink\"><a href=\"")
                        if local:
                            filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/comments/" + ficnostring + "/index.html")
                        else:
                            filewrite.write("/fic/comments/" + ficnostring)
                        filewrite.write("\">comments</a></li>\n")
                    else:
                        try:
                            if fileread.comments:
                                filewrite.write("<li class=\"prazelink\"><a href=\"")
                                if local:
                                    filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/comments/" + ficnostring + "/index.html")
                                else:
                                    filewrite.write("/fic/comments/" + ficnostring)
                                filewrite.write("\">comments</a></li>\n")
                        except:
                            pass
                except:
                    try:
                        if fileread.comments:
                            filewrite.write("<li class=\"prazelink\"><a href=\"")
                            if local:
                                filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/comments/" + ficnostring + "/index.html")
                            else:
                                filewrite.write("/fic/comments/" + ficnostring)
                            filewrite.write("\">comments</a></li>\n")
                    except:
                        pass
        filewrite.write("</ul>\n")
        # write links for translation if required
        try:
            if fileread.translation:
                if transread.language == "en":
                    filewrite.write("<ul class=\"ficlinks english")
                elif transread.language == "fr":
                    filewrite.write("<ul class=\"ficlinks french")
                filewrite.write("\">\n")
                # write html link if there is one
                if fileread.html:
                    filewrite.write("<li class=\"prazelink\"><a ")
                    if fileread.locked:
                        filewrite.write("class=\"locked\" href=\"")
                        if local:
                            filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/secret/")
                        else:
                            filewrite.write("/fic/secret/")
                    else:
                        if local:
                            filewrite.write("href=\"/home/mdd/Documents/drive/proj/fic-archive/build/files/")
                        else:
                            filewrite.write("href=\"/fic/files/")
                    filewrite.write(translationstring + ".html\">HTML</a></li>\n")
                # write pdf link if there is one
                if fileread.pdf:
                    filewrite.write("<li class=\"prazelink\"><a ")
                    if fileread.locked:
                        filewrite.write("class=\"locked\" href=\"")
                        if local:
                            filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/secret/")
                        else:
                            filewrite.write("/fic/secret/")
                    else:
                        if local:
                            filewrite.write("href=\"/home/mdd/Documents/drive/proj/fic-archive/build/files/")
                        else:
                            filewrite.write("href=\"/fic/files/")
                    filewrite.write(translationstring + ".pdf\">PDF</a></li>\n")
                # write epub link if there is one
                if fileread.epub:
                    filewrite.write("<li class=\"prazelink\"><a ")
                    if fileread.locked:
                        filewrite.write("class=\"locked\" href=\"")
                        if local:
                            filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/secret/")
                        else:
                            filewrite.write("/fic/secret/")
                    else:
                        if local:
                            filewrite.write("href=\"/home/mdd/Documents/drive/proj/fic-archive/build/files/")
                        else:
                            filewrite.write("href=\"/fic/files/")
                    filewrite.write(translationstring + ".epub\">EPUB</a></li>\n")
                # write ao3 link if there is one
                try:
                    if fileread.ao3slug:
                        filewrite.write("<li class=\"ao3link\"><a ")
                        if fileread.locked:
                            filewrite.write("class=\"locked\" ")
                        filewrite.write("href=\"https://archiveofourown.org/works/" + str(transread.ao3slug) + "\">AO3</a></li>\n")
                except:
                    pass
                # determine if comments page required
                if any(item in fffandoms for item in fileread.fandom):
                    filewrite.write("<li class=\"prazelink\"><a href=\"")
                    if local:
                        filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/comments/" + translationstring + "/index.html")
                    else:
                        filewrite.write("/fic/comments/" + translationstring)
                    filewrite.write("\">comments</a></li>\n")
                else:
                    timeelapsed = datetime.datetime.now() - (transread.datewords[-1])["date"]
                    if timeelapsed.days < 730:
                        filewrite.write("<li class=\"prazelink\"><a href=\"")
                        if local:
                            filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/comments/" + translationstring + "/index.html")
                        else:
                            filewrite.write("/fic/comments/" + translationstring)
                        filewrite.write("\">comments</a></li>\n")
                    else:
                        try:
                            if transread.comments:
                                filewrite.write("<li class=\"prazelink\"><a href=\"")
                                if local:
                                    filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/comments/" + translationstring + "/index.html")
                                else:
                                    filewrite.write("/fic/comments/" + translationstring)
                                filewrite.write("\">comments</a></li>\n")
                        except:
                            pass
                    filewrite.write("</ul>\n")
        except:
            pass
        filewrite.write("</div>\n")
        filewrite.close()
