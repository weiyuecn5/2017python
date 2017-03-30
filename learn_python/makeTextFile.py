import os
ls = os.linesep
#获取文件名
fname = input('Enter filename:')
while True:
    if os.path.exists(fname):
        print("ERROR: '%s' already exists"%fname)
        fname = input('Enter another filename:')
    else:
        break
#get file content (text) lines
all = []
print("\nEnter lines ('.' by itself to quit).\n")
#loop until user terminates input
while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)
#write lines to file with proper line-ending
file = open(fname,'w')
file.writelines(['%s%s'%(x,ls) for x in all])
file.close()
print('DONE')