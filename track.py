import os
import urllib2

MONITOR = (
    ("https://sessionserver.mojang.com/blockedservers", "files/blockedservers"),
)

for page in MONITOR:
    print page[0],
    try:
        page_content = urllib2.urlopen(page[0]).read()
        open(page[1], "w").write(page_content)
        print "OK"
    except:
        print "FAILED"

# Try to commit
os.system("git add .")
os.system("git commit -a -m \"Automatic update\"")
os.system("git push -u origin master")
