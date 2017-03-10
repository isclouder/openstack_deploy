import ConfigParser
import utils

def change_manage_ip(address):
    cfile = "/etc/nova/nova.conf"
    conf = ConfigParser.ConfigParser()
    conf.read(cfile)
    conf.set("DEFAULT", "my_ip", address)
    conf.write(open(cfile, "w"))

    cfile = "/etc/cinder/cinder.conf"
    conf = ConfigParser.ConfigParser()
    conf.read(cfile)
    conf.set("DEFAULT", "my_ip", address)
    conf.write(open(cfile, "w"))

    cfile = "/etc/neutron/plugins/ml2/linuxbridge_agent.ini"
    conf = ConfigParser.ConfigParser()
    conf.read(cfile)
    conf.set("vxlan", "local_ip", address)
    conf.write(open(cfile, "w"))

    cfile = "/etc/mysql/mariadb.conf.d/99-openstack.cnf"
    file1 = open(cfile, "r")
    lines = file1.readlines()
    file2 = open(cfile, "w")
    find = False
    for line in lines:
        if line.find('bind-address') != -1 and not line.strip().startswith('#'):
            file2.writelines('bind-address = %s\n' % address)
            find = True
        else:
            file2.writelines(line)
    if not find:
        file2.writelines('bind-address = %s\n' % address)
    file1.close()
    file2.close()

    cfile = "/etc/memcached.conf"
    file1 = open(cfile, "r")
    lines = file1.readlines()
    file2 = open(cfile, "w")
    for line in lines:
        if line.find('-l') != -1 and not line.strip().startswith('#'):
            file2.writelines('-l %s\n' % address)
        else:
            file2.writelines(line)
    file1.close()
    file2.close()

    file = open("/etc/chrony/chrony.conf", "a")
    file.writelines('allow %s.0.0.0/24\n' % utils.get_subnet(address))
    file.close()

