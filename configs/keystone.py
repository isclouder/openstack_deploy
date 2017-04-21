import common

controller_keystone = {
    "filename":"/etc/keystone/keystone.conf",
    "database": {
        "connection": "mysql+pymysql://nova:%s@%s/nova_api" %(common.KEYSTONE_DBPASS, common.CONTROLLER_HOSTNAME)
    },
    "token": {
        "provider": "fernet"
    }
}

controller = [controller_keystone]
computer = []
