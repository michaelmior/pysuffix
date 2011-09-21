#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import tools_karkkainen_sanders as tks
import array
import suffixIndexers as si
import random
import re

def get_all_pos(w, pattern) :
  i = 0
  lt = len(w)
  res = []
  while i < lt :
    try :
      pos = w.index(pattern, i)
      res.append(pos)
      i = pos + 1
    except Exception, e :
      return res
  return res

def naive_get_all_list(l, pattern) :
  res = []
  for i in xrange(len(l)) :
    w = l[i]
    if is_pattern_in(pattern, w) :
      res.append(i)
  return res

def naive_get_all_dict(d, pattern) :
  res = []
  for i,w in d.iteritems() :
    if is_pattern_in(pattern, w) :
      res.append(i)
  return res

def naive_get_all_with_pos_list(l, pattern) :
  res = []
  for w in l :
    r = get_all_pos(w, pattern)
    for o in r :
      res.append((w,o))
  return res

def naive_get_all_with_pos_dict(d, pattern) :
  res = []
  for i,w in d.iteritems() :
    r = get_all_pos(w, pattern)
    for o in r :
      res.append((i,o))
  return res
    
s = 'abcabcc'
d = {1:s}
l = [s]
p = 'c'

r1 = naive_get_all_with_pos_list(l, p)
r2 = naive_get_all_with_pos_dict(d, p)
print r1
print r2
1/0


def naive_search_list(l, pattern) :
  for i in l :
    if is_pattern_in(pattern, i) :
      return True
  return False

def naive_search_all_list(l, pattern) :
  res = []
  for i in l :
    if is_pattern_in(pattern, i) :
      res.append(i)
  return res

def is_pattern_in(pattern, word) :
  return pattern in word

def is_pattern_at_pos(pattern, pos, word) :
  return word[pos:pos+len(pattern)] == pattern

def naive_search_dict(d, pattern) :
  res = []
  for i,v in d.iteritems() :    
    if is_pattern_in(pattern, v) :
      res.append(i)
  return res

class Test_list_indexer :
  def setUp(self) :
    self.l,self.pattern = self.getData()
    self.index = si.ListIndexer(self.l)

  def test_one_word(self) :
    res = self.index.searchOneWord(self.pattern)
    if res == None :
      self.assertFalse(naive_search_list(self.l, self.pattern))
    else :
      test = res.index(self.pattern,0)

  def test_all_words(self) :
    res = self.index.searchAllWords(self.pattern)
    for i in res :
      try :
        r = i.index(self.pattern)
      except Exception, e :
        self.assertTrue(False)
    self.assertTrue(True)

  def test_one_word_and_pos(self) :
    res = self.index.searchOneWordAndPos(self.pattern)
    if res == None :
      self.assertFalse(naive_search_list(self.l, self.pattern))
    else :
      w,p = res
      self.assertTrue(is_pattern_at_pos(self.pattern, p, w))

  def test_all_words_and_pos(self) :
    res = self.index.searchAllWordsAndPos(self.pattern)
    if res == [] :
      self.assertFalse(naive_search_all_list(self.l, self.pattern))
    else :
      for w,p in res :
        self.assertTrue(is_pattern_at_pos(self.pattern, p, w))


class Test_dict_values_indexer :
  def setUp(self) :
    self.d, self.pattern = self.getData()
    self.index = si.DictValuesIndexer(self.d)

  def test_one_word(self) :
    res = self.index.searchOneWord(self.pattern)
    if res == None :
      self.assertFalse(naive_search_list(self.d.values(), self.pattern))
    else :
      w = self.d[res]
      test = w.index(self.pattern,0)

  def test_all_words(self) :
    res = self.index.searchAllWords(self.pattern)
    for i in res :
      self.assertTrue(is_pattern_in(self.pattern, self.d[i]))

  def test_one_word_and_pos(self) :
    res = self.index.searchOneWordAndPos(self.pattern)
    if res == None :
      self.assertFalse(naive_search_dict(self.d, self.pattern))
    else :
      k,p = res
      w = self.d[k]
      self.assertTrue(is_pattern_at_pos(self.pattern, p, w))

  def test_all_words_and_pos(self) :
    res = self.index.searchAllWordsAndPos(self.pattern)
    if res == [] :
      self.assertFalse(naive_search_dict(self.d, self.pattern))
    else :
      for k,p in res :
        w = self.d[k]
        self.assertTrue(is_pattern_at_pos(self.pattern, p, w))

class Test_list_a_b(Test_list_indexer, unittest.TestCase) :
  def getData(self) :
    l = ['a'*100 for i in xrange(100)]
    return l,'bbb'

class Test_list_a_a(Test_list_indexer, unittest.TestCase) :
  def getData(self) :
    l = ['a'*100 for i in xrange(100)]
    return l,'aaa'

class Test_list_python(Test_list_indexer, unittest.TestCase) :
  def getData(self) :
    s = open('Python.htm','r').read()
    s_unicode = unicode(s,'utf-8','replace')[20000:25000]
    l = re.split('\s', s_unicode)
    return l, 'ython'

class Test_dict_a_a(Test_dict_values_indexer, unittest.TestCase) :
  def getData(self) :
    d = dict([(i,'a'*10) for i in xrange(10)])
    return d,'aaa' 

class Test_dict_a_b(Test_dict_values_indexer, unittest.TestCase) :
  def getData(self) :
    d = dict([(i,'a'*10) for i in xrange(10)])
    return d,'bbb' 

class Test_dict_python(Test_dict_values_indexer, unittest.TestCase) :
  def getData(self) :
    s = open('Python.htm','r').read()
    s_unicode = unicode(s,'utf-8','replace')[20000:25000]
    l = re.split('\s', s_unicode)
    d = dict((i, l[i]) for i in xrange(len(l))) 
    return d, 'ython'

if (__name__ == '__main__') :
  unittest.main() 
