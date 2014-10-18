 # -*- coding: utf-8 -
''' 

Juan Luis Pérez Valbuena
Ingeniería del Conocimiento - Práctica 1 - Algoritmo A* 

'''
import random

''' Metodos que definen el quicksort ''' 
def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )
 
def _quicksort( aList, first, last ):
    if first < last:
      pivot = partition( aList, first, last )
      _quicksort( aList, first, pivot - 1 )
      _quicksort( aList, pivot + 1, last )
 
def partition( aList, first, last ) :
    pivot = first + random.randrange( last - first + 1 )
    swap( aList, pivot, last )
    for i in range( first, last ):
      if aList[i] <= aList[last]:
        swap( aList, i, first )
        first += 1
 
    swap( aList, first, last )
    return first
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

def checkSorted(a):
    for i in xrange(1, len(a) - 1):
        if a[i] < a[i-1]:
            return False
    return True