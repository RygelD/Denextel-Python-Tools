from string import ascii_letters as ABC
from random import choice 
import os

def fdd(f=None,comp=0):
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
          os.remove(a)
          if u = 0
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
