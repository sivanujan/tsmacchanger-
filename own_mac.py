import subprocess
print("Welcome to ST Mac Changer")


def mac_changer(interface,new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
   
    subprocess.run(f"sudo ifconfig {interface} down", shell=True)
    subprocess.run(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
    subprocess.run(f"sudo ifconfig {interface}  up", shell=True)
interface = input("[+]Enter the interface name ")
new_mac = input("[+]Enter the new Mac ")
mac_changer(interface,new_mac)    


