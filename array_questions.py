'''
Question 1. Insert a new element in the array.
Question 2: Delete an element from an array. 
Question 3. Find the product of two matrices.
Question 4. Sum of diagonal and non-diagonal elements in a matrix.
Question 5. Enter marks of five students for three subjects each and find the percentage of students.

'''
# Question 1:
arr = list(map(int, input("Enter array elements: ").split()))
pos = int(input(f"Enter position (0 to {len(arr)}): "))
val = int(input("Enter element to insert: "))

if 0 <= pos <= len(arr):
    arr.insert(pos, val)
    print("Updated array:", arr)
else:
    print("Invalid position")

# Question 2:
arr = list(map(int, input("Enter array elements: ").split()))
pos = int(input(f"Enter position to delete (0 to {len(arr) - 1}): "))

if 0 <= pos < len(arr):
    removed = arr.pop(pos)
    print(f"Deleted {removed}. Updated array:", arr)
else:
    print("Invalid position")

# Question 3:
r1, c1 = map(int, input("Rows and columns of matrix A: ").split())
r2, c2 = map(int, input("Rows and columns of matrix B: ").split())

if c1 != r2:
    print("Multiplication not possible (columns of A must equal rows of B)")
else:
    print("Enter matrix A:")
    A = [list(map(int, input().split())) for _ in range(r1)]
    print("Enter matrix B:")
    B = [list(map(int, input().split())) for _ in range(r2)]

    C = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    print("Product:")
    for row in C:
        print(*row)

# Question 4:
n = int(input("Enter order of square matrix: "))
print("Enter matrix:")
M = [list(map(int, input().split())) for _ in range(n)]

diag = non_diag = 0
for i in range(n):
    for j in range(n):
        if i == j:
            diag += M[i][j]
        else:
            non_diag += M[i][j]

print("Sum of diagonal elements:", diag)
print("Sum of non-diagonal elements:", non_diag)

# Question 5:
for s in range(1, 6):
    print(f"\nStudent {s}")
    total = 0
    for sub in range(1, 4):
        total += float(input(f"Marks in subject {sub}: "))
    percentage = total / 300 * 100
    print(f"Percentage: {percentage:.2f}%")