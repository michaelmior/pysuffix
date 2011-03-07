#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tools_karkkainen_sanders import *

s = 'aa'*10000
n = len(s)
s_unicode = unicode(s,'utf-8','replace')
sa = simple_kark_sort(s_unicode)
#print sa
for i in xrange(n-1) :
  assert(s[sa[i]:] <= s[sa[i+1]:])
  


#print sa
    
