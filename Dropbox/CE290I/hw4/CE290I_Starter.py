import time
import os
import shutil
from numpy import genfromtxt

somefile = os.path.abspath("C:\Users\Choco\OneDrive\CE290I\somefile.txt")
startfile = os.path.abspath("C:\Users\Choco\OneDrive\CE290I\startfile.txt")
a = "C:\Users\Choco\OneDrive\CE290I\somefile"
d = "C:\Users\Choco\OneDrive\CE290I\startfile"
c = "C:\Users\Choco\OneDrive\CE290I\cloudfile"
stoploop = 0
i = 0

print "Starting Timer"

shutil.copyfile(startfile, d + str(0) + ".txt")

start = time.time()
while (stoploop < 5):
    try:
        my_data = genfromtxt(os.path.abspath(c + str(i) + ".txt"), delimiter=',')
        statinfo = os.stat(os.path.abspath(c + str(i) + ".txt"))
        print len(my_data)
        if (statinfo.st_size == 36512000) and (my_data[999][4563] == 0.59091):
            print "Cloudfile found and last point verified"
            stoploop = stoploop + 1
            i = i + 1
            shutil.copyfile(startfile, d + str(i) + ".txt")
    except:
        stoploop = stoploop

end = time.time()
print end - start