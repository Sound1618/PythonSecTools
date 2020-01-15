#!/usr/bing/env python

# This program changes the Mac address of the primary interface on Linux distributions

import subprocess
import optparse
import re

# Handles command arguments from console
def get_arguments():
    
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to modify")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Please specify an interface, use --help for more information.")
    return options


# Passing value from parser to system subprocess
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for" + interface + "to" + new_mac)

    # Actual subprocess call
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    output_search = subprocess.check_output(["ifconfig", interface])
    mac_output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output_search)

    # Return message if input is invalid
    if mac_output:
        return mac_output.group(0)
    else:
        print("[-] Could not read MAC address.")

# Return from functions
options = get_arguments()

# Verifies current MAC
current_mac = get_current_mac(options.interface)
print("Current MAC Address = " + str(current_mac))

change_mac(options.interface, options.new_mac)

# Verify MAC update after change
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC Address was susccessfully changed to " + current_mac)
else:
    print("[-] MAC Address was not changed")



