import time
import os
import shutil

somefile = os.path.abspath("C:\Users\Bryan\OneDrive\CE290I\somefile.txt")
a = "C:\Users\Bryan\OneDrive\CE290I\startfile"
c = "C:\Users\Bryan\OneDrive\CE290I\cloudfile"
stoploop = 0
i = 0

print "Starting Timer"

start = time.time()
while (stoploop < 5):
    try:
        statinfo = os.stat(os.path.abspath(a + str(i) + ".txt"))
        if (statinfo.st_size == 7):
            print "Startfile found"
            b = c + str(i) + ".txt"
            shutil.copyfile(somefile, b)
            stoploop = stoploop + 1
            i = i + 1
    except:
        stoploop = stoploop

end = time.time()
print end - start