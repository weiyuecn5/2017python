def chengfa(x,y):
    return x*y
def pingfen(x):
    if 90<=x<=100:
        return 'A'
    elif 80<=x<=89:
        return 'B'
    elif 70<=x<=79:
        return 'C'
    elif 60<=x<=69:
        return 'D'
    elif x<60:
        return 'F'
def jisuanqi():

a = '1 + 1'
print(a.split())