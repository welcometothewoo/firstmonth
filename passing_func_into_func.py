def total_bill(func, total):
    total = func(total)
    print("Total: " + str(total))

#def gst(num):
 #   total = num * 1.06
  #  return total


gst = lambda num: num * 1.06
