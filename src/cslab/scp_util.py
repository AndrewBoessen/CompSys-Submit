'''
SCP files from local computer to students cslab
'''

import sys
import pathlib
from paramiko import SSHClient
from scp import SCPClient

# Define progress callback that prints the current percentage completed for the file
def progress(filename, size, sent):
    sys.stdout.write("%s's progress: %.2f%%   \r" % (filename, float(sent)/float(size)*100) )

# Creates scp connection
def create_scp_client(ssh: SSHClient) -> SCPClient:
    return SCPClient(ssh.get_transport(), progress=progress)

# Copies file to ssh connection with scp
def copy_file(scp: SCPClient, in_file_path: pathlib.PurePath, out_file_path: pathlib.PurePath) -> None:
    try:
        scp.put(in_file_path, out_file_path)
    except Exception as err:
        sys.stdout.write(f"Invalid file path: {err}\n")

