import suffixIndexers as si
import time

l = open('suffixIndexers.py').readlines()
l = l * 100
word = 'search'
runs = 10000

def naive_get_all_list(l, pattern) :
  return list((i for i, w in enumerate(l) if pattern in w))

t0 = time.time()
for i in xrange(runs):
  naive_get_all_list(l, word)
t1 = time.time()
print t1 - t0

t0 = time.time()
indexedList = si.ListIndexer(l)
for i in xrange(runs):
  indexedList.searchAllWords(word)
t1 = time.time()
print t1 - t0
