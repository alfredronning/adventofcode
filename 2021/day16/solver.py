def parse_packet(bits):
    version, type_id, rest = int(bits[:3], 2), int(bits[3:6], 2), bits[6:]
    if type_id == 4:
        packet_data = ""
        next_block, rest = rest[:5], rest[5:]
        while next_block:
            startbit, blockdata = next_block[0], next_block[1:]
            packet_data += blockdata
            if startbit == "0":
                break
            next_block, rest = rest[:5], rest[5:]
        return version, rest
    else:
        total = version
        sizebit, rest = int(rest[0]), rest[1:]
        if sizebit:
            packet_num, rest = int(rest[:11], 2), rest[11:]
            for _ in range(packet_num):
                subpacket, rest = parse_packet(rest)
                total += subpacket
        else:
            packets_size, rest = int(rest[:15], 2), rest[15:]
            tmp_len_rest = len(rest) - packets_size
            while len(rest) > tmp_len_rest:
                subpacket, rest = parse_packet(rest)
                total += subpacket
        return total, rest

if __name__ == "__main__":
    inp_hex = open("input.txt").read().strip()
    bitstring = "{:b}".format(int(inp_hex, 16))
    bitstring = bitstring.zfill(-(-len(bitstring)//8)*8)

    res, rest = parse_packet(bitstring)
    print(res)

