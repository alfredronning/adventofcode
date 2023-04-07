if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    width = 25
    height = 6
    layer_size = width*height
    layers = [inp[layer_size*i:layer_size*(i+1)] for i in range(len(inp)//layer_size)]
    fewest_zeros = 0
    fewest_zero_count = float("inf")
    end_img = [None]*layer_size
    for layer in layers:
        for i in range(len(layer)):
            if end_img[i] is not None or layer[i] == "2":
                continue
            end_img[i] = "*" if layer[i] == "1" else " "
    img = "\n".join(["".join(end_img[width*i:width*(i+1)]) for i in range(height)])
    print(img)

