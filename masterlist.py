import datetime, os
from importlib import import_module

import makeheader
import headerfooter

"""
Code to generate masterlist
"""
    
def listgen(local=False):
    # delete existing file
    if os.path.exists("build/masterlist/index.html"):
        os.remove("build/masterlist/index.html")
    # write header
    headerfooter.headerwrite("build/masterlist/index.html","Masterlist","Fic masterlist","<p>On this page, from newest to oldest, you’ll find basically everything I’ve ever written that is a. fanfiction and b. extant; quality may vary. RPF and things I wrote before 2020 require a username and password to access.</p>",False,local)
    # write fic divs
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
            makeheader.ficgen(ficcount,True,"build/masterlist/index.html",local)
    # write footer
    headerfooter.footerwrite("build/masterlist/index.html",False,local)

if __name__ == "__main__":
    listgen()
