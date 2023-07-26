def count_meta(entries):
    ip = 0
    m_count_stack = []
    c_count_stack = []
    parent_stack = []
    value_dict = {}
    c_dict = {}
    while ip < len(entries):
        c_count = entries[ip]
        m_count = entries[ip+1]
        ip += 2
        if c_count > 0:
            m_count_stack.append(m_count)
            c_count_stack.append(c_count)
            if ip > 2:
                if parent_stack[-1] in c_dict:
                    c_dict[parent_stack[-1]].append(ip-2)
                else:
                    c_dict[parent_stack[-1]] = [ip-2]
            parent_stack.append(ip-2)
        else:
            val = sum(entries[ip:ip+m_count])
            value_dict[ip-2] = val
            if parent_stack[-1] in c_dict:
                c_dict[parent_stack[-1]].append(ip-2)
            else:
                c_dict[parent_stack[-1]] = [ip-2]
            ip += m_count
            c_count_stack[-1] -= 1
            while c_count_stack and c_count_stack[-1] == 0:
                c_count_stack.pop()
                p_m_count = m_count_stack.pop()
                p_ip = parent_stack.pop()

                c = c_dict[p_ip]
                val = 0
                for i in entries[ip:ip+p_m_count]:
                    if i-1 < len(c):
                        val += value_dict[c[i-1]]
                value_dict[p_ip] = val

                ip += p_m_count
                if c_count_stack:
                    c_count_stack[-1] -= 1
    return value_dict

if __name__ == "__main__":
    entries = [int(i) for i in open("input.txt").read().strip().split()]
    print(count_meta(entries)[0])
        
