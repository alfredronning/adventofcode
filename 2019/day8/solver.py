if __name__ == "__main__":
    inp = open("input.txt").read().strip()
    layer_size = 25*6
    layers = [inp[layer_size*i:layer_size*(i+1)] for i in range(len(inp)//layer_size)]
    fewest_zeros = 0
    fewest_zero_count = float("inf")
    for i in range(len(layers)):
        current_count = layers[i].count("0")
        if current_count < fewest_zero_count:
            fewest_zero_count = current_count
            fewest_zeros = i
    fewest_zeros_layer = layers[fewest_zeros]
    res = fewest_zeros_layer.count("1") * fewest_zeros_layer.count("2")
    print(res)

