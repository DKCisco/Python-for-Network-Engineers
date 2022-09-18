from concurrent.futures import Executor, ProcessPoolExecutor, process
from time import sleep, perf_counter
from scrapli.driver.core import IOSXEDriver
from inv2 import DEVICES

start = perf_counter()


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
        return response.result

if __name__ == "__main__":
    with ProcessPoolExecutor() as exectuor:
        results = exectuor.map(send_cmd, DEVICES)
    
    for results in results:
        print(results)

end = perf_counter()
total_time = end - start
print(total_time)