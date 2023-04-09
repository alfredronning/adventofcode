from hashlib import md5

if __name__ == "__main__":
    secret_key = open("input.txt").read().strip()
    i = 0
    while True:
        h = str(md5((secret_key+str(i)).encode()).hexdigest())
        if h[:6].count("0") == 6:
            print(i)
            break
        i += 1

