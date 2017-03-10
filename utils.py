def check_ip_validity(ipaddr):
    if ipaddr == None or ipaddr.strip() == '':
       return -1
    ret = 0
    addr=ipaddr.strip().split('.')
    if len(addr) != 4:
        ret = -1
    else:
        for i in range(4):
            try:
                addr[i]=int(addr[i])
                if addr[i] > 255 or addr[i] < 0:
                    ret = -1
            except:
                ret = -1
    return ret

def get_subnet(ipaddr):
    if check_ip_validity(ipaddr) != 0:
        return None
    addr=ipaddr.strip().split('.')
    return addr[0]
