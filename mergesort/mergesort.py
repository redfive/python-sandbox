#!/bin/env python

from collections import deque

def mergesort ( listA, listB, depth ):
  print "%sMerging %s and %s" % (depth, listA, listB)
  if len(listA) == 0:
    return listB
  if len(listB) == 0:
    return listA

  retList = []
  if listA[0] <= listB[0]:
    retList.append(listA[0])
    retList.extend( mergesort( listA[1:], listB, depth + " " ) )
  else:
    retList.append(listB[0])
    retList.extend( mergesort( listA, listB[1:], depth + " " ) )

  return retList

def sort ( list ):
  print "Sorting %s" % (list)
  listQ = deque()
  for item in list:
    # add the items as lists so the merge operation can assume list inputs
    listQ.append([item])

  # once we get to one item in the queue we've been fully sorted
  while len(listQ) > 1:
    # pop the top two items and sort them, then append the resulting
    # list item to the end of the queue.
    listQ.append( mergesort( listQ.popleft(), listQ.popleft(), "" ) )

  print listQ
  

if __name__ == "__main__":
  sorted = sort( [ 5, 8, 4, 14, 3, 20, 2, 1, 100] )
  #sorted = sort( [ 3, 2, 1] )
