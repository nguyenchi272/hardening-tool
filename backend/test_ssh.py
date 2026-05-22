from app.services.ssh_collector \
    import SSHCollector


collector = SSHCollector(
    host="172.22.1.15",
    username="root",
    password="Ncc@rhel"
)

collector.connect()

result = collector.run_command(
    "hostname"
)

print(result)

collector.close()