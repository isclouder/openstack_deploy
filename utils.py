import os
import ConfigParser

class Config(object):
    def __init__(self, filename):
        self.file = filename
        self.parser = ConfigParser.ConfigParser()
        if not os.path.exists(self.file):
            open(self.file, 'w').close()
        self.parser.read(self.file)

    def set(self, contents):
        for section, options in contents.items():
            for option, value in options.items():
                self.parser.set(section, option, value)

    def write(self):
        self.parser.write(open(self.file, "w"))

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
