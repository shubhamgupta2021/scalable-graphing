Simple python tool to monitor the CPU usage of the virtual machines running on a system.
In the backend uses libvirt api to connect to the xen or qemu hypervisor.
It connect to domain and calculate CPU usage.
Send the CPU usage to the statsd deamon.
Statsd deamon can then send the metrics to carbon which is a twisted async server which listens for metrics and graphite-web can be used to visualize.


Usage:

sudo apt-get install python-libvirt
sudo pip install statsd==1.7.2

sudo python src/main.py