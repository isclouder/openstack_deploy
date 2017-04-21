import common

controller_cinder = {
    "filename":"/etc/cinder/cinder.conf",
    "database": {
        "connection": "mysql+pymysql://nova:%s@%s/nova" %(common.CINDER_DBPASS, common.CONTROLLER_HOSTNAME)
    },
    "DEFAULT": {
        "transport_url": "rabbit://openstack:%s@%s" % (common.RABBIT_PASS, common.CONTROLLER_HOSTNAME),
        "auth_strategy": "keystone",
        "enabled_backends": "ceph",
        "glance_api_servers": "http://%s:9292" % common.CONTROLLER_HOSTNAME,
        "enable_force_upload": "true",
        "my_ip": ""
    },
    "keystone_authtoken": {
        "auth_uri": "http://%s:5000" % common.CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "memcached_servers": "%s:11211" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "project_name": "service",
        "username": "cinder",
        "password": common.NOVA_PASS
    },
    "oslo_concurrency": {
        "lock_path": "/var/lib/cinder/tmp"
    },
    "ceph": {
        "volume_driver": "cinder.volume.drivers.rbd.RBDDriver",
        "rbd_pool": "volumes",
        "rbd_ceph_conf": "/etc/ceph/ceph.conf",
        "rbd_flatten_volume_from_snapshot": "false",
        "rbd_max_clone_depth": "5",
        "rbd_store_chunk_size": "4",
        "rados_connect_timeout": "-1",
        "glance_api_version": "2"
    }
}

controller = [controller_cinder]
computer = []
