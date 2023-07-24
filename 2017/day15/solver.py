if __name__ == "__main__":
    val_a = 634
    val_b = 301

    fac_a = 16807
    fac_b = 48271
    m = 2147483647

    count = 0
    for _ in range(40_000_000):
        val_a = (val_a*fac_a)%m
        val_b = (val_b*fac_b)%m

        if (val_a^val_b)&0xffff == 0:
            count += 1
    print(count)

