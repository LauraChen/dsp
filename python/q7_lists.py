# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    count = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1

    return count


def front_x(words):
    xlist = []
    alist = []

    for word in words:
        if word.startswith('x'):
            xlist.append(word)
        else:
            alist.append(word)

    return sorted(xlist) + sorted(alist)

def last(t): return t[-1]

def sort_last(tuples):
    return sorted(tuples, key=last)

def remove_adjacent(nums):
    i = 1
    while i < len(nums):    
        if nums[i] == nums[i-1]:
            nums.pop(i)
            i -= 1  
        i += 1
    return nums


def linear_merge(list1, list2):
    sortedlist=sorted(list1+list2)
    return sortedlist
