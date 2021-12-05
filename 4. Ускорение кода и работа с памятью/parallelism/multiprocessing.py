def if_prime(x):
  if x <= 1:
    return 0
  elif x <= 3:
    return x
  elif x % 2 == 0 or x % 3 == 0:
    return 0
  i = 5
  while i ** 2 <= x:
    if x % i == 0 or x % (i + 2) == 0:
      return 0
    i += 6
  return x

