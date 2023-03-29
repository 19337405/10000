import datetime
f = open("subtitles/10000.srt", "w")
i = 0

for i in range(10000):
    f.write(str(i + 1) + "\n" + str(str(datetime.timedelta(milliseconds=(i) * 10))[:11] + " --> " + str(datetime.timedelta(milliseconds=(i + 1) * 10))[:11]).replace(".", ",") + "\n" + str(i + 1) + "\n\n")

f.close()