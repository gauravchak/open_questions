def binary_search(a: list, key):
  '''
  a is sorted list of type T
  key is of type T
  It returns the index of the element which matches key
  '''
  if not a:
    return -1
  if (len(a) == 1) and (a[0] != key):
    return -1
  mid_idx = len(a)//2
  if (a[mid_idx] < key):
    rt_idx = binary_search(a[mid_idx+1:], key)
    if (rt_idx == -1):
      return -1
    else:
      return ((mid_idx + 1) + rt_idx)
  elif (a[mid_idx] > key):
    return (binary_search(a[:mid_idx], key))
  else:
    return mid_idx
  return -1
