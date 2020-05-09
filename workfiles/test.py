
import os
os.getcwd()
os.chdir('../')
file = open('tem.txt','w')
file.write('asdf\sdsd110f')
file.close()
input()
os.remove('tem.txt')
print(os.listdir('./'))