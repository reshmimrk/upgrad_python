import ast,sys
input_str = input() #sys.stdin.read()
input_list = ast.literal_eval(input_str)


# Type your code here

output_list = []

for index in range(len(input_list)):
    output_list.append(input_list[index].title())


print(output_list)