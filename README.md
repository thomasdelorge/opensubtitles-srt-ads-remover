# opensubtitles-srt-ads-remover

## Description
Easily delete all ads in srt files download from opensubtitles.org

## Requirements
1) Install pikepdf `pip install pikepdf`
2) Install coloredlogs `pip install coloredlogs`
3) Install pysrt `pip install pysrt`

## Warning
This script will overwrite srt files !

## Exemple
Tree :
```
C:.
│   movie1.srt
│   opensubtitles-srt-ads-remover.py
│   movie2.srt
│
└───folder
        movie3.mkv
        movie3.srt
```

Log file :
```
[2022-02-12 22:57:46,910] [INFO] 1) File processing : movie1.fr.srt
[2022-02-12 22:57:47,035] [INFO] Deletion of line 1 : 'Soutenez-nous et devenez membre VIP pour désactiver toutes les publicités sur www.OpenSubtitles.org'
[2022-02-12 22:57:47,821] [INFO] 2) File processing : movie2.fr.srt
[2022-02-12 22:57:48,230] [INFO] Deletion of line 1 : 'Soutenez-nous et devenez membre VIP pour désactiver toutes les publicités sur www.OpenSubtitles.org'
[2022-02-12 22:57:48,827] [INFO] 3) File processing : movie3.fr.srt
[2022-02-12 22:57:49,056] [INFO] 4) File processing : movie4.fr.srt
[2022-02-12 22:57:49,141] [INFO] Deletion of line 1 : 'Annoncez votre produit ou votre marque ici. Contactez www.OpenSubtitles.org aujourd'hui !'
```

## Screenshots
![alt text](https://github.com/thomasdelorge/multiple-pdf-password-remover/blob/main/screenshot.png?raw=true "python console screenshot")
