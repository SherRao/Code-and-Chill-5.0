arr = []
counter = 0


def append(n, value):
  global counter
  for i in range(1, value + 1):
    if len(arr) < n:
      arr.append(i)
    else:
      arr[counter % n] = i
    counter += 1
