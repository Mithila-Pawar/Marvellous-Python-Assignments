def power(N, P):

    if P == 0:
        return 1

    return (N*power(N, P-1))

if __name__ == "__main__":
    N = 5
    P = 2

    print(power(N, P))