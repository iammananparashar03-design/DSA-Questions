'''
Question 1: Write a dynamic program where the user will choose which operation of a queue is to be followed:
1. Creating a new queue
2. Inserting an element into the queue
3. Removing an element from the queue
4. Display
5. Exit
'''

queue = []
size = 0
created = False

while True:
    print("\n--- Queue Menu ---")
    print("1. Create a new queue")
    print("2. Insert an element")
    print("3. Remove an element")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        size = int(input("Enter size of the queue: "))
        if size <= 0:
            print("Size must be greater than 0")
        else:
            queue = []
            created = True
            print(f"Queue of size {size} created")

    elif choice in ("2", "3", "4") and not created:
        print("Create a queue first (option 1)")

    elif choice == "2":
        if len(queue) == size:
            print("Queue Overflow! Cannot insert")
        else:
            queue.append(int(input("Enter element to insert: ")))
            print("Element inserted")

    elif choice == "3":
        if len(queue) == 0:
            print("Queue Underflow! Cannot remove")
        else:
            print("Removed element:", queue.pop(0))

    elif choice == "4":
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue (front to rear):", *queue)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again")
