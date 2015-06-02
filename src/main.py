from  virtlib import VirtualizationLib
import statsd
import logging
import constants
import traceback

logging.basicConfig(filename=constants.LogFile, level=logging.DEBUG)

logger = logging.getLogger('virtlib')

virtlib=None

try:
    stats = statsd.Gauge("libvirt")
    virtlib = VirtualizationLib(hypervisor="qemu")
except Exception as err:
    trace = traceback.format_exc()
    logger.exception(trace)

while 1:
    try:
        cpu_usages = virtlib.getCPUusages()
        for domain_name in cpu_usages:
            stats.send(domain_name, cpu_usages[domain_name])
            print domain_name, cpu_usages[domain_name]
    except Exception as err:
        trace = traceback.format_exc()
        logger.exception(trace)
