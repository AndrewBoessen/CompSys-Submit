import paramiko

SERVER = "cslab.bc.edu"
PORT = 22

# Create ssh client
def create_ssh_client() -> paramiko.SSHClient:
    return paramiko.SSHClient()

# Connect ssh client
def connect_ssh(client: paramiko.SSHClient, user: str, password: str) -> None:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(SERVER, PORT, user, password)
