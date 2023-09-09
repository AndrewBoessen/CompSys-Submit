import sys
from paramiko import SSHClient
from scp import SCPClient

# Define progress callback that prints the current percentage completed for the file
def progress(filename, size, sent):
    """
    Callback function to display progress while copying files via SCP.

    Parameters:
    - filename (str): The name of the file being copied.
    - size (int): The total size of the file in bytes.
    - sent (int): The number of bytes sent so far.

    Returns:
    None
    """
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

# Creates SCP client for file transfer
def create_scp_client(ssh: SSHClient) -> SCPClient:
    """
    Create an SCP (Secure Copy Protocol) client for file transfer over SSH.

    Parameters:
    - ssh (SSHClient): An active SSH client connection.

    Returns:
    SCPClient: An SCP client object for file transfer.
    """
    return SCPClient(ssh.get_transport(), progress=progress)

# Copies a file to a remote server using SCP
def copy_file(scp: SCPClient, in_file_path: str, out_file_path: str) -> None:
    """
    Copy a file to a remote server using SCP.

    Parameters:
    - scp (SCPClient): An SCP client object.
    - in_file_path (str): The path to the local file to be copied.
    - out_file_path (str): The destination path on the remote server.

    Returns:
    None
    """
    try:
        # Attempt to copy the file to the remote server.
        scp.put(in_file_path, out_file_path)
    except Exception as err:
        sys.stdout.write(f"Invalid file path: {err}\n")
