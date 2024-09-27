def main():
    guest = input()
    host = input()
    letters = input()

    guest_hosts = {}
    l_counts = {}
    result = ""
    guest_host = guest + host
    for c in guest_host:
        if c not in guest_hosts:
            guest_hosts[c] = 0
        guest_hosts[c] += 1
    for c in letters:
        if c not in l_counts:
            l_counts[c] = 0
        l_counts[c] += 1
    
    for key, value in guest_hosts.items():
        if key not in l_counts or value != l_counts[key]:
            result = "NO"
            break
        del l_counts[key]
    if len(l_counts) != 0:
        result = "NO"

    if result == "NO":
        print(result)
    else:
        print("YES")


if __name__ == "__main__":
    main()