def subsets_k(superset, k):
  if k > len(superset):
    return
  if k == 0:
    yield []
    return

  indices = list(range(k))
  while True:
    yield [superset[i] for i in indices]

    i = k - 1
    while indices[i] == len(superset) - k + i:
      i -= 1
      if i == -1:
        return
    
    indices[i] += 1
    for j in range(i + 1, k):
      indices[j] = indices[i] + j - i

def allSubsetsOfGivenSizeOfaSet(arrInput, arrExpect):
    tablica = []
    for s in subsets_k(arrInput, len(arrExpect)):
        tablica.append(s)
    return tablica
      
def compare(set1, set2):
    return set1.index(set2)+1
    
def newton( n, k ):
    Wynik = 1
    for i in range( 1, k+1 ):
        Wynik = Wynik * ( n - i + 1 ) / i
    return Wynik
      
def rank(n, arrExpect):
    tablica = []
    arrInput= list(range(1, n+1))
    wynikznewtona = 0
    
    tablica = allSubsetsOfGivenSizeOfaSet(arrInput, arrExpect)
    
    wynikwzcompare = compare(tablica, arrExpect)

    for x in range(len(arrExpect)-1):
        x=x+1
        wynikznewtona = wynikznewtona + newton(len(arrInput), x)

    return int(wynikznewtona+wynikwzcompare+1)
    
def unrank(n, number):
    
    if(number > 2**n):
        return "Blad: parametr {} jest wieksze od 2^{}".format(number, n)
        
    if(number == 1):
        return "[]"
        
    if(number <= 0):
        return "Blad: parametr {} jest <=0".format(number)
    
    arrInput= list(range(1, n+1))
    wynikznewtona = 1
    x=1
    
    while(True):
        wynikznewtona = wynikznewtona + newton(len(arrInput), x)
        z=x
        if(wynikznewtona >= number):
            break
        x=x+1
    
    tablica = allSubsetsOfGivenSizeOfaSet(arrInput, list(range(1, z+1)))
    res = tablica[::-1]
    return res[int(wynikznewtona-number)]
        
def succ(n, arr):
    ranknumber = rank(n, arr)
    return unrank(n, ranknumber+1)

def pred(n, arr):
    ranknumber = rank(n, arr)
    return unrank(n, ranknumber-1)

n=50
print("Rank number:", rank(n, [1,2,3,4,5]))
print("Unrank subset:", unrank(n, 23))
print("Succ subset:", succ(n, [49,50]))
print("Pred subset:", pred(n, [1,2,3]))