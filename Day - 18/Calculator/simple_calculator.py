import addition,subtraction,multiplication,division
#add2 = addition.addition_2positional(10,20)
x = int(input())
y = int(input())
unlimited = list(map(int,input().split()))

print("addition of 2 values: ", addition.addition_2positional(x,y))
print("addition of so many value :",addition.addition_unlimited(unlimited))
# print(subtraction.subtraction(110,900))