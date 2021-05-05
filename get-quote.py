import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)
  rnd = random.randint(1,5)
  arr = random.sample(range(0,last),rnd)
  for i in range(len(arr)):
  	print(quotes[arr[i]],end= ' ')

if __name__== "__main__":
  primary()
