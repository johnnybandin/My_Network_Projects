from netmiko import ConnectHandler
import getpass
import json
import csv
# Set username and password 
username = input( 'Enter your SSH username here: ')
password = getpass.getpass()

# Set login and device parameters
ios_device_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.15',
    'username': username,
    'password': password
}

# Make a list of all device
all_devices = [ios_device_s1]

# Iterate through all your devices
for device in all_devices:
    print(f"Connecting to device: " + device['ip'])
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show interface status')
    print(output)
filename = f"port_security-{device['ip']}.json"
print('-------------- Writing Port Security table------------')
with open(filename, 'w') as f:
    port = json.dump(output, f)


   