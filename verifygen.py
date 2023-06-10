import os

import headerfooter

def verifygen(local=False):
    # delete existing file
    if os.path.exists("build/verify/index.html"):
        os.remove("build/verify/index.html")
    # write header
    headerfooter.headerwrite("build/verify/index.html","Tré’s fic archive","Warning","",True,local)
    filewrite = open("build/verify/index.html", "a")
    filewrite.write("<p><strong>Please note before proceeding:</strong></p>\n<p>Some of my fanfiction is NSFW (ranging from slightly obscene language to explicit sex scenes), some is RPF, and some of it contains mature or potentially objectionable themes (death, suicide, mental illness, incest …). Ratings and warnings are given accordingly, <strong>don’t like don’t read</strong>. If you happen to be under 18, kindly gtfo and <em>read some real literature instead</em>. Honestly, it will be much more edifying.</p>\n<label for=\"verifyage-checkbox\">Please tick to confirm you have read this warning and are an adult:</label>\n<input type=\"checkbox\" id=\"verifyage-checkbox\">\n<button id=\"verifyage-button\">Let me in!</button>\n</div>\n</div>\n<script>\nvar verifyageButton = document.getElementById(\"verifyage-button\"); var verifyageCheckbox = document.getElementById(\"verifyage-checkbox\"); verifyageButton.addEventListener(\"click\", () => {if (verifyageCheckbox.checked) {localStorage.setItem(\"ageVerified\", \"✓\"); if (window.location = window.location.search.startsWith(\"?returnto=\")) {window.location = window.location.search.substring(\"?returnto=\".length);} else {window.location = \"")
    if local:
        filewrite.write("/home/mdd/Documents/drive/proj/fic-archive/build/index.html")
    else:
        filewrite.write("/fic")
    filewrite.write("\";}} else {alert(\"You must agree before proceeding.\");}});\n</script>\n</body>\n</html>")
    filewrite.close()

if __name__ == "__main__":
    verifygen()
