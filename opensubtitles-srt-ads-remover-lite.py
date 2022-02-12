import os
import pysrt

# CHANGE KEYWORD HERE
ads = "www.OpenSubtitles.org"

rootdir = os.getcwd()
nb = 0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".srt"):
            nb += 1
            print(str(nb) + ") File processing : " + file)
            # Search $ads in each line of the SRT file
            srt = pysrt.open(filepath)
            for i, l in enumerate(srt):
                if ads in (l.text):
                    print(f"Deletion of line {i+1} : '{l.text}'")
                    del srt[i]
            srt.save(filepath)

os.system("pause")