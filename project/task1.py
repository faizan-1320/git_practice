# Example Input
# logs = [
#     (1609459200, "192.168.1.1", "192.168.1.2", 100),
#     (1609459260, "192.168.1.2", "192.168.1.3", 50),
#     (1609459320, "192.168.1.3", "192.168.1.4", 250),
#     (1609459380, "192.168.1.4", "192.168.1.2", 300),
#     (1609459440, "192.168.1.5", "192.168.1.1", 400)
# ]

# Test Case 1
# logs = [
#     (1609459200, "10.0.0.1", "10.0.0.2", 20),
#     (1609459260, "10.0.0.2", "10.0.0.3", 40),
#     (1609459320, "10.0.0.1", "10.0.0.3", 80),
# ]

# Test Case 2
logs = [
    (1609459200, "1.1.1.1", "2.2.2.2", 10),
    (1609459260, "2.2.2.2", "3.3.3.3", 10),
    (1609459320, "3.3.3.3", "4.4.4.4", 10),
]

# Test Case 3
# logs = []

if logs:
    data_mb = [data[3] for data in logs]
    avrage_data = sum(data_mb)/len(data_mb)

    high_transfer_ips = []
    relay_ips = []

    for entry in logs:
        _,src_ip,den_ip,data = entry
        if data > avrage_data*2:
            high_transfer_ips.append(src_ip)

    source = {src for _, src, _, _ in logs}
    destination = {den for _,_,den,_ in logs}

    delay = source.intersection(destination)

    print('High Transer IPs:',high_transfer_ips)
    print('Delay IPs:',list(delay))
else:
    print('High Transer IPs:',[])
    print('Delay IPs:',[])