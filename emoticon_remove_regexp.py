#!/usr/bin/python
import sys
import pickle
import re
#pickle because the list is too small. This is a universal list independent of the language
#generic smileys are found in this case
#eyes nose and mouth are generated by a limited number of characters these are used to enumerate the pattern for the smileys
   

def main():
  lines=sys.stdin.readlines()
  for line in lines:
    eyes, noses, mouths = r":;8BX=", r"-~'^", r")(/\|DP"
    pattern1 = "[%s][%s]?[%s]" % tuple(map(re.escape, [eyes, noses, mouths]))
    x=str(re.sub(pattern1,' ',line))
    print x[:-1]
  
if __name__=="__main__":
  main()
