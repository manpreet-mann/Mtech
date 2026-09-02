def read_matrix():
    n = int(input("Number of samples (rows): "))
    m = int(input("Number of features (columns): "))

    print(f"\nEnter {n} rows, {m} space-separated numbers each:")
    X = []
    i = 0
    while i < n:
        parts = input(f"row {i + 1}: ").split()
        if len(parts) != m:
            print(f"  expected {m} values, got {len(parts)} - try again")
            continue
        try:
            X.append([float(p) for p in parts])
        except ValueError:
            print("  non-numeric value - try again")
            continue
        i += 1
    return X


def covariance_matrix(X, dof=1):
    n = len(X)
    m = len(X[0])
    if n - dof <= 0:
        raise ValueError("not enough samples for the given dof")

    means = [sum(row[j] for row in X) / n for j in range(m)]
    Xc = [[row[j] - means[j] for j in range(m)] for row in X]

    C = [[0.0] * m for _ in range(m)]
    for i in range(m):
        for j in range(i, m):
            s = 0.0
            for k in range(n):
                s += Xc[k][i] * Xc[k][j]
            C[i][j] = C[j][i] = s / (n - dof)
    return C


def show(C):
    for row in C:
        print("  ".join(f"{v:9.4f}" for v in row))


if __name__ == "__main__":
    X = read_matrix()
    d = input("\ndof (1 = sample, 0 = population) [1]: ").strip()
    dof = int(d) if d else 1

    print("\nCovariance matrix:")
    show(covariance_matrix(X, dof))