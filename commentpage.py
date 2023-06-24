import datetime, os, shutil
from importlib import import_module

import headerfooter

fffandoms = ["FF1","FF2","FF3","FF4","FF5","FF6","FF7","FF8","FF9","FFX","FF11","FF12","FF13","FF14","FF15","FF16"]

"""
Code to generate comment page
"""

def commentpage(ficno,directory,local=False):
    # convert to three-digit number
    if ficno < 10:
        ficnostring = "00" + str(ficno)
    elif ficno < 100:
        ficnostring = "0" + str(ficno)
    else:
        ficnostring = str(ficno)
    # open the file
    ficfile = directory + "." + ficnostring
    fileread = import_module(ficfile)
    # determine if comments page
    try:
        if any(item in fffandoms for item in fileread.fandom):
            fffandom = True
        else:
            fffandom = False
    except:
        origfile = "originalsmeta." + str(fileread.original)
        origread = import_module(origfile)
        if any(item in fffandoms for item in origread.fandom):
            fffandom = True
        else:
            fffandom = False
    if fffandom:
        commentspage = True
    else:
        timeelapsed = datetime.datetime.now() - (fileread.datewords[-1])["date"]
        if timeelapsed.days < 730:
            commentspage = True
        else:
            try:
                if fileread.event == "ao3exchange" and (fileread.datewords[0])["date"].year > 2019:
                    commentspage = True
                else:
                    try:
                        if fileread.comments:
                            commentspage = True
                    except:
                        commentspage = False
            except:
                try:
                    if fileread.comments:
                        commentspage = True
                except:
                    commentspage = False
    if commentspage:
        commentspath = "build/comments/" + ficnostring
        if not os.path.isdir(commentspath):
            os.mkdir(commentspath)
        if os.path.exists(commentspath + "/index.html"):
            os.remove(commentspath + "/index.html")
        # write to output file
        headerfooter.headerwrite(commentspath + "/index.html","Comments for fic no. " + ficnostring,"Comments for fic no. <span id=\"ficno\">" + ficnostring + "</span>","",False,local)
        filewrite = open(commentspath + "/index.html", "a")
        if fffandom or timeelapsed.days < 730:
            filewrite.write("<h2>Leave a comment</h2>\n<noscript>\n<p><b>JavaScript is unavailable.</b> Please <a href=\"mailto:eheu48@gmail.com\">email me</a> any comments.</p>\n</noscript>\n<p class=\"jsonly\">Comments will be posted manually; please expect a delay between submitting your comment and seeing it below!</p>\n<form id=\"theform\" onsubmit=\"sendContact(event)\" class=\"jsonly\">\n<input type=\"text\" id=\"nameInput\" required placeholder=\"Pseudonym (required)\">\n<input type=\"email\" id=\"emailInput\" placeholder=\"Email (if you want email notification of reply)\">\n<input type=\"text\" id=\"siteInput\" placeholder=\"Site (if you want a link back)\">\n<textarea id=\"messageInput\" rows=\"5\" required placeholder=\"Your comment (required, include whatever markup [or down] you like)\"></textarea>\n<button type=\"submit\">Submit</button>\n</form>\n")
        else:
            try:
                if fileread.event == "ao3exchange" and (fileread.datewords[0])["date"].year > 2019:
                    filewrite.write("<p>Comments aren’t open for this fic. They’re still available <a href=\"https://archiveofourown.org/works/" + str(fileread.ao3slug) + "\">on AO3</a>, however, as this was written for an AO3-based gift exchange.</p>\n")
            except:
                pass
        try:
            if fileread.comments:
                filewrite.write("<h2>Archived comments</h2>\n<p>If you left one of these comments and would like it to be removed from the archive, please <a href=\"mailto:eheu48@gmail.com\">email me</a>.</p>\n<p><small>My replies are included only if they were originally posted on this site.</small></p>\n")
            for comment in fileread.comments:
                filewrite.write("<div class=\"comment\">\n<h1>")
                if comment["site"] == "dw":
                    if comment["registered"]:
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + comment["username"].replace("_","-") + ".dreamwidth.org/profile\"><img src=\"https://www.dreamwidth.org/img/silk/identity/user.png\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" /></a><a href=\"https://"+ comment["username"].replace("_","-") + ".dreamwidth.org/\"><b>" + comment["username"].replace("-","_")+ "</b></a></span>")
                    else:
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><img src=\"https://www.dreamwidth.org/img/silk/identity/user.png\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" /><b>anonymous</b></a></span>")
                elif comment["site"] == "lj":
                    if comment["registered"]:
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://" + comment["username"].replace("_","-") + ".livejournal.com/profile\"><img src=\"https://www.dreamwidth.org/img/external/lj-userinfo.gif\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" /></a><a href=\"https://"+ comment["username"].replace("_","-") + ".livejournal.com/\"><b>" + comment["username"].replace("-","_")+ "</b></a></span>")
                    else:
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><img src=\"https://www.dreamwidth.org/img/external/lj-userinfo.gif\" alt=\"[personal profile]\" width=\"17\" height=\"17\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" /><b>anonymous</b></a></span>")
                elif comment["site"] == "ao3":
                    if comment["registered"]:
                        try:
                            filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://archiveofourown.org/users/" + comment["username"] + "/profile\"><img src=\"https://p.dreamwidth.org/b164c54b26e4/-/archiveofourown.org/favicon.ico\" alt=\"[archiveofourown.org profile]\" width=\"16\" height=\"16\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" /></a><a href=\"https://archiveofourown.org/users/"+ comment["username"] + "/pseuds/" + comment["pseud"].replace(" ","%20") + "\"><b>" + comment["pseud"] + " (" + comment["username"] + ")</b></a></span>")
                        except:
                            filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><a href=\"https://archiveofourown.org/users/" + comment["username"] + "/profile\"><img src=\"https://p.dreamwidth.org/b164c54b26e4/-/archiveofourown.org/favicon.ico\" alt=\"[archiveofourown.org profile]\" width=\"16\" height=\"16\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" /></a><a href=\"https://archiveofourown.org/users/"+ comment["username"] + "\"><b>" + comment["username"] + "</b></a></span>")
                    else:
                        filewrite.write("<span style=\"white-space: nowrap;\" class=\"ljuser\"><img src=\"https://p.dreamwidth.org/b164c54b26e4/-/archiveofourown.org/favicon.ico\" alt=\"[archiveofourown.org profile]\" width=\"16\" height=\"16\" style=\"vertical-align: text-bottom; border: 0; padding-right: 1px;\" /><b>" + comment["username"] + "</b></span>")
                elif comment["site"] == "praze":
                    try:
                        filewrite.write("<a href=\"" + comment["url"] + "\">" + comment["username"] + "</a>")
                    except:
                        filewrite.write(comment["username"])
                try:
                    filewrite.write(" on chapter " + str(comment["chapter"]))
                except:
                    pass
                filewrite.write(", " + comment["date"].strftime("%Y-%m-%d"))
                try:
                    filewrite.write(" [<a href=\"" + comment["link"] + "\">original</a>]")
                except:
                    pass
                filewrite.write("</h1>\n<p>" + comment["text"] + "</p>\n</div>\n")
                try:
                    filewrite.write("<div class=\"comment reply\">\n<h1>Reply</h1>\n<p>" + comment["reply"] + "</p>\n</div>")
                except:
                    pass
        except:
            pass
        if fffandom or timeelapsed.days < 730:
            filewrite.write("<script>\nasync function sendContact(ev) {\nev.preventDefault();\nconst theFic = document\n.getElementById('ficno').innerHTML;\nconst senderName = document\n.getElementById('nameInput').value;\nconst senderAddress = document\n.getElementById('emailInput').value;\nconst senderSite = document\n.getElementById('siteInput').value;\nconst senderMessage = document\n.getElementById('messageInput').value;\nconst webhookBody = {\nembeds: [{\ntitle: 'New comment received',\nfields: [\n{ name: 'Fic ID', value: theFic },\n{ name: 'Pseudonym', value: senderName },\n{ name: 'Email', value: senderAddress },\n{ name: 'Site', value: senderSite },\n{ name: 'Comment', value: senderMessage }\n]\n}],\n};\n\nconst webhookUrl = 'https://discord.com/api/webhooks/1110564759109120001/nJRKlR2vGf_kQNNniChju_kt5MA-Y6WC3c-3nTrDuwH8s3Pg4wUfgxwd1SI9ZHicXP0m';\n\nconst response = await fetch(webhookUrl, {\nmethod: 'POST',\nheaders: {\n'Content-Type': 'application/json',\n},\nbody: JSON.stringify(webhookBody),\n});\n\nif (response.ok) {\nalert('Comment submitted, thank you!');\n} else {\nalert('This is fucked, sorry.');\n}\n\ndocument.getElementById(\"theform\").reset();\n}\n</script>\n")
        filewrite.close()
        headerfooter.footerwrite(commentspath + "/index.html",False,local)

