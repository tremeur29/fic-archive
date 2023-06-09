def headerwrite(output,title,headerone,desc,main=False,local=False):
    header = open(output, "a")
    header.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<link rel=\"stylesheet\" href=\"")
    if local:
        header.write("https://tre.praze.net")
    header.write("/fic/archive.css\">\n<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n<link href=\"https://fonts.googleapis.com/css2?family=Hubballi&family=Lato:wght@400;700&family=Merriweather:wght@400;700&display=swap\" rel=\"stylesheet\">\n<title>" + title + "</title>\n</head>\n<body>\n<div id=\"content\">\n<h1>" + headerone + "</h1>\n" + desc + "\n")
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
    if not main:
        footer.write("<hr>\n<p>\n<a href=\"")
        if local:
            footer.write("/home/mdd/Documents/drive/proj/fic-archive/build/index.html")
        else:
            footer.write("/fic")
        footer.write("\">main page\n</a>\n</p>\n")
    footer.write("</div>\n</body>\n</html>")
    footer.close()
