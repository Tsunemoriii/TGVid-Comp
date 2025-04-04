#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", default="4560655", cast=int)
    API_HASH = config("API_HASH", default="ce54eacb9b6854768b06daa2864e88fa")
    BOT_TOKEN = config("BOT_TOKEN", default="6722197684:AAExVaNGi0MO1nzY9fi4Sv0nfNl9cpdPcYw")
    DEV = 1287276743
    OWNER = config("OWNER", default="1446111611 682111519")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By AnshuSharma (https://github.com/Anshusharma75/TG-videoCompress)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMB = config("THUMBNAIL", default="https://telegra.ph/file/a1cb73168488b99c975bb.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
