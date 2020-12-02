my_stack = []

x=input("Enter1 for stack:")
y=input("Enter2 for stack:")
z=input("Enter3 for stack:")

my_stack.append(x)
my_stack.append(y)
my_stack.append(z)

print(my_stack)

print('\nElements popped from my_stack:')
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

print('\nmy_stack after elements are popped:')
print(my_stack)

queue = []

a=input("Enter1 for queue:")
b=input("Enter2 for queue:")
c=input("Enter3 for queue:")

queue.append(a)
queue.append(b)
queue.append(c)

print("Initial queue")
print(queue)

print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)


