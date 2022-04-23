my_ip_address = ["192.168.1.1", "192.168.2.1", "200.0.0.1", "203.0.01", "8.8.8.8"]
my_public_ips = []

for ip_address in my_ip_address:
    if "192.168" not in ip_address:
        my_public_ips.insert(0, ip_address)

print(f"My public IP addresses are {my_public_ips}")