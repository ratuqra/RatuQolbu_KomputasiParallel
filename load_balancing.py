# Studi Kasus: Load Balancing pada Sistem E-Commerce

jumlah_server = int(input("Masukkan jumlah server: "))

servers = []
for i in range(jumlah_server):
    s = input(f"Masukkan nama server ke-{i+1}: ")
    servers.append(s)

jumlah_request = int(input("\nMasukkan jumlah request: "))

requests = []
for i in range(jumlah_request):
    req = input(f"Masukkan request ke-{i+1}: ")
    requests.append(req)

print("\n=== Hasil Load Balancing (Round Robin) ===\n")

for i in range(len(requests)):
    server = servers[i % len(servers)]
    print(f"{requests[i]} --> ditangani oleh {server}")