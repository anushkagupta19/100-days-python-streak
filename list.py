# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed
#  by  lines of commands where each command will be of the
#   types listed above. Iterate through each command in order 
# and perform the corresponding operation on your list.

if __name__ == '__main__':
    # Read the number of commands
    N = int(input())
    
    # Initialize an empty list
    my_list = []
    
    # Loop N times to process each command
    for _ in range(N):
        # Read the full command line and split it into words
        # e.g., "insert 0 5" becomes ['insert', '0', '5']
        command_parts = input().split()
        
        # The first part is always the command name
        command = command_parts[0]
        
        # Use if/elif to execute the correct list operation
        if command == "insert":
            # 'insert' takes two integer arguments: position and value
            position = int(command_parts[1])
            value = int(command_parts[2])
            my_list.insert(position, value)
            
        elif command == "print":
            print(my_list)
            
        elif command == "remove":
            # 'remove' takes one integer argument: the value to remove
            value = int(command_parts[1])
            my_list.remove(value)
            
        elif command == "append":
            # 'append' takes one integer argument: the value to add
            value = int(command_parts[1])
            my_list.append(value)
            
        elif command == "sort":
            my_list.sort()
            
        elif command == "pop":
            my_list.pop()
            
        elif command == "reverse":
            my_list.reverse()