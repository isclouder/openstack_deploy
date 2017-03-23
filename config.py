
import utils
import os

CONTROLLER_HOSTNAME='controller'
PROVIDER_INTERFACE_NAME = 'eth1'

ADMIN_PASS='123456'
MYSQL_PASS='123456'
GLANCE_PASS = '123456'
NOVA_PASS = '123456'
NEUTRON_PASS = '123456'
CINDER_PASS = '123456'

KEYSTONE_DBPASS = '123456'
GLANCE_DBPASS = '123456'
NOVAAPI_DBPASS = '123456'
NOVA_DBPASS = '123456'
NEUTRON_DBPASS = '123456'
CINDER_DBPASS = '123456'

RABBIT_PASS= '123456'
METADATA_SECRET = '123456'

config_2_neutron = \
    {
     "filename":"/etc/neutron/neutron.conf",
     "database":{
        "connection": "mysql+pymysql://neutron:%s@%s/neutron" %(NEUTRON_DBPASS, CONTROLLER_HOSTNAME)
        },
     "DEFAULT":{
        "transport_url": "rabbit://openstack:%s@%s" % (RABBIT_PASS, CONTROLLER_HOSTNAME),
        "auth_strategy": "keystone",
        "core_plugin": "ml2",
        "service_plugins": "",
        "allow_overlapping_ips":"false",
        "notify_nova_on_port_status_changes": "True",
        "notify_nova_on_port_data_changes": "True"
        },
     "keystone_authtoken":{
        "auth_uri": "http://%s:5000" % CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % CONTROLLER_HOSTNAME,
        "memcached_servers": "%s:11211" % CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "project_name": "service",
        "username": "neutron",
        "password": NEUTRON_PASS
        },
     "nova":{
        "auth_url": "http://%s:35357" % CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "region_name": "RegionOne",
        "project_name": "service",
        "username": "nova",
        "password": NOVA_PASS
        }
     }

config_3_neutron = \
    {
     "filename":"/etc/neutron/neutron.conf",
     "database":{
        "connection": "mysql+pymysql://neutron:%s@%s/neutron" %(NEUTRON_DBPASS, CONTROLLER_HOSTNAME)
        },
     "DEFAULT":{
        "transport_url": "rabbit://openstack:%s@%s" % (RABBIT_PASS, CONTROLLER_HOSTNAME),
        "auth_strategy": "keystone",
        "core_plugin": "ml2",
        "service_plugins": "router",
        "allow_overlapping_ips":"true",
        "notify_nova_on_port_status_changes": "True",
        "notify_nova_on_port_data_changes": "True"
        },
     "keystone_authtoken":{
        "auth_uri": "http://%s:5000" % CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % CONTROLLER_HOSTNAME,
        "memcached_servers": "%s:11211" % CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "project_name": "service",
        "username": "neutron",
        "password": NEUTRON_PASS
        },
     "nova":{
        "auth_url": "http://%s:35357" % CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "region_name": "RegionOne",
        "project_name": "service",
        "username": "nova",
        "password": NOVA_PASS
        }
     }

config_2_ml2_conf = \
    {
     "filename":"/etc/neutron/plugins/ml2/ml2_conf.ini",
     "ml2": {
        "type_drivers": "flat,vlan",
        "tenant_network_types": "",
        "mechanism_drivers": "linuxbridge",
        "extension_drivers": "port_security"
        },
     "ml2_type_flat":{
        "flat_networks": "provider"
        },
     "securitygroup":{
        "enable_ipset": "True"
        }
     }

config_3_ml2_conf = \
    {
     "filename":"/etc/neutron/plugins/ml2/ml2_conf.ini",
     "ml2":{
        "type_drivers": "flat,vlan",
        "tenant_network_types": "vlan",
        "mechanism_drivers": "linuxbridge,l2population",
        "extension_drivers": "port_security"
        },
     "ml2_type_flat":{
        "flat_networks": "provider01,provider02"
        },
     "ml2_type_vlan":{
        "network_vlan_ranges": "provider02:101:200"
        },
     "securitygroup":{
        "enable_ipset": "True"
        }
     }

config_2_linuxbridge_agent = \
    {
     "filename":"/etc/neutron/plugins/ml2/linuxbridge_agent.ini",
     "linux_bridge":{
        "physical_interface_mappings": "provider:%s" % PROVIDER_INTERFACE_NAME
        },
     "vxlan":{
        "enable_vxlan": "False"
        },
     "securitygroup":{
        "enable_security_group": "True",
        "firewall_driver": "neutron.agent.linux.iptables_firewall." +
                           "IptablesFirewallDriver"
        }
     }

config_3_linuxbridge_agent = \
    {
     "filename":"/etc/neutron/plugins/ml2/linuxbridge_agent.ini",
     "linux_bridge":{
        "physical_interface_mappings": "provider01:%s,provider02:%s" % (PROVIDER_INTERFACE_NAME,PROVIDER_INTERFACE_NAME)
        },
     "vxlan":{
        "enable_vxlan": "False"
        },
     "securitygroup":{
        "enable_security_group": "True",
        "firewall_driver": "neutron.agent.linux.iptables_firewall." +
                           "IptablesFirewallDriver"
        }
     }

config_23_dhcp_agent = \
    {
     "filename":"/etc/neutron/dhcp_agent.ini",
     "DEFAULT":{
        "interface_driver": "neutron.agent.linux.interface." +
                            "BridgeInterfaceDriver",
        "dhcp_driver": "neutron.agent.linux.dhcp.Dnsmasq",
        "enable_isolated_metadata": "True"
        }
    }

config_23_metadata_agent = \
    {
     "filename":"/etc/neutron/metadata_agent.ini",
     "DEFAULT":{
        "nova_metadata_ip": CONTROLLER_HOSTNAME,
        "metadata_proxy_shared_secret": METADATA_SECRET
        }
    }

config_3_l3_agent = \
    {
     "filename":"/etc/neutron/l3_agent.ini",
     "DEFAULT":{
        "interface_driver": "neutron.agent.linux.interface.BridgeInterfaceDriver"
        },
    }

configs_2 = [config_2_neutron, config_2_ml2_conf, config_2_linuxbridge_agent, config_23_dhcp_agent, config_23_metadata_agent]
configs_3 = [config_3_neutron, config_3_ml2_conf, config_3_linuxbridge_agent, config_23_dhcp_agent, config_23_metadata_agent, config_3_l3_agent]

def do_config(configs):
    for cfg in configs:
        parser = utils.Config(cfg['filename'])
        del cfg['filename']
        parser.set(cfg)
        parser.write()

