from string import ascii_letters as ABC
from random import choice 
import os

def fdd():
  while True:
    print('File Deletion Device - press Ctrl-D (EOF) to exit\n')
    a = input('Path to file: ')
    b = input('Retype path to file: ')
    if a != b:
      print("Did not match. Try again (or Ctrl-D (EOF) to exit)\n")
    else:
      import os
      if os.path.exists(a):
        x = ""
        for i in range (0,6):
          x = x + choice(ABC)
        print('File found. To confirm, enter the confirmation code "' + x +'" (without quotation marks).')
        a = input('Enter confirmation code: ')
        b = input('Retype path to file: ')
        if a != b or a != x:
          print("Did not match. Try again (or Ctrl-D (EOF) to exit)\n")
        else:
          os.remove(a)
          print('\n    -----    \nFile deleted.\n   -----    '

      else:
        print("The file does not exist. Try again (or Ctrl-D (EOF) to exit)\n")
       
