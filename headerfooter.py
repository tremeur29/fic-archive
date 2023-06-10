def headerwrite(output,title,headerone,desc,main=False,local=False):
    header = open(output, "a")
    header.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<link rel=\"stylesheet\" href=\"")
    if local:
        header.write("/home/mdd/Documents/drive/proj/fic-archive/build/")
    else:
        header.write("/fic/")
    header.write("archive.css\">\n<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n<link href=\"https://fonts.googleapis.com/css2?family=Hubballi&family=Lato:wght@400;700&family=Merriweather:wght@400;700&display=swap\" rel=\"stylesheet\">\n<title>" + title + "</title>\n<noscript>\n<style>.jsonly{display:none;}</style>\n</noscript>\n</head>\n<body>\n<div id=\"content\">\n<div id=\"inside\">\n<noscript>\n<div id=\"warning\">\n<p><b>Warning:</b> this part of my site is <b>18+</b>. Fics contain NSFW material and mature themes (death, suicide, mental illness, incest …). Browse at your own risk.</p>\n</div>\n</noscript>\n<h1>" + headerone + "</h1>\n" + desc + "\n")
    if not main:
        header.write("<p>\n<a href=\"")
        if local:
            header.write("/home/mdd/Documents/drive/proj/fic-archive/build/index.html")
        else:
            header.write("/fic")
        header.write("\">main page\n</a>\n</p>\n")
    header.write("<hr>\n")
    header.close()

def footerwrite(output,main=False,local=False):
    footer = open(output, "a")
    footer.write("</div>\n<footer>\n<hr>\n")
    if not main:
        footer.write("<p>\n<a href=\"")
        if local:
            footer.write("/home/mdd/Documents/drive/proj/fic-archive/build/index.html")
        else:
            footer.write("/fic")
        footer.write("\">main page\n</a>\n</p>\n")
    footer.write("<img src=\"")
    if local:
        footer.write("/home/mdd/Documents/drive/proj/fic-archive/build/emacs.jpg")
    else:
        footer.write("/fic/emacs.jpg")
    footer.write("\">\n</footer>\n</div>\n<script>\nif (localStorage.getItem(\"ageVerified\") == null) { window.location = `")
    if local:
        footer.write("/home/mdd/Documents/drive/proj/fic-archive/build/")
    else:
        footer.write("/fic/")
    footer.write("verify/index.html?returnto=${window.location}`; }\n</script>\n</body>\n</html>")
    footer.close()
