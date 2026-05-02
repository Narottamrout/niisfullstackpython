# MAX=5
# queue=[0]*MAX
# front,rear=-1,-1
# def enqueue():
# 	global rear,front
# 	if rear==MAX-1:
# 		print("queue overflow")
# 	else:
# 		item=int(input("enter element to insert"))
# 		if front==-1:
# 			front=0
# 		rear=rear+1
# 		queue[rear]=item
# 		print(item,"insert into queue")	
# def dequeue():
# 	global rear,front
# 	if front==-1:
# 		print("stack underflow")
# 	else:
# 		item=queue[front]
# 		print(item,"delete from the queue")
# Queue Program in Python (Without OOP)
MAX = 5
queue = [0] * MAX
front,rear = -1,-1
def enqueue():
    global rear,front
    if rear == MAX - 1:
        print("Q Overflow")
    else:
        item = int(input("Enter element to insert: "))
        if front==-1:
            front=0
        rear=rear+1
        queue[rear] = item
        print(item, "insert into queue")
def dequeue():
    global rear,front
    if front == -1:
        print("Q Underflow")
    else:
        item = queue[front]
        print(item, "delete from queue")
        if front==rear:
            front=-1
            rear=-1
            return 
        front = front +1
def peek():
    if front == -1:
        print("Q is Empty")
    else:
        print("Top element is:", queue[front])

def display():
    if front == -1:
        print("Q is Empty")
    else:
        print("Q elements are:")
        for i in range(front, rear+1, 1):
            print(queue[i])
while True:
    print("\n--- queue MENU ---")
    print("1. insert")
    print("2. delete")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()
    elif choice == 5:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
