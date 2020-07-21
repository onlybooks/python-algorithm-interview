def bubblesort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


A = [38, 27, 43, 3, 9, 82, 10]
bubblesort(A)
print(A)
