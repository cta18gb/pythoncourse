x=int(input("EnterSomething"))
for i in range(1,x+1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        i ="Fizz"
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)

