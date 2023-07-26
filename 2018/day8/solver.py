def count_meta(entries):
    meta_sum = 0
    ip = 0
    m_count_stack = []
    c_count_stack = []
    while ip < len(entries):
        c_count = entries[ip]
        m_count = entries[ip+1]
        ip += 2
        if c_count > 0:
            m_count_stack.append(m_count)
            c_count_stack.append(c_count)
        else:
            meta_sum += sum(entries[ip:ip+m_count])
            ip += m_count
            c_count_stack[-1] -= 1
            while c_count_stack and c_count_stack[-1] == 0:
                c_count_stack.pop()
                p_m_count = m_count_stack.pop()
                meta_sum += sum(entries[ip:ip+p_m_count])
                ip += p_m_count
                if c_count_stack:
                    c_count_stack[-1] -= 1
    return meta_sum

if __name__ == "__main__":
    entries = [int(i) for i in open("input.txt").read().strip().split()]
    print(count_meta(entries))
        
