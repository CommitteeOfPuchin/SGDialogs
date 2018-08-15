import sys, os
argv = sys.argv

def strClear(str):
  while str.find('[') != -1:
    brStart, brEnd = str.find('['), str.find(']')+1
    if str[brStart:brEnd] == '[name]':
      brEnd = str.find(']', brEnd)+1
    str = '%s%s' % (str[:brStart], str[brEnd:])
    
  str = str.replace('“', '').replace('”', '')
    
  return str
  
def strName(str):
  return str[str.find('[name]')+6:str.find('[line]')]

if len(argv) == 1:
  files = [f.replace('.txt', '') for f in os.listdir('txt') if f != ".gitignore"]
else:
  files = [f.find('.txt') == -1 and '%s' % f or f for f in argv[1:]]
  
if not os.path.exists('log'):
  os.makedirs('log')
  
if not os.path.exists('lines'):
  os.makedirs('lines')

log = open('log/format_log.txt', 'w', encoding='utf-8')
glRepDict = {}
  
for fName in files:
  with open("txt/%s.txt" % fName, encoding="utf-8") as file:
    strs = [row.strip() for row in file]
    strs = strs[::-1]
    
  with open("lines/%s.txt" % fName, "w", encoding='utf-8') as file:
    try:
      log.write('%s\n' % fName)
      repDict = {}
      while True:
        str = strs.pop()
        while str.find("[name]") == -1:
          str = strs.pop()
    
        charName = strName(str)
        str = strClear(str)
        
        if not charName in repDict:
          repDict[charName] = 1
        else:
          repDict[charName] += 1
          
        if not charName in glRepDict:
          glRepDict[charName] = 1
        else:
          glRepDict[charName] += 1  
      
        file.write('%s|%s\n' % (charName, str))
    except:
      for n, c in repDict.items():
        log.write('%s | %s\n' % (n, c))
      log.write('\n')

log.write('Summary:\n')
for n, c in [(k, glRepDict[k]) for k in sorted(glRepDict, key=glRepDict.get, reverse=True)]:
  log.write('%s | %s\n' % (n, c))