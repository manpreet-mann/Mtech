def read_matrix():
    n = int(input("Matrix size n (n x n): "))
    print(f"\nEnter {n} rows, {n} space-separated numbers each:")
    A = []
    i = 0
    while i < n:
        parts = input(f"row {i + 1}: ").split()
        if len(parts) != n:
            print(f"  expected {n} values, got {len(parts)} - try again")
            continue
        try:
            A.append([float(p) for p in parts])
        except ValueError:
            print("  non-numeric value - try again")
            continue
        i += 1
    return A


def inverse(A, tol=1e-12):
    n = len(A)
    M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)]
         for i, row in enumerate(A)]

    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[piv][col]) < tol:
            raise ValueError("matrix is singular, no inverse exists")
        M[col], M[piv] = M[piv], M[col]

        d = M[col][col]
        M[col] = [x / d for x in M[col]]

        for r in range(n):
            if r != col and M[r][col] != 0.0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]

    return [row[n:] for row in M]


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)]
            for i in range(n)]


def show(M):
    for row in M:
        print("  ".join(f"{v:10.6f}" for v in row))


if __name__ == "__main__":
    A = read_matrix()
    Ai = inverse(A)

    print("\nInverse:")
    show(Ai)

    print("\nCheck A x A_inv (should be identity):")
    show(matmul(A, Ai))