from urllib import response
import logging
from scrapli.driver.core import JunosDriver

logging.basicConfig(filename="newlogsblah.txt", level=logging.DEBUG)

def test_func():
    with JunosDriver(
        host="192.168.50.21",
        auth_username = "ds_local_netadmin",
        auth_password = "XIEY;R~pBfi/1YmF@@VC",
        auth_secondary = "1ekVJm2^keW|gJ~hZR~r",
        auth_strict_key = False,
        ssh_config_file = True,
    ) as conn:
        response = conn.send_command("show version")
        return response.result
if __name__ == "__main__":
    test_func()