server_ip = ("192.168.1.1",)  # Tuple (immutable)
allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_allowed_ips(new_ip):
    allowed_ips.append(new_ip)

def display_config():
    print("Server IP:", server_ip[0])
    print("Allowed IPs:", allowed_ips)

update_allowed_ips("192.168.1.4")
display_config()

