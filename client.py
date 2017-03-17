
import json
import urllib2
import config

class Opthttp(object):
    def __init__(self, passwd):
        self.token = None
        self.tenant = None
        self.token, self.tenant = self.__get_token(passwd)

    def __get_token(self, passwd):
        url = 'http://127.0.0.1:5000/v2.0/tokens'
        values = {"auth": {"tenantName": "admin", "passwordCredentials": {"username": "admin", "password": passwd}}}
        data = self.http_post(url, values)
        token = data['access']['token']['id']
        tenant = data['access']['token']['tenant']['id']
        return token, tenant

    def http_get(self, url):
        req = urllib2.Request(url)
        req.add_header('X-Auth-Token', self.token)
        response = urllib2.urlopen(req)
        data = response.read()
        data = json.loads(data)
        return data

    def _do_http_post(self, method, url, body):
        if body:
            jdata = json.dumps(body)
            req = urllib2.Request(url, jdata)
        else:
            req = urllib2.Request(url, None)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        if self.token:
            req.add_header('X-Auth-Token', self.token)
        req.get_method = lambda: method
        response = urllib2.urlopen(req)
        data = response.read()
        if data != '':
            data = json.loads(data)
        return data

    def http_post(self, url, body):
        return self._do_http_post('POST', url, body)

    def http_put(self, url, body):
        return self._do_http_post('PUT', url, body)

    def http_delete(self, url, body):
        return self._do_http_post('DELETE', url, body)

class Neutron(object):
    def __init__(self):
        self.baseurl = 'http://cvm:9696/v2.0'
        self.http = Opthttp(config.ADMIN_PASS)

    def router_list(self):
        url = '%s/routers.json' %(self.baseurl)
        list = self.http.http_get(url)
        return list

    def router_port_list(self, id):
        url = '%s/ports.json?device_id=%s' %(self.baseurl, id)
        list = self.http.http_get(url)
        return list

    def router_create(self, name):
        url = '%s/routers.json' %(self.baseurl)
        body = {'router': {'name': name, 'admin_state_up': True}}
        ret = self.http.http_post(url, body)
        return ret

    def router_gateway_clear(self, id):
        url = '%s/routers/%s.json' %(self.baseurl, id)
        body = {'router': {'external_gateway_info': {}}}
        ret = self.http.http_put(url, body)
        return ret

    def router_interface_delete(self, id, subnet_id):
        url = '%s/routers/%s/remove_router_interface.json' %(self.baseurl, id)
        body = {'subnet_id': subnet_id}
        ret = self.http.http_put(url, body)
        return ret

    def router_delete(self, id):
        url = '%s/routers/%s.json' %(self.baseurl, id)
        body = None
        ret = self.http.http_delete(url, body)
        return ret


