import csv
import struct
from scrapli.driver.core import IOSXEDriver
from rich import print as rprint
from inv import DEVICES

for device in DEVICES:
    hostname = device["hostname"]
    with IOSXEDriver(
        host = device["host"],
        auth_username = "ds_local_netadmin",
        auth_password = "XIEY;R~pBfi/1YmF@@VC",
        auth_secondary = "1ekVJm2^keW|gJ~hZR~r",
        auth_strict_key = False,
        ssh_config_file = True,
    ) as conn:
        response = conn.send_command("show version")
    structured_result = response.textfsm_parse_output()[0]
    version = structured_result["version"]
    serial = structured_result["serial"]
    #rprint(f"{hostname} - {version} - {serial}")
    with open("test.csv", "a") as csv_data:
        writer = csv.writer(csv_data)
        my_data = ("DigitalSpiffy.com", hostname, serial, version)
        writer.writerow(my_data)

