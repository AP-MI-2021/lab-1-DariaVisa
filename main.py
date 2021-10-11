'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if n < 2:
    return False
  for i in range(2, n-1):
    if n % i == 0:
      return False
  return True
'''
 returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  produs = 1
  for i in lst:
    produs = produs * i
  return produs
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  while x!=y:
    if x>y: x = x-y
    else: y = y-x
  return x
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  while y != 0:
    a = x % y
    x = y
    y = a
  return x

def main():
  # interfata de tip consola aici
  # print("citeste un numar")
  # n = int( input() )
  # print(is_prime(n))
  # lst = [1,5,7,8,9,10]
  # print( get_product(lst))
  # x = 4
  # y = 8
  # print(get_cmmdc_v1(x,y))
  x = int( input() )
  y = int( input() )
  print(get_cmmdc_v2(x,y))
if __name__ == '__main__':
  main()
