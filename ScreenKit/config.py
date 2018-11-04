# Configuration Script
#
__version__ = 0.1
RELEASE = 0.1
from string import ascii_letters as ABC
from random import choice 
import os
from shutil import rmtree
from sys import path
import time

def fdd(f=None,comp=0):
  def out(u=0):
    if u = 0:
      print('File Deletion Device - press Ctrl-D (EOF) to exit\n')
      m = 'Try again (or Ctrl-D (EOF) to exit)\n'
    else:
      m = 'Moving on\n'
    if f != None:
      a = input('File Name: \n')
      b = input('Retype File Name: \n')
    else:
      a = f
      b = f
    if a != b:
      print("Did not match. " + m)
    else:
      if os.path.exists(a):
        
        if u == 0:
          x = ""
          for i in range (0,6):
            x = x + choice(ABC)
        
          print('File found. To confirm, enter the confirmation code "' + x +'" (without quotation marks).')
          q = input('Enter confirmation code: ')
          w = input('Retype path to file: ')
        else:
          q = 1
          w = 1
          x = 1
        if q != w or q != x:
          print("Did not match. "+ m)
        else:
          if u == 0:
            print('File destruction in progress (deleting ' + a + ')... (Ctrl-D to exit)')
            for i in range(0,5):
              time.sleep(1)
              print('Deleting... ['+str(5-i) + ' seconds left]')
          os.remove(a)
          if u == 0:
            print('\n    -----    \nFile deleted.\n   -----    ')
          return 1
      else:
        print("The file " + a + " does not exist. " + m)
    if comp != 'dxl':
      y = 0
      while y != 1:
        y = out()
    else:
      out(1)
print('NOTICE: This program will be deleted after execution. Press Ctrl-D to exit and keep this file (other files may not work)')

if os.path.exists(os.path.dirname(os.getcwd())+'dev'):
  a = os.path.dirname(os.getcwd())+'dev'        

  x = ""
  for i in range (0,6):
    x = x + choice(ABC)

  print('Delete \'dev\'? Enter the confirmation code "' + x +'" (without quotation marks) to delete it.')
  q = input('Enter confirmation code: ')
  w = input('Retype path to file: ')

  if q != w or q != x:
    print("Did not match. Press Ctrl-D and retry if you want to delete 'dev'")
  else:
    print('Folder destruction in progress (deleting dev)... (Ctrl-D to exit)')
    for i in range(0,5):
      time.sleep(1)
      print('Deleting... ['+str(5-i)+' seconds left]')   
    shutil.rmtree(a, ignore_errors=True)
    print('\n    -----    \nDev deleted.\n   -----    ')
print('File destruction in progress (deleting config.py)... (Ctrl-D to exit)')
for i in range(0,5):
  time.sleep(1)
  print('Deleting... ['+ str(5-i) +' seconds left]')
fdd(sys.path,'dxl')
d = open('deletion.py',w)
d.write('''def fdd(f=None,comp=0):
  def out(u=0):
    if u = 0:
      print('File Deletion Device - press Ctrl-D (EOF) to exit\n')
      m = 'Try again (or Ctrl-D (EOF) to exit)\n'
    else:
      m = 'Moving on\n'
    if f != None:
      a = input('Path to file: ')
      b = input('Retype path to file: ')
    else:
      a = f
      b = f
    if a != b:
      print("Did not match. " + m)
    else:
      if os.path.exists(a):
        
        if u == 0:
          x = ""
          for i in range (0,6):
            x = x + choice(ABC)
        
          print('File found. To confirm, enter the confirmation code "' + x +'" (without quotation marks).')
          q = input('Enter confirmation code: ')
          w = input('Retype path to file: ')
        else:
          q = 1
          w = 1
          x = 1
        if q != w or q != x:
          print("Did not match. "+ m)
        else:
          if u == 0:
            print('File destruction in progress (deleting ' + a + ')... (Ctrl-D to exit)')
            for i in range(0,5):
              time.sleep(1)
              print('Deleting... ['+str(5-i) + ' seconds left]')
          os.remove(a)
          if u == 0:
            print('\n    -----    \nFile deleted.\n   -----    ')
          return 1
      else:
        print("The file " + a + " does not exist. " + m)
    if comp != 'dxl':
      y = 0
      while y != 1:
        y = out()
    else:
      out(1)
    active = True ''')
    
d.close()
        
