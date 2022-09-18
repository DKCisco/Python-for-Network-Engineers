import pytest
from urllib import response
from rich import print as rprint
from scrapli.driver.core import IOSXEDriver
from inv import DEVICES

@pytest.mark.parametrize("device", DEVICES)
def test_number_interfaces(device):
    for device in DEVICES:
        with IOSXEDriver(
        host=device["host"],
        auth_username = "ds_local_netadmin",
        auth_password = "XIEY;R~pBfi/1YmF@@VC",
        auth_secondary = "1ekVJm2^keW|gJ~hZR~r",
        auth_strict_key = False,
        ssh_config_file = True,
        ) as conn:
            response = conn.send_command("show interfaces")
        structured_result = response.textfsm_parse_output()
        #rprint(structured_result)
        assert len(structured_result) == 20