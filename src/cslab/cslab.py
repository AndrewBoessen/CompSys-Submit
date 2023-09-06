import pathlib
from scp_util import create_scp_client, copy_file
from ssh_util import create_ssh_client, connect_ssh
import paramiko

def copy_file_to_cslab(in_file: pathlib.PurePath, out_file: pathlib.PurePath, user, password) -> None:
    with create_ssh_client() as ssh:
        connect_ssh(ssh, user, password)

        with create_scp_client(ssh) as scp:
            copy_file(scp, in_file, out_file)