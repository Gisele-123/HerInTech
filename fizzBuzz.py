def fizzBuzz():
    for num in range(1,100):
        if num%3==0:
            print("fizz", end=",")
        elif num%5==0:
            print("buzz", end=",")
        elif num%3 == 0 and num%5 == 0 :
            print ("fizzBuzz", end=",")
        else: print (num, end=",")
fizzBuzz()