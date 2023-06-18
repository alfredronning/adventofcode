import hashlib

if __name__ == "__main__":
    inp = "ugkcyxxp"

    password = ""
    i = 0
    while len(password) < 8:
        h = hashlib.md5((inp+str(i)).encode()).hexdigest()
        if h[:5] == "00000":
            password += h[5]
            print(inp + str(i))
            print(password)
        i += 1


