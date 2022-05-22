from scrapli.driver.core import IOSXEDriver

MY_DEVICE = {
    "host": "192.168.31.101",
    "auth_username" : "john",
    "auth_password" : "C1sco12345",
    "auth_secondary": "cisco1",
    "port" : 22,
    "auth_strict_key" : False,
    "transport_options": {"open_cmd": ["-o", "KexAlgorithms=+diffie-hellman-group14-sha1"]}
}

with IOSXEDriver(**MY_DEVICE) as conn:
    response = conn.send_configs(["router ospf 41", "network 41.41.41.41 0.0.0.0 area 41"])
    print(response.result)