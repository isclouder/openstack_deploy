from openstack_deploy.configs import keystone
from openstack_deploy.configs import glance
from openstack_deploy.configs import nova
from openstack_deploy.configs import neutron
from openstack_deploy.configs import cinder
from openstack_deploy.utils import utils

def do_config(configs):
    for cfg in configs:
        parser = utils.Config(cfg['filename'])
        del cfg['filename']
        parser.set(cfg)
        parser.write()

def config_controller():
    do_config(keystone.controller)
    do_config(glance.controller)
    do_config(nova.controller)
    do_config(neutron.controller)
    do_config(cinder.controller)

def config_computer():
    do_config(keystone.computer)
    do_config(glance.computer)
    do_config(nova.computer)
    do_config(neutron.computer)
    do_config(cinder.computer)

