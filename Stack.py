stack =[]

def provide_values():
    Data_input = input("Provide values input: ")
    return Data_input

def stack_up(data):
    stack.append(data)
    print ("Data in Stack: ",stack)

def stack_down():
    stack.pop()
    print ("Data Removed from Stack: ",stack)

# setting stack size as 5
for i in range(5): 
    input_data = provide_values()
    stack_up(input_data)

# removing items from stack
for i in range(2): 
    stack_down()

