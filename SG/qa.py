import sys, os
argv = sys.argv

if len(argv) < 2:
  sys.exit('Usage: qa.py <character> [files...]')

mainChar = argv[1]

if len(argv) == 2:
  files = [f.replace('.txt', '') for f in os.listdir('lines') if f != ".gitignore"]
else:
  files = [f.find('.txt') == -1 and '%s' % f or f for f in argv[2:] if os.path.exists('lines/%s.txt' % f)]
  
  if len(files) == 0:
    sys.exit('Usage: qa.py <character> [files...]')

glRepDict = {}
sum = 0

if not os.path.exists('log'):
  os.makedirs('log')
  
if not os.path.exists('qa/%s' % mainChar):
  os.makedirs('qa/%s' % mainChar)
  
log = open('log/qa_%s_log.txt' % mainChar, 'w', encoding='utf-8')
aggr = open('qa/%s_qa.txt' % mainChar, 'w', encoding='utf-8')
  
for fName in files:
  with open("lines/%s.txt" % fName, encoding="utf-8") as file:
    strs = [row.strip() for row in file]
    strs = strs[::-1]
    
  with open("qa/%s/%s.txt" % (mainChar, fName), "w", encoding='utf-8') as file:
    try:
      log.write('%s\n' % fName)
      repDict = {}
      history = []
      while True:
        mainS, secS, secChar = [], [], ''
        str = strs.pop()
        if str.startswith(mainChar):
          try:
            mainS.append(str[str.find('|')+1:])
              
            while True:
              tmpS = strs.pop()
              if tmpS.startswith(mainChar):
                tmpS = tmpS[tmpS.find('|')+1:]
                mainS.append(tmpS)
              else:
                break
            
            rew = history[::-1]
            secChar = rew[0][:rew[0].find('|')]
            if secChar == mainChar:
              continue
            secS.append(rew[0][rew[0].find('|')+1:])
            for i in rew[1:]:
              if i[:i.find('|')] == secChar:
                secS.append(i[i.find('|')+1:])
              else:
                break
            
            if not secChar in repDict:
              repDict[secChar] = 1
            else:
              repDict[secChar] += 1
          
            if not secChar in glRepDict:
              glRepDict[secChar] = 1
            else:
              glRepDict[secChar] += 1  
                    
            file.write('%s|%s\n%s|%s\n' % (secChar, ' '.join(secS), mainChar, ' '.join(mainS)))
            aggr.write('%s|%s\n%s|%s\n\n' % (secChar, ' '.join(secS), mainChar, ' '.join(mainS)))
            sum += 1
            history.extend(['%s|%s' % (mainChar, mS) for mS in mainS])
            history.append(tmpS)
          except:
            pass
            
        else:
          history.append(str)
            
    except:
      for n, c in repDict.items():
        log.write('%s | %s\n' % (n, c))
      log.write('\n')
      
log.write('%s dialogs\n\n' % mainChar)
log.write('Total | %s\n' % sum)
for n, c in [(k, glRepDict[k]) for k in sorted(glRepDict, key=glRepDict.get, reverse=True)]:
  log.write('%s | %s\n' % (n, c))
log.write('\n')