
import os
import libvirt
import logging
from xml.etree import ElementTree

class DomainManager(object):

    def __init__(self, remote = None):
        self.conn = None
        self.remote = remote
        self.__createConnection();

    def __createConnection(self):
        try:
            if self.remote:
                self.conn = libvirt.open("qemu+tcp://%s/system" % self.remote)
            else:
                self.conn = libvirt.open("qemu:///system")
            return self.conn
        except Exception as e:
            logging.error('Failed to open connection to QEMU/KVM: %s' % e)
            return None

    def closeConnection(self):
        self.conn.close()

    def getDomInfoByName(self, name):
        if self.conn == None:
            self.conn = self.__createConnection()
        myDom = self.conn.lookupByName(name)
        return myDom

    def defineDomainXml(self, path):
        ret = os.path.exists(path)
        if ret is False:
            raise FileNotFoundException(path+" is not found")
        root = ElementTree.parse(path).getroot()
        xml = ElementTree.tostring(root, 'utf-8')
        self.conn.defineXML(xml)

    def startDomain(self, name):
        logging.info('In [%s] libvirt start %s' % (self.remote, name))
        myDom = self.getDomInfoByName(name)
        if myDom.isActive() == False:
            myDom.create()

    def shutdownDomain(self, name):
        logging.info('In [%s] libvirt shutdown %s' % (self.remote, name))
        myDom = self.getDomInfoByName(name)
        if myDom.isActive() == True:
            myDom.shutdown()

    def ifDomRunning(self, name):
        try:
            myDom = self.getDomInfoByName(name)
            if myDom.isActive() == False:
                logging.info('In [%s] libvirt %s is not running' % (self.remote, name))
                return False
            else:
                logging.info('In [%s] libvirt %s is running' % (self.remote, name))
                return True
        except:
            logging.info('In [%s] libvirt %s is not defined' % (self.remote, name))
            return False

