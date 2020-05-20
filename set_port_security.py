from netmiko import ConnectHandler
import getpass

password = getpass.getpass()

with open('devices_file') as f:
    all_devices = f.read().splitlines()


for devices in all_devices:
    print(f"Connecting to device {devices}")
    ip_of_devices = devices
    ios_devices = {
        'device_type': 'cisco_ios',
        'ip': ip_of_devices,
        'username': input('Enter username here: '),
        'password': password
    }
    net_connect = ConnectHandler(**ios_devices)
    commands = ['conf t', 'int ra g1/0 - 3', 'switchport', 'switchport mode access', 'switchport port-security', 'switchport port-sec max 1']
    output = net_connect.send_config_set(commands)
    print(output)