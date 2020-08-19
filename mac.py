import subprocess
import optparse
import re
print("Welcome to ST Mac Changer") 

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface",help="Interface to Chance its MAC address")
    parser.add_option("-m","--mac",dest = "new_mac", help = "New Mac Address" )
    (options,arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Please enter the interface , use --help more info")
    elif not options.new_mac:
        parser.error("[-] Please Enter the Mac ,Use --help more info")
    return options



def mac_changer(interface,new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.run(f"sudo ifconfig {interface} down", shell=True)
    subprocess.run(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.run(f"sudo ifconfig {interface}  up", shell=True)

def current_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface]).strip()
    mac_address_result = re.search(rb"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    print(mac_address_result)
    if mac_address_result:
        return mac_address_result.group(0)
    else:
        print("[-] Could not read Mac Address") 
 

options = get_arguments()   
current_mac = current_mac_address(options.interface)
print(f"Current Mac = {current_mac}")
mac_changer(options.interface, options.new_mac)




