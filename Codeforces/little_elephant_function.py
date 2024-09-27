def main():
    n = int(input())

    perms = [i for i in range(1, n+1)]

    sorting(perms, len(perms) - 1)

    print(' '.join(map(str,perms)))

def sorting(perms, idx):
    while idx > 0:
        if perms[idx] == 1:
            continue
        perms[idx - 1], perms[idx] = perms[idx], perms[idx - 1]
        idx -= 1

if __name__ == "__main__":
    main()