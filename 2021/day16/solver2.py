def do_operation(subpackets, type_id):
    if type_id == 0:
        return sum(subpackets)
    if type_id == 1:
        m = 1
        for subpacket in subpackets:
            m *= subpacket
        return m
    if type_id == 2:
        return min(subpackets)
    if type_id == 3:
        return max(subpackets)
    if type_id == 5:
        return subpackets[0] > subpackets[1]
    if type_id == 6:
        return subpackets[0] < subpackets[1]
    if type_id == 7:
        return subpackets[0] == subpackets[1]

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
        return int(packet_data, 2), rest
    else:
        subpackets = []
        sizebit, rest = int(rest[0]), rest[1:]
        if sizebit:
            packet_num, rest = int(rest[:11], 2), rest[11:]
            for _ in range(packet_num):
                subpacket, rest = parse_packet(rest)
                subpackets.append(subpacket)
        else:
            packets_size, rest = int(rest[:15], 2), rest[15:]
            tmp_len_rest = len(rest) - packets_size
            while len(rest) > tmp_len_rest:
                subpacket, rest = parse_packet(rest)
                subpackets.append(subpacket)
        return do_operation(subpackets, type_id), rest

if __name__ == "__main__":
    inp_hex = open("input.txt").read().strip()
    bitstring = "{:b}".format(int(inp_hex, 16))
    bitstring = bitstring.zfill(-(-len(bitstring)//8)*8)

    res, rest = parse_packet(bitstring)
    print(res)

