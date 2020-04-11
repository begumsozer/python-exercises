def standart_factoriel(x):
  y=1
  while x > 1:
    y=y*x
    x-=1
    print(y)
  return y

def recursive_factoriel(x):
  if x == 1:
    print(x)
    return x
  else:
    y=x*recursive_factoriel(x-1)
    print(y)
    return y

standart_factoriel(5)
recursive_factoriel(5)
