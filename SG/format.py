import sys, os
argv = sys.argv

if len(argv) == 1:
  files = [f.replace('.nsb', '') for f in os.listdir('nsb') if f != ".gitignore"]
else:
  files = [f.find('.nsb') == -1 and '%s' % f or f for f in argv[1:]]

if not os.path.exists('log'):
  os.makedirs('log')
  
if not os.path.exists('lines'):
  os.makedirs('lines')
  
log = open('log/format_log.txt', 'w', encoding='utf-8')
glRepDict = {}
  
for fName in files:
  with open("nsb/%s.nsb" % fName, encoding="utf-16-le") as file:
    strs = [row.strip() for row in file]
    strs = strs[::-1]
    
  with open("lines/%s.txt" % fName, "w", encoding='utf-8') as file:
    try:
      log.write('%s\n' % fName)
      repDict = {}
      while True:
        str = strs.pop()
        while str.find("<voice") == -1:
          str = strs.pop()
    
        charName = str[str.find('name')+6:str.find('"', str.find('name')+6)]
        if not charName in repDict:
          repDict[charName] = 1
        else:
          repDict[charName] += 1
          
        if not charName in glRepDict:
          glRepDict[charName] = 1
        else:
          glRepDict[charName] += 1  
        line, str = [], strs.pop()
    
        while str != "":
          while str.find('<') != -1:
            str = '%s%s' % (str[:str.find('<')], str[str.find('>')+1:])
          line.append(str[1:-1].encode('utf-8', errors='ignore').decode('utf-8'))
          str = strs.pop()
      
        file.write('%s|%s\n' % (charName, ' '.join(line)))
    except:
      for n, c in repDict.items():
        log.write('%s | %s\n' % (n, c))
      log.write('\n')

log.write('Summary:\n')
for n, c in [(k, glRepDict[k]) for k in sorted(glRepDict, key=glRepDict.get, reverse=True)]:
  log.write('%s | %s\n' % (n, c))
log.write('\n')