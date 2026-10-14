'''
Question 1: Write a A dynamic program for stack operations where the user can dynamically choose which operations to select.
 the following are the options that need to be put forward:
1. Create a stack
2. Push the element into a stack
3. Pop an element
4. Display an element
5. Overflow condition
6. Underflow condition
7. Exit

'''

stack = []
size = 0
created = False

def is_full():
    return len(stack) == size

def is_empty():
    return len(stack) == 0

while True:
    print("\n--- Stack Menu ---")
    print("1. Create a stack")
    print("2. Push an element")
    print("3. Pop an element")
    print("4. Display the stack")
    print("5. Overflow condition")
    print("6. Underflow condition")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        size = int(input("Enter size of the stack: "))
        if size <= 0:
            print("Size must be greater than 0")
        else:
            stack = []
            created = True
            print(f"Stack of size {size} created")

    elif choice in ("2", "3", "4", "5", "6") and not created:
        print("Create a stack first (option 1)")

    elif choice == "2":
        if is_full():
            print("Stack Overflow! Cannot push")
        else:
            stack.append(int(input("Enter element to push: ")))
            print("Element pushed")

    elif choice == "3":
        if is_empty():
            print("Stack Underflow! Cannot pop")
        else:
            print("Popped element:", stack.pop())

    elif choice == "4":
        if is_empty():
            print("Stack is empty")
        else:
            print("Stack (top to bottom):")
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i])

    elif choice == "5":
        if is_full():
            print("Overflow condition: stack is FULL")
        else:
            print(f"No overflow: {size - len(stack)} space(s) left")

    elif choice == "6":
        if is_empty():
            print("Underflow condition: stack is EMPTY")
        else:
            print(f"No underflow: {len(stack)} element(s) in stack")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again")