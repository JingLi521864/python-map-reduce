import sys 


# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split("    ")
  if (len(datalist) == 6) : 
    store, amount = datalist

    # print intermediate key-value pairs to standard output
    print(amount + "\t" + store + "\n")

