import common

controller_glance_api = {
    "filename":"/etc/glance/glance-api.conf",
    "database": {
        "connection": "mysql+pymysql://glance:%s@%s/glance" %(common.GLANCE_DBPASS, common.CONTROLLER_HOSTNAME)
    },
    "keystone_authtoken": {
        "auth_uri": "http://%s:5000" % common.CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "memcached_servers": "%s:11211" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "project_name": "service",
        "username": "glance",
        "password": common.GLANCE_PASS
    },
    "paste_deploy": {
        "flavor": "keystone"
    },
    "glance_store": {
        "stores": "rbd",
        "default_store": "rbd",
        "rbd_store_chunk_size": "8",
        "rbd_store_pool": "images",
        "rbd_store_user": "glance",
        "rbd_store_ceph_conf": "/etc/ceph/ceph.conf"
    }
}

controller_glance_registry = {
    "filename":"/etc/glance/glance-registry.conf",
    "database": {
        "connection": "mysql+pymysql://glance:%s@%s/glance" %(common.GLANCE_DBPASS, common.CONTROLLER_HOSTNAME)
    },
    "keystone_authtoken": {
        "auth_uri": "http://%s:5000" % common.CONTROLLER_HOSTNAME,
        "auth_url": "http://%s:35357" % common.CONTROLLER_HOSTNAME,
        "memcached_servers": "%s:11211" % common.CONTROLLER_HOSTNAME,
        "auth_type": "password",
        "project_domain_name": "Default",
        "user_domain_name": "Default",
        "project_name": "service",
        "username": "glance",
        "password": common.GLANCE_PASS
    },
    "paste_deploy": {
        "flavor": "keystone"
    }
}

controller = [controller_glance_api, controller_glance_registry]
computer = []
