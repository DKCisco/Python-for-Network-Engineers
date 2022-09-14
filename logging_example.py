import logging
#from scrapli.driver.core import JunosDriver
from scrapli.driver.core import IOSXEDriver

logging.basicConfig(filename="newlogsconfig.txt", level=logging.DEBUG)

def test_func():
    with IOSXEDriver(
        host="192.168.50.22",
        auth_username = "ds_local_netadmin",
        auth_password = "XIEY;R~pBfi/1YmF@@VC",
        auth_secondary = "1ekVJm2^keW|gJ~hZR~r",
        auth_strict_key = False,
        ssh_config_file = True,
    ) as conn:
        response = conn.send_configs(["router ospf 51"])
        return response.result

if __name__ == "__main__":
    results = test_func()
    print(results)