# Heap's algorithm
resp: list


def heap_algo(k: int, A: List[int]):
    if k == 1:
        # output(A)
        resp.append(list(A))
    else:
        # Generate permutations with k-th unaltered
        # Initially k = length(A)
        heap_algo(k - 1, A)

        # Generate permutations for k-th swapped with each k-1 initial
        for i in range(k-1):
            # Swap choice dependent on parity of k (even or odd)
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]
            heap_algo(k - 1, A)
