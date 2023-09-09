import pathlib
from scp_util import create_scp_client, copy_file
from ssh_util import create_ssh_client, connect_ssh

def resolve_absolute_path(file_path):
    """
    Resolve the absolute path from a given file path.

    Parameters:
    - file_path (str): The input file path to be resolved.

    Returns:
    str: The resolved absolute path.
    """
    # Create a Path object from the input file path
    path = pathlib.Path(file_path)

    # Get the absolute path
    absolute_path = path.resolve()

    return str(absolute_path)

def copy_file_to_cslab(in_file: str, out_file: str, user: str, password: str) -> None:
    """
    Copy a file from a local machine to a remote server using SSH and SCP.

    Parameters:
    - in_file (str): The path to the local file to be copied.
    - out_file (str): The path to the destination file on the remote server.
    - user (str): The username for SSH authentication.
    - password (str): The password for SSH authentication.

    Returns:
    None
    """
    # Create an SSH client context using a context manager.
    with create_ssh_client() as ssh:
        # Connect to the remote server using SSH.
        connect_ssh(ssh, user, password)

        # Create an SCP (Secure Copy Protocol) client context using a context manager.
        with create_scp_client(ssh) as scp:
            # Resolve the absolute path of the local input file.
            abs_in_file = resolve_absolute_path(in_file)

            # Copy the local file to the remote server.
            copy_file(scp, abs_in_file, out_file)
