import hashlib

if __name__ == "__main__":
    inp = "ugkcyxxp"

    password = ["#"]*8
    i = 0
    while "#" in password:
        h = hashlib.md5((inp+str(i)).encode()).hexdigest()
        if h[:5] == "00000" and h[5] < "8" and password[int(h[5])] == "#":
            password[int(h[5])] = h[6]
            print(inp + str(i))
            print(password)
        i += 1
    print("".join(password))


