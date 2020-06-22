def readfile(file):
  data = []
  f = open(file, 'r') 
  lines = f.readlines()
  for l in lines:
    line = l.split(" ")
    line[-1] = line[-1].replace("\n", "")
    data.append(line)
  return data

def routes(triangle):
  accTotal = []
  accTotal.append(triangle[0])
  for i in range(1, len(triangle)):
    line = []
    for n in range(0, len(triangle[i])):
      if n == 0:
        line.append(int(triangle[i][n]) + int(accTotal[-1][n]))
      elif n == len(triangle[i]) - 1:
        line.append(int(triangle[i][n]) + int(accTotal[-1][n - 1]))
      else:
        sum1 = int(triangle[i][n]) + int(accTotal[-1][n - 1])
        sum2 = int(triangle[i][n]) + int(accTotal[-1][n])
        best = sum1 if sum1 >= sum2 else sum2
        line.append(best)
    accTotal.append(line)
  return max(accTotal[-1])

triangle = readfile("triangle.txt")
print(routes(triangle))