from paramiko import SSHClient, AutoAddPolicy

SERVER = "cslab.bc.edu"
PORT = 22

# Create ssh client
def create_ssh_client() -> SSHClient:
    return SSHClient()

# Connect ssh client
def connect_ssh(client: SSHClient, user: str, password: str) -> None:
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(SERVER, PORT, user, password)
