#Print reverse of a list
lst = [1, 2, 3, 4, 5]

#Method 1: Using slicing
reversed_lst = lst[::-1]
print("Reversed list using slicing:", reversed_lst)

#Method 2: Using the built-in reversed() function
reversed_lst = list(reversed(lst))
print("Reversed list using reversed() function:", reversed_lst)

#Method 3: Using a for loop
lst = [10,20,30,40,50]
for i in range(len(lst)-1, -1, -1):
    print("Reversed list using for loop:", lst)


