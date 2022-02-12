import os
import logging
import coloredlogs
import pysrt

# CHANGE KEYWORD HERE
ads = "www.OpenSubtitles.org"

# Logs to scriptName.log
scriptName = os.path.basename(__file__)
logging.basicConfig(level = logging.DEBUG,
                    filename = scriptName + ".log",
                    filemode = "a",
                    encoding = 'utf-8',
                    format = '[%(asctime)s] [%(levelname)s] %(message)s')

# Logs into console
mylogs = logging.getLogger(__name__)
stream = logging.StreamHandler()
mylogs.addHandler(stream)
coloredlogs.install(level=logging.DEBUG, 
                    logger=mylogs,
                    fmt='[%(asctime)s] [%(levelname)s] %(message)s')

rootdir = os.getcwd()
nb = 0
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".srt"):
            nb += 1
            mylogs.info(str(nb) + ") File processing : " + file)
            # Search $ads in each line of the SRT file
            srt = pysrt.open(filepath)
            for i, l in enumerate(srt):
                if ads in (l.text):
                    mylogs.info(f"Deletion of line {i+1} : '{l.text}'")
                    del srt[i]
            srt.save(filepath)

os.system("pause")