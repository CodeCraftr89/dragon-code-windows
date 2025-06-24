def add(x,y) :
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

def div(x,y):
    if y==0:
        return "can not divide"
    return x/y

print("dragon calculator")
print("select operation : ")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice =input("Enter chose (1/2/3/4) : ")

num1 = float(input("Enter first number : "))
num2 = float(input("Enter first number : "))

if(choice=='1'):
    print(f"Result:{add(num1,num2)}")
elif(choice=='2'):
    print(f"Result: {sub(num1,num2)}")
elif(choice=='3'):
    print(f"Result: {multi(num1,num2)}")
elif(choice=='4'):
    print(f"Result: {div(num1,num2)}")
else:
    print("invalid Input")


    
