import common

controller_nova = {
    "filename":"/etc/nova/nova.conf",
    "api_database": {
        "connection": "mysql+pymysql://nova:%s@%s/nova_api" %(common.NOVAAPI_DBPASS, common.CONTROLLER_HOSTNAME)
    },
    "database": {
        "connection": "mysql+pymysql://nova:%s@%s/nova" %(common.NOVA_DBPASS, common.CONTROLLER_HOSTNAME)
    },
    "DEFAULT": {
        "transport_url": "rabbit://openstack:%s@%s" % (common.RABBIT_PASS, common.CONTROLLER_HOSTNAME),
        "auth_strategy": "keystone",
        "my_ip": "",
        "use_neutron": "True",
        "firewall_driver": "nova.virt.firewall.NoopFirewallDriver"
    },
    "keystone_authtoken": {
        "auth_uri": "http://%s:5000" % common.CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "memcached_servers": "%s:11211" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "project_name": "service",
        "username": "nova",
        "password": common.NOVA_PASS
    },
    "vnc": {
        "vncserver_listen": "$my_ip",
        "vncserver_proxyclient_address": "$my_ip"
    },
    "oslo_concurrency": {
        "lock_path": "/var/lib/nova/tmp"
    },
    "glance": {
        "api_servers": "http://%s:9292" % common.CONTROLLER_HOSTNAME
    },
    "cinder": {
        "os_region_name": "RegionOne"
    },
    "neutron": {
        "url": "http://%s:9696" % common.CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "region_name": "RegionOne",
        "project_name": "service",
        "username": "neutron",
        "password": common.NEUTRON_PASS,
        "service_metadata_proxy": "True",
        "metadata_proxy_shared_secret": common.METADATA_SECRET
    }
}

computer_nova = {
    "filename":"/etc/nova/nova.conf",
    "DEFAULT": {
        "transport_url": "rabbit://openstack:%s@%s" % (common.RABBIT_PASS, common.CONTROLLER_HOSTNAME),
        "auth_strategy": "keystone",
        "my_ip": "",
        "use_neutron": "True",
        "firewall_driver": "nova.virt.firewall.NoopFirewallDriver"
    },
    "keystone_authtoken": {
        "auth_uri": "http://%s:5000" % common.CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "memcached_servers": "%s:11211" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "project_name": "service",
        "username": "nova",
        "password": common.NOVA_PASS
    },
    "vnc": {
        "enabled": "True",
        "vncserver_listen": "0.0.0.0",
        "vncserver_proxyclient_address": "$my_ip",
        "novncproxy_base_url": "http://%s:6080/vnc_auto.html" % common.CONTROLLER_HOSTNAME
    },
    "oslo_concurrency": {
        "lock_path": "/var/lib/nova/tmp"
    },
    "glance": {
        "api_servers": "http://%s:9292" % common.CONTROLLER_HOSTNAME
    },
    "neutron": {
        "url": "http://%s:9696" % common.CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "region_name": "RegionOne",
        "project_name": "service",
        "username": "neutron",
        "password": common.NEUTRON_PASS
    }
}

computer_nova_compute = {
    "filename":"/etc/nova/nova-compute.conf",
    "libvirt": {
        "images_type": "rbd",
        "images_rbd_pool": "images",
        "images_rbd_ceph_conf": "/etc/ceph/ceph.conf",
        "disk_cachemodes": "\"network=writeback\"",
        "inject_password": "false",
        "inject_key": "false",
        "inject_partition": "-2",
        "live_migration_flag": "\"VIR_MIGRATE_UNDEFINE_SOURCE," +
                               "VIR_MIGRATE_PEER2PEER," +
                               "VIR_MIGRATE_LIVE," +
                               "VIR_MIGRATE_PERSIST_DEST," +
                               "VIR_MIGRATE_TUNNELLED\"",
        "hw_disk_discard": "unmap"
    }
}

controller = [controller_nova]
computer = [computer_nova, computer_nova_compute]

