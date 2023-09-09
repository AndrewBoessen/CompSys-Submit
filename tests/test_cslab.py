import unittest
import sys
from unittest.mock import MagicMock, patch
import paramiko
import scp

sys.path.append("../src/cslab")
from cslab import copy_file_to_cslab

class TestCopyFileToCslab(unittest.TestCase):

    @patch('cslab.create_ssh_client')
    @patch('cslab.create_scp_client')
    @patch('cslab.copy_file')
    @patch('cslab.connect_ssh')
    def test_copy_file_to_cslab(self, mock_connect_ssh, mock_copy_file, mock_create_scp_client, mock_create_ssh_client):
        # Mock the return values of create_ssh_client, create_scp_client, and connect_ssh
        ssh_mock = MagicMock(spec=paramiko.SSHClient)
        scp_mock = MagicMock(spec=scp.SCPClient)
        mock_create_ssh_client.return_value.__enter__.return_value = ssh_mock
        mock_create_scp_client.return_value.__enter__.return_value = scp_mock

        # Call the function
        in_file = 'path/to/source/file.txt'
        out_file = 'path/to/destination/file.txt'
        user = 'your_user'
        password = 'your_password'
        copy_file_to_cslab(in_file, out_file, user, password)

        # Ensure that the functions were called with the correct arguments
        mock_create_ssh_client.assert_called_once()
        mock_connect_ssh.assert_called_once_with(ssh_mock, user, password)
        mock_create_scp_client.assert_called_once_with(ssh_mock)
        mock_copy_file.assert_called_once_with(scp_mock, in_file, out_file)

if __name__ == '__main__':
    unittest.main()