"""
Generate all comment pages
"""

def allcomments(local=False):
    for filename in os.listdir("build/comments"):
        filepath = os.path.join("build/comments", filename)
        if os.path.isfile(filepath):
            os.unlink(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)
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
            commentpage(ficcount,"originalsmeta",local)
        elif os.path.exists("translationsmeta/" + ficcountstring + ".py"):
            commentpage(ficcount,"translationsmeta",local)
        
if __name__ == "__main__":
    allcomments()

"""
Generate comments index page
"""

def commentindex(local=False):
    # delete existing file
    if os.path.exists("build/comments/index.html"):
        os.remove("build/comments/index.html")
    # write header
    headerfooter.headerwrite("build/comments/index.html","Comments","Comments","",False,local)
    filewrite = open("build/comments/index.html", "a")
    filewrite.write("<p>Comments I receive are archived on this site and linked back to the original. If you don’t want your comments from other sources archived here, or if you require any changes to the presentation of your comments, <a href=\"mailto:eheu48@gmail.com\">please email me</a>. Please note, however, that this website is not indexed by search engines and the only place I really “advertise” it is Dreamwidth.</p>\n<p>You can leave comments on the relevant comment pages for each fic. If you’d like notification of any reply, please leave your email address. If you’d like a link from your pseudonym to a website, you can supply this as well. I’ll happily link to personal websites, Dreamwidth profiles, and (at least for now) AO3 profiles; I’m unlikely to include links to for-profit social media websites, Carrd, or Patreon.</p>\n<p>Comments are turned off on any fic over two years old unless it’s in a Final Fantasy fandom. On AO3, comments are turned off on <b>all</b> fics over two years old, unless they were written for AO3-hosted gift exchanges in 2020 or later.</p>\n")
    filewrite.close()
    headerfooter.footerwrite("build/comments/index.html",False,local)

if __name__ == "__main__":
    commentindex()
