import paramiko

SERVER = "cslab.bc.edu"
PORT = 22

# Create an SSH client instance
def create_ssh_client() -> paramiko.SSHClient:
    """
    Create and return an SSH client instance.

    Returns:
    paramiko.SSHClient: An SSH client instance.
    """
    return paramiko.SSHClient()

# Connect to an SSH server
def connect_ssh(client: paramiko.SSHClient, user: str, password: str) -> None:
    """
    Connect to an SSH server using the provided SSH client.

    Parameters:
    - client (paramiko.SSHClient): An SSH client instance.
    - user (str): The username for SSH authentication.
    - password (str): The password for SSH authentication.

    Returns:
    None
    """
    # Set the policy to automatically add the host key (not recommended for production).
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SSH server using the specified server, port, username, and password.
    client.connect(SERVER, PORT, user, password)
