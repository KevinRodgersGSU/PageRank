x = [.2] * 5
x1 = [.2] * 5
c = 0.85
A = [[0, 0, 0, 0.5, 0], 
    [1, 0, 0, 0, 0],
    [0, 0.5, 0, 0, 1],
    [0, 0.5, 1, 0, 0],
    [0, 0, 0, 0.5, 0]]

for b in range(0,1000000):
  for y in range(len(x)):
    sum = 0
    for z in range(len(A[y])):
      sum += c * A[y][z] * x[z]
    x1[y] = sum + (1-c)/5
  for y in range(len(x)):
    x[y] = x1[y]

print(x)
for c in range(len(x)):
  print("Node",c+1,":",x[c])
