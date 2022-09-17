from scrapli.driver.core import IOSXEDriver
from inv import DEVICES

def find_macs(structure_result):
    my_mac = []
    for interface in structure_result:
        try:
            my_mac.append(structure_result[interface]["mac_address"])
        except KeyError:
            pass
    return my_mac

def send_cmd(device):
    with IOSXEDriver(
        host=device["host"],
        auth_username = "ds_local_netadmin",
        auth_password = "XIEY;R~pBfi/1YmF@@VC",
        auth_secondary = "1ekVJm2^keW|gJ~hZR~r",
        auth_strict_key = False,
        ssh_config_file = True,
    ) as conn:
        response = conn.send_command("show interfaces")
        structured_result = response.genie_parse_output()
        return structured_result

if __name__ == "__main__":
    for device in DEVICES:
        result = send_cmd(device)
        my_macs = find_macs
        print(device)
        print(my_macs)  