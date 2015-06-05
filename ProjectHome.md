# pysuffix : a python implementation for efficient augmented suffix array construction. #
  * [What does it do?](http://code.google.com/p/pysuffix/#What_does_it_do?)
  * [Usage](http://code.google.com/p/pysuffix/#Usage)
  * [Pysuffix v2.1](http://code.google.com/p/pysuffix/#Pysuffix_v2.1)
  * [Bench pysuffix please](http://code.google.com/p/pysuffix/#Bench_pysuffix_please)
  * [Pysuffix v2.0](http://code.google.com/p/pysuffix/#Pysuffix_v2.0)
  * [Pysuffix v1.0](http://code.google.com/p/pysuffix/#Pysuffix_v1.0)
  * [See also](#See_also.md)

## What does it do ? ##

Let's start with a string S = 'abcdabcd'
You can represent S in that way :

<table>
<tr><td>a</td><td>b</td><td>c</td><td>d</td><td>a</td><td>b</td><td>c</td><td>d</td><td>$</td></tr>
<tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr>
</table>

, where '$' is the smallest letter in the alphabet used to write S.

Each offset can be seen as a suffix of the string S. For exemple, in S :

<table>
<blockquote><tr><th>offset</th><th>suffix</th></tr>
<tr><td>0</td><td>abcdabcd$</td></tr>
<tr><td>1</td><td>bcdabcd$</td></tr>
<tr><td>2</td><td>cdabcd$</td></tr>
<tr><td>3</td><td>dabcd$</td></tr>
<tr><td>4</td><td>abcd$</td></tr>
<tr><td>5</td><td>bcd$</td></tr>
<tr><td>6</td><td>cd$</td></tr>
<tr><td>7</td><td>d$</td></tr>
<tr><td>8</td><td>$</td></tr>
</table></blockquote>

Pysuffix computes for you the augmented suffix array as follow :

<table>
<blockquote><tr><th>i</th><th>lcp</th><th>offset</th><th>suffix</th></tr>
<tr><td>0</td><td>0</td><td>8</td><td>$</td></tr>
<tr><td>1</td><td>4</td><td>4</td><td>abcd$</td></tr>
<tr><td>2</td><td>0</td><td>0</td><td>abcdabcd$</td></tr>
<tr><td>3</td><td>3</td><td>5</td><td>bcd$</td></tr>
<tr><td>4</td><td>0</td><td>1</td><td>bcdabcd$</td></tr>
<tr><td>5</td><td>2</td><td>6</td><td>cd$</td></tr>
<tr><td>6</td><td>0</td><td>2</td><td>cdabcd$</td></tr>
<tr><td>7</td><td>1</td><td>7</td><td>d$</td></tr>
<tr><td>8</td><td>0</td><td>3</td><td>dabcd$</td></tr>
</table></blockquote>

suffix\_array = (4, 0, 5, 1, 6, 2, 7, 3)
lcp = (4, 0, 3, 0, 2, 0, 1, 0)

## Usage ##

```
>user@machina tar -xzvf pysuffix.2.1.tar.gz
>user@machina python suffix_array.test.py
```

## Pysuffix v2.1 ##

### Inside suffix\_array.test.py ###

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools_karkkainen_sanders as tks

s = 'abab'
s_unicode = unicode(s,'utf-8','replace')
sa = simple_kark_sort(s_unicode)
lcp = tks.LCP(s,sa)
print sa
print lcp
```

print :
```
[2, 0, 3, 1, 0, 0, 0] #suffix_array
[2, 0, 1, 0] #longest common prefixes
```

`lcp[i] : ` longest common prefix between `sa[i]` and `sa[i+1]`

You surely only be interested in `sa[0:n]`, where `n` is the length of `s` :
```
[2, 0, 3, 1]
```

## Bench pysuffix please ##

Tests are done with an Intel Atom N280 (benchmarking with mini-pc is so fun). The string used for the benchs is
```
str = 'a' * len
```

Runs with Python :

<img src='http://users.info.unicaen.fr/~rbrixtel/img_svn/bench_suffix.png' alt='bench_pysuffix' width='550' />

<br />

Runs with Pypy :

<img src='http://users.info.unicaen.fr/~rbrixtel/img_svn/bench_pypysuffix.png' alt='bench_pysuffix' width='550' />


## Pysuffix v2.0 ##

### Inside suffix\_array.test.py ###

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tools_karkkainen_sanders import *

s = 'abcdabcd'
s_unicode = unicode(s,'utf-8','replace')
sa = simple_kark_sort(s_unicode)
print sa
```

print :
```
[4, 0, 5, 1, 6, 2, 7, 3, 0, 0, 0]
```

You surely only be interested in `sa[0:n]`, where `n` is the length of `s` :
```
[4, 0, 5, 1, 6, 2, 7, 3]
```

## Pysuffix v1.0 ##

### Inside suffix\_array.test.py ###

Some imports

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import *
from StringIO import StringIO
from tools import *
from suffix_array import Suffix_array
import sys
```

Prepare string in unicode

```
str = 'abcabc'
str_unicode = utf82unicode(str)
```

Create Suffix\_array and feed it with unicode strings.
Here, twice 'abcabc'.

```
sa1 = Suffix_array()
sa1._add_str(str_unicode)
sa1._add_str(str_unicode)
```

Run the Karkkaïnen and Sanders sort

```
sa1.karkkainen_sort()
```

Write the 5th letters of each suffix in a sorted order

```
sa1._write_su_n(5)
```

Or you can simply access to the sorted suffix array

```
sorted = sa1.suffix_array
```

## See also ##

  * [py-rstr-max : maximum repeats in strings detection for python users](http://code.google.com/p/py-rstr-max)

### And also ###

  * [linsuffarr.py](http://jgosme.perso.info.unicaen.fr/Linsuffarr.html)