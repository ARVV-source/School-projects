#1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
  print(i, end=" ")
print()
#2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
  print(i, end=" ")
#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range (8):
  print("# "*i)
print()

aum = 0
while  aum < 10:
  print("# "*10)
  aum += 1