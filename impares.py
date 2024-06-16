
li=[1,3,5,78,9,15,18,12]

def odd(n):
  if n%2!=0:
    return n
a=[e for e in li if odd(e)]
print(a)
