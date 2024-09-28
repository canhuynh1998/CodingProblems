def main():
    read = open("mixmilk.in")

    c1, m1 = list(map(int, read.readline().split(" ")))
    c2, m2 = list(map(int, read.readline().split(" ")))
    c3, m3 = list(map(int, read.readline().split(" ")))

    milk_buckets = [m1, m2, m3]
    capacity = [c1, c2, c3]

    count = 0
    for i in range(1, 101):
        current_bucket = i % 3
        previous_bucket = 2 if current_bucket == 0 else current_bucket - 1
        count += 1
        if milk_buckets[previous_bucket] + milk_buckets[current_bucket] >= capacity[current_bucket]:
            milk_buckets[previous_bucket] = milk_buckets[previous_bucket] - ( capacity[current_bucket] - milk_buckets[current_bucket] )
            milk_buckets[current_bucket] = capacity[current_bucket]
        else:
            milk_buckets[current_bucket] += milk_buckets[previous_bucket]
            milk_buckets[previous_bucket] = 0

    with open("mixmilk.out","w+") as f:
        for m in milk_buckets:
            print(m, file=f)


if __name__ == "__main__":
    main()