from filecmp import DEFAULT_IGNORES
import threading
from time import perf_counter
from unittest import result
from scrapli.driver.core import IOSXEDriver
from inv import DEVICES

start = perf_counter()

threads = []

def send_cmd(device):
    with IOSXEDriver(
        host=device["host"],
        auth_username = "ds_local_netadmin",
        auth_password = "XIEY;R~pBfi/1YmF@@VC",
        auth_secondary = "1ekVJm2^keW|gJ~hZR~r",
        auth_strict_key = False,
        ssh_config_file = True,
    ) as conn:
        response = conn.send_command('show version')
        print(response.result)

if __name__ == "__main__":
    for device in DEVICES:
        th = threading.Thread(target=send_cmd, args=(device,))
        threads.append(th)
    
    for th in threads:
        th.start()

    for th in threads:
        th.join()
    
end = perf_counter()
total_time = end - start
print(total_time)