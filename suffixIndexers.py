import tools_karkkainen_sanders as suffixesTools
import array

class SuffixIndexer :
  def __init__(self, data) :
    self.reset()
    self.buildWord(data)

  def buildWord(self, lstWords):
    raise NotImplementedError  
      
  def getWordAt(self, idx):
    raise NotImplementedError                           
        
  def reset(self):
    self.word = None
    self.sortedSuffixes = None
    self.lcp = None
    
  def sortSuffixes(self) :
    if self.sortedSuffixes != None:
      return
    self.sortedSuffixes = suffixesTools.direct_kark_sort(self.word)

  def computeLCP(self) :
    if self.lcp != None:
      return
    self.sortSuffixes()
    self.lcp = suffixesTools.LCP(self.word, self.sortedSuffixes)   
          
  def _search(self, word):
    self.sortSuffixes()
    min_ = 0
    max_ = len(self.sortedSuffixes) - 1 
    len_word = len(word)
    it_word = range(len(word))
    mid = 0
    while 1:
      mid = (max_ + min_) / 2
      start = self.sortedSuffixes[mid]
      for i in it_word:
        c1 = self.word[start + i]
        c2 = word[i]
        if c1 > c2: 
          if mid == max_:
            return None
          max_ = mid
          break
        elif c1 < c2:
          if mid == min_:
            return None
          min_ = mid
          break
      else:
        return mid

  def _searchAll(self, word):
    self.computeLCP()
    len_word = len(word)
    idx = self._search(word)
    if idx == None: 
      return None, None
    lcp = self.lcp
    words = set()
    sup = inf = idx
    while 1: 
      inf -= 1 
      if self.lcp[inf] < len_word:
        break
    inf += 1
    while 1: 
      if self.lcp[sup] < len_word:
        break
      sup += 1 
    return (inf, sup)

  def searchOneWord(self, word):
    idx = self._search(word)
    if idx == None:
      return None
    return self.getWordAt(idx)
    
  def searchAllWords(self, word):
    inf, sup = self._searchAll(word)
    if inf == None: 
      return []
    result = [] 
    for idx in xrange(inf, sup+1):
      result.append(self.getWordAt(idx))
    return result
    
    
class ListIndexer(SuffixIndexer):
  def buildWord(self, lstWords):
    if self.word != None:
      return
    self.array_str = lstWords
    charFrontier = chr(2)
    self.word = charFrontier.join(self.array_str)
  
    self.indexes = array.array('i', [0]*len(self.word))
    idx_w = k = 0
    for w in self.array_str:
      for _ in w :
        self.indexes[k] = idx_w
        k += 1
      idx_w += 1
      k += 1

  def getWordAt(self, idx):
    return self.array_str[self.indexes[self.sortedSuffixes[idx]]]         

class DictValuesIndexer(SuffixIndexer):
  def buildWord(self, dictWords):
    if self.word != None:
      return
#    self.array_str = lstWords
    charFrontier = chr(2)
    self.word = charFrontier.join(dictWords.itervalues())

    self.indexes = {}
    idx_w = i = 0
    for k, v in dictWords.iteritems():
      for _ in v :
        self.indexes[i] = k
        i += 1
      i += 1

  def getWordAt(self, idx):
    return self.indexes[self.sortedSuffixes[idx]]
      
    
if __name__ == '__main__':                             
  m = ListIndexer([
    'azerty',
    'ayerty',
    'axxxty',
    'azeyyy',
  ])

  s = 'y'

  print s, m.searchOneWord(s)

  print s, m.searchAllWords(s)

  m = DictValuesIndexer({
    'a':'azerty',
    'b':'ayerty',
    'c':'axxxty',
    'd':'azeyyy',
  })

  s = 'y'

  print s, m.searchOneWord(s)

  print s, m.searchAllWords(s)
