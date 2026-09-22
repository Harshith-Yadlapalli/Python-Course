########### Exception Handling #########

a=10
b='h'
print(a/b) # Zero Division Error
print(a/b) #Type Error

d={'c':6}
print(d['g']) # Key Error

a=int(input())  #10
b=int(input())  #3
try:
    print(a/b) # 3.33333333333
except Exception as e:
    print(e)
else:
    print("No Error") # No Error
finally:
    print("Completed") # Completed

a=int(input())  #10
b=int(input())  # e
try:
    print(a/b) 
except Exception as e:
    print(e)  # ValueError
else:
    print("No Error") 
finally:
    print("Completed")#Completed

####### File Handling #########

f=open("chatgpt.txt","r") # read mode
f=open("chatgpt.txt","w")  # Write mode
f=open("chatgpt.txt","a")  # append mode

f=open("chatgpt.txt",'w')
d="Python Concepts"
f.write(d)