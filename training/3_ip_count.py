# Count IPs in a Range
# 10.10.7.0 - 10.10.8.255

import ipaddress

def count_ips(start, end):
    start_ip = int(ipaddress.ip_address(start))
    print(start_ip)
    end_ip = int(ipaddress.ip_address(end))
    print(end_ip)
    return end_ip - start_ip + 1

print(count_ips("10.10.7.0", "10.10.9.5"))  # Output: 512
