import common

config_2_neutron = \
    {
     "filename":"/etc/neutron/neutron.conf",
     "database":{
        "connection": "mysql+pymysql://neutron:%s@%s/neutron" %(common.NEUTRON_DBPASS, common.CONTROLLER_HOSTNAME)
        },
     "DEFAULT":{
        "transport_url": "rabbit://openstack:%s@%s" % (common.RABBIT_PASS, common.CONTROLLER_HOSTNAME),
        "auth_strategy": "keystone",
        "core_plugin": "ml2",
        "service_plugins": "",
        "allow_overlapping_ips":"false",
        "notify_nova_on_port_status_changes": "True",
        "notify_nova_on_port_data_changes": "True"
        },
     "keystone_authtoken":{
        "auth_uri": "http://%s:5000" % common.CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "memcached_servers": "%s:11211" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "project_name": "service",
        "username": "neutron",
        "password": common.NEUTRON_PASS
        },
     "nova":{
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "region_name": "RegionOne",
        "project_name": "service",
        "username": "nova",
        "password": common.NOVA_PASS
        }
     }

config_3_neutron = \
    {
     "filename":"/etc/neutron/neutron.conf",
     "database":{
        "connection": "mysql+pymysql://neutron:%s@%s/neutron" %(common.NEUTRON_DBPASS, common.CONTROLLER_HOSTNAME)
        },
     "DEFAULT":{
        "transport_url": "rabbit://openstack:%s@%s" % (common.RABBIT_PASS, common.CONTROLLER_HOSTNAME),
        "auth_strategy": "keystone",
        "core_plugin": "ml2",
        "service_plugins": "router",
        "allow_overlapping_ips":"true",
        "notify_nova_on_port_status_changes": "True",
        "notify_nova_on_port_data_changes": "True"
        },
     "keystone_authtoken":{
        "auth_uri": "http://%s:5000" % common.CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "memcached_servers": "%s:11211" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "project_name": "service",
        "username": "neutron",
        "password": common.NEUTRON_PASS
        },
     "nova":{
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "region_name": "RegionOne",
        "project_name": "service",
        "username": "nova",
        "password": common.NOVA_PASS
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
        "physical_interface_mappings": "provider:%s" % common.PROVIDER_INTERFACE_NAME
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
        "physical_interface_mappings": "provider01:%s,provider02:%s" % (common.PROVIDER_INTERFACE_NAME,common.PROVIDER_INTERFACE_NAME)
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
        "nova_metadata_ip": common.CONTROLLER_HOSTNAME,
        "metadata_proxy_shared_secret": common.METADATA_SECRET
        }
    }

config_3_l3_agent = \
    {
     "filename":"/etc/neutron/l3_agent.ini",
     "DEFAULT":{
        "interface_driver": "neutron.agent.linux.interface.BridgeInterfaceDriver"
        },
    }

#controller = [config_2_neutron, config_2_ml2_conf, config_2_linuxbridge_agent, config_23_dhcp_agent, config_23_metadata_agent]
controller = [config_3_neutron, config_3_ml2_conf, config_3_linuxbridge_agent, config_23_dhcp_agent, config_23_metadata_agent, config_3_l3_agent]
computer = controller

