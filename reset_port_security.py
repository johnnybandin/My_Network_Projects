from netmiko import ConnectHandler
import getpass
import json
import csv
# Set username and password 
username = input( 'Enter your SSH username here: ')
password = getpass.getpass()

# Set login and device parameters
with open('devices_file') as f:
    all_devices = f.read().splitlines()


# Iterate through all your devices
for devices in all_devices:
    print(f"Connecting to device: " + devices)
    ip_of_devices = devices
    ios_devices = {
        'device_type': 'cisco_ios',
        'ip': ip_of_devices,
        'username': username,
        'password': password
    }
    net_connect = ConnectHandler(**ios_devices)
    output = net_connect.send_command('show interface status')
    print(output)
    if 'err-disabled' in output:
        fix_errdisabled = input('What interfaces needs fixing: ')
        output = net_connect.send_command('int ra ' + fix_errdisabled)
        if 'invalid input detected' in output:
            print('You have entered incorrect interfaces')
        else:
            clear_portsecurity = ['int ra ' + fix_errdisabled, 'shut', 'no shut', 'do wr']
            output = net_connect.send_config_set(clear_portsecurity)
    else:
        print('There is no port security violations here.')
