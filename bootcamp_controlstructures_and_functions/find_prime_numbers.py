import ast
num_list = ast.literal_eval(input())

for n in num_list:
    i = 2
    flag = True
    while i < n:
        if (n%i == 0):
            print(f"{n} is not Prime")
            flag = False
            break
        
        i+=1
    if flag == True:
        print(f"{n} is a prime number")
