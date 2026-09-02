import math


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

    for i in range(n):
        for j in range(n):
            if abs(A[i][j] - A[j][i]) > 1e-9:
                raise ValueError("matrix is not symmetric")
    return A


def jacobi_eigen(A, tol=1e-10, max_sweeps=100):
    n = len(A)
    A = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for _ in range(max_sweeps):
        off = sum(A[i][j] ** 2 for i in range(n) for j in range(i + 1, n))
        if math.sqrt(off) < tol:
            break

        for p in range(n):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-15:
                    continue

                theta = (A[q][q] - A[p][p]) / (2.0 * A[p][q])
                sign = 1.0 if theta >= 0 else -1.0
                t = sign / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c

                app, aqq, apq = A[p][p], A[q][q], A[p][q]
                A[p][p] = app - t * apq
                A[q][q] = aqq + t * apq
                A[p][q] = A[q][p] = 0.0

                for r in range(n):
                    if r != p and r != q:
                        arp, arq = A[r][p], A[r][q]
                        A[r][p] = A[p][r] = c * arp - s * arq
                        A[r][q] = A[q][r] = c * arq + s * arp

                for r in range(n):
                    vrp, vrq = V[r][p], V[r][q]
                    V[r][p] = c * vrp - s * vrq
                    V[r][q] = c * vrq + s * vrp

    vals = [A[i][i] for i in range(n)]
    vecs = [[V[r][c] for r in range(n)] for c in range(n)]
    order = sorted(zip(vals, vecs), key=lambda pair: -pair[0])
    return [p[0] for p in order], [p[1] for p in order]


def verify(A, lam, v):
    n = len(A)
    Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
    return Av, [lam * x for x in v]


if __name__ == "__main__":
    A = read_matrix()
    vals, vecs = jacobi_eigen(A)

    print("\nEigenvalues and eigenvectors (descending):")
    for k, (lam, v) in enumerate(zip(vals, vecs), 1):
        print(f"\nlambda_{k} = {lam:.6f}")
        print("  vector  =", "  ".join(f"{x:9.6f}" for x in v))
        Av, lv = verify(A, lam, v)
        print("  Av      =", "  ".join(f"{x:9.6f}" for x in Av))
        print("  lambda*v=", "  ".join(f"{x:9.6f}" for x in lv))