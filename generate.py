import sys

import masterlist
import commentpage
import feed
import characters
import ships
import events
import indexgen
import verifygen
import statsgen
import fandoms

try:
    if sys.argv[1] == "local":
        local = True
    else:
        local = False
except:
    local = False

if __name__ == "__main__":
    if local == True:
        feed.feedgen(True)
        masterlist.listgen(True)
        fandoms.fandomlist(True)
        commentpage.allcomments(True)
        commentpage.commentindex(True)
        characters.charlist(True)
        ships.shiplist(True)
        events.eventlist(True)
        indexgen.indexgen(True)
        verifygen.verifygen(True)
        statsgen.yeargen(True)
    else:
        feed.feedgen()
        masterlist.listgen()
        fandoms.fandomlist()
        commentpage.allcomments()
        commentpage.commentindex()
        characters.charlist()
        ships.shiplist()
        events.eventlist()
        indexgen.indexgen()
        verifygen.verifygen()
        statsgen.yeargen()
