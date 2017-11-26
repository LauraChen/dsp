# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count>10:
        return "Number of donuts: many"
    else:
        return "Number of donuts: "+str(count)


def both_ends(s):
    s=[x for x in s]
    new=[]
    if len(s)<4:
        return("")
    else:
        new=s[0]+s[1]+s[-2]+s[-1]
        return new

def fix_start(s):
    s=[x for x in s]
    newString=[s[0]]
    for i in range (1,len(s)):
        if s[i]==s[0]:
            newString.append('*')
        else:
            newString.append(s[i])
    return(''.join(newString))

def mix_up(a, b):
    a2=[x for x in a]
    b2=[y for y in b]
    del(a2[0],a2[0])
    del(b2[0],b2[0])
    for i in range(2):
        a2.insert(i,b[i])
        b2.insert(i,a[i])
    return(''.join(a2)+" "+''.join(b2))

def verbing(s):
    if len(s)<3:
        return s
    elif s[-3:]=="ing":
        return s+'ly'
    else:
        return s+'ing'


def not_bad(s):
    snot = s.find('not')
    sbad = s.find('bad')
    if sbad > snot:
        s = s.replace(s[snot:(sbad+3)], 'good')

    return s


def front_back(a, b):
    alength = len(a)
    blength = len(b)
    if alength % 2 == 0:
        aindex = alength // 2
    else:
        aindex = (alength // 2) + 1
    if blength % 2 == 0:
        bindex = blength // 2
    else:
        bindex = (blength // 2) + 1
    afront = a[0:aindex]
    aback = a[aindex:]

    bfront = b[0:bindex]
    bback = b[bindex:]

    return afront + bfront + aback + bback
