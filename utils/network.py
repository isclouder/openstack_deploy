
import netifaces

def get_address(ifname):
    try:
        return netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['addr']
    except Exception as e:
        print("Get address error: %s" % e)
        return None

def get_gateway(ifname):
    try:
        for iface in netifaces.gateways()[netifaces.AF_INET]:
            if iface[1] == ifname:
                return iface[0]
    except Exception as e:
        print("Get gateway error: %s" % e)
        return None

    return None

def get_netmask(ifname):
    try:
        return netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['netmask']
    except Exception as e:
        print("Get netmask error: %s" % e)
        return None

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

def set_hosts(address, hostname):
    file1 = open('/etc/hosts', 'r')
    lines = file1.readlines()
    file2 = open('/etc/hosts', 'w')
    find_flag = False
    for line in lines:
        if (line.find(' ' + hostname) != -1 or line.find('\t' + hostname) != -1) and line.strip().endswith(hostname):
            find_flag = True

    if find_flag == True:
        write_flag = False
        for line in lines:
            if (line.find(' '+hostname) != -1 or line.find('\t' + hostname) != -1) and line.strip().endswith(hostname):
                if write_flag == False:
                    file2.writelines('%s    %s\n' % (address, hostname))
                    write_flag = True
            else:
                file2.writelines(line)
    else:
        file2.writelines('%s    %s\n' % (address, hostname))
        for line in lines:
            file2.writelines(line)

    file1.close()
    file2.close()

def set_ip_address_ubuntu(ifname, proto, address, netmask, gateway):
    file1 = open('/etc/network/interfaces', 'r')
    file2 = open('/etc/network/interfaces', 'w')
    lines = file1.readlines()
    flag = False
    config = False
    for line in lines:
        if line.find('iface') != -1 and (line.find(' '+ifname+' ') != -1 or line.find('\t'+ifname+'\t') != -1 or line.find(' '+ifname+'\t') != -1 or line.find('\t'+ifname+' ') != -1):
            file2.writelines('iface %s inet %s\n' % (ifname, proto))
            if proto == 'static':
                file2.writelines('        address %s\n' % address)
                file2.writelines('        netmask %s\n' % netmask)
                file2.writelines('        gateway %s\n' % gateway)
            flag = True
            config = True
        elif flag == True and line.startswith('auto '):
            flag=False

        if flag:
            if line.find('iface') != -1 or line.find('address') != -1 or line.find('netmask') != -1 or line.find('gateway') != -1 or line.find('pre-up') != -1:
                pass
            else:
                file2.writelines(line)
        else:
            file2.writelines(line)

    if config == False:
        file2.writelines('auto %s\n' % ifname)
        file2.writelines('iface %s inet %s\n' % (ifname, proto))
        file2.writelines('        address %s\n' % address)
        file2.writelines('        netmask %s\n' % netmask)
        file2.writelines('        gateway %s\n' % gateway)

    file1.close()
    file2.close()

