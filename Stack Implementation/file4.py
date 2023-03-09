# stack = frist come last serve 

stack = []

while True:
    q = input("Enter 1 to push \n Enter 2 to pop \n Enter 0 to exit")
    if q == '0' :
        break
    elif q == '1' :
        name = input("enter item to push")
        stack.append(name)
    elif q == '2' :
        if len(stack) <= 0 :
            print("stack is empty")
        else:
            x = stack.pop()
            print(f"pop item is {x}")

    else:
        print("invalid input")
    print(stack) 