import os
print(__file__)

dir_list = __file__.split('\\')
my_dir = '\\'.join(dir_list[:-1])
my_dir = my_dir +'\\'+ 'temp'
my_dir = my_dir.replace('\\', '\\\\')
print (my_dir)