fname = input('enter filename:')
try:
    fobj = open(fname,'r')
except:
    print('*** file open error:')
else:
    for eachLine in fobj:
        print(eachLine.strip())
    fobj.close()