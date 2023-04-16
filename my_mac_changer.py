import subprocess
import optparse
import re

def get_user_input():
    parse_option = optparse.OptionParser()
    parse_option.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_option.add_option("-m","--mac",dest="mac_address",help="new mac address")
    return parse_option.parse_args()

def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
    if new_mac:
        return new_mac.group(0)
    else:
        return None

print("Mac changer started!")
(user_inputs, arguments) = get_user_input()
change_mac_address(user_inputs.interface, user_inputs.mac_address)
finalized_mac = control_new_mac(user_inputs.interface)

if finalized_mac == user_inputs.mac_address:
    print("The MAC address has been successfully changed.")
else:
    print("An error occurred while changing MAC address")