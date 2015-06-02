import libvirt
import time
import constants

class VirtualizationLib(object):

    def __init__(self, hypervisor):
        if hypervisor=="qemu":
            self.conn = libvirt.open(constants.qemu_uri)
        elif hypervisor == "xen":
            self.conn = libvirt.open(constants.xen_uri)
    def getCPUusages(self):
        usage_dict ={}
        for domain_id in self.conn.listDomainsID():
            domain = self.conn.lookupByID(domain_id)
            usage_dict[domain.name()] = self.getCPUusage(domain)
        return usage_dict


    def getCPUusage(self, domain):
            cputime1 = domain.info()[4]
            time.sleep(1)
            cputime2 = domain.info()[4]
            cpuUsage = float(cputime2-cputime1)/(10**7)
            return cpuUsage