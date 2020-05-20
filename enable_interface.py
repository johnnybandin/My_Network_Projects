from netmiko import ConnectHandler
import getpass
# Make the login parameters entered from user
password = getpass.getpass()
username = input( "Enter SSH user here: " )

# Create dictionaries for login
ios_device_s1 ={
    'device_type': 'cisco_ios',
    'ip': '192.168.122.15',
    'username': username,
    'password': password
}

# Create a list for all iOS devices
all_devices = [ios_device_s1]

for device in all_devices:
    # Connect to devices
    net_connect = ConnectHandler(**device)
    is_valid_input = False
    while not is_valid_input:
        interface = input("What interface would you like to enable?: ")
        output = net_connect.send_command('show interface ' + interface)
        if 'Invalid input detected' in output:
            print("You have entered an invalid interface")
        else:
            is_valid_input = True
            firstline = output.splitlines()[0]
            print(firstline)
            if not 'up' in firstline:
                no_shut = input('Interface is down, would you like to enable? (y/n)')
                if no_shut == 'y':
                    commands = ['interface ' + interface, 'no shut', 'exit']
                    output = net_connect.send_config_set(commands)
                    print(output)
                    print('#' * 40)
                    print('The interface has been enabled')
                else:
                    print("Will terminate connection now!")
                    break
            else:
                print("The interface " + interface + " is already up")