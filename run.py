import sys 
import os 


if len(sys.argv) < 2:
     print('There was no app specified')
     exit()
app_name = sys.argv[1]

sys.path.append('pygame-psp')
sys.path.append(app_name)

