# SGDialogs
Python script for parsing Steins;Gate and Steins;Gate 0 scripts files

## Needed files
At least you need .nsb files from S;G or .txt files from S;G0. You can google them or extract by yourself from the game
Put .nsb to SG/nsb and .txt to SG0/txt

### format.py
```
<python> format.py [files...]

[files...] - filenames from nsb/txt folder. If none provided, script will format ALL files inside nsb/txt folder
```
#### Examples:
Format all files
```
py format.py
```
Format only SG0_00_01.txt
```
py format.py SG0_00_01
```
### qa.py
```
<python> qa.py <character> [files...]

<character> - character name. Required
[files...] - filenames from nsb/txt folder. If none provided, script will extract dialogs from ALL files inside nsb/txt folder
```
#### Examples:
Extract all Okabe Rintaro's dialogs
```
py qa.py Rintaro
```
Extract all Amane Suzuha's dialogs from first scene
```
py qa.py Suzuha SG0_00_01
```
