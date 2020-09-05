import sys
import getopt
import time
from si_prefix import si_format

arg = argv = sys.argv[1:] 
iface = None
try:
    opts, args = getopt.getopt(arg, "i:", ["interface="])
    if len(opts) < 1:
       print("no interface given")
except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
for opt, arg in opts:
    if opt in ("-i", "--interface"):
        iface = arg
        print("interface: " + arg)
    else:
        print("error - no option given")

while True:
    start_rx = 0
    end_rx = 0
    start_tx = 0
    end_tx = 0
    with open('/proc/net/dev','r') as file:
        for i in file.readlines():
            if iface in i:
                itx = i.split()
                start_rx = itx[1]
                start_tx = itx[9]
    time.sleep(1)

    with open('/proc/net/dev','r') as file:
        for i in file.readlines():
            if iface in i:
                itx = i.split()
                stop_rx = itx[1]
                stop_tx = itx[9]       
    delta_rx = si_format(int(stop_rx) - int(start_rx), precision=2)
    delta_tx = si_format(int(stop_tx) - int(start_tx), precision=2)
    sys.stdout.write("RX: " + str(delta_rx) + "B/s  TX: " + str(delta_tx) + "B/s               \r")
    sys.stdout.flush()

