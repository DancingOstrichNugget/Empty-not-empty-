import random
while True:
  empty = random.randint(1, 3)
print(empty)
empty += empty
print(empty)
if empty > 10:
  exit()
  #even this is so slow