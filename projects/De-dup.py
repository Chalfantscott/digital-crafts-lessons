t = [1, 2, 3, 1, 2, 5, 6, 7, 8]

s = []
for i in t:
  if i not in s:
    s.append(i)

print s