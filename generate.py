import sys

import masterlist
import commentpage
import feed
import characters
import ships
import events
import indexgen

try:
    if sys.argv[1] == "local":
        local = True
    else:
        local = False
except:
    local = False

if __name__ == "__main__":
    feed.feedgen()
    if local == True:
        masterlist.listgen(True)
        commentpage.allcomments(True)
        commentpage.commentindex(True)
        characters.charlist(True)
        ships.shiplist(True)
        events.eventlist(True)
        indexgen.indexgen(True)
    else:
        masterlist.listgen()
        commentpage.allcomments()
        commentpage.commentindex()
        characters.charlist()
        ships.shiplist()
        events.eventlist()
        indexgen.indexgen()
