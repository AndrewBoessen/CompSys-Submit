import sys
import unittest
from unittest.mock import Mock, patch, MagicMock
from paramiko import SSHClient, AutoAddPolicy

sys.path.append("src/cslab/")
from ssh_util import create_ssh_client, connect_ssh

# Mock the paramiko.SSHClient class
class MockSSHClient(SSHClient):
    def __init__(self):
        super(MockSSHClient, self).__init__()

    def connect(self, hostname, port, username, password):
        pass

class TestSSHFunctions(unittest.TestCase):

    @patch('paramiko.SSHClient', MockSSHClient)
    def test_create_ssh_client(self):
        # Ensure create_ssh_client returns an instance of MockSSHClient
        client = create_ssh_client()
        self.assertIsInstance(client, MockSSHClient)

    @patch('paramiko.SSHClient', MockSSHClient)
    def test_connect_ssh(self):
        client = create_ssh_client()
        user = "test_user"
        password = "test_password"

        # Mock the connect method
        with patch.object(client, 'connect', return_value=None) as mock_connect:
            connect_ssh(client, user, password)

            # Verify that the connect method was called with the correct arguments
            mock_connect.assert_called_once_with("cslab.bc.edu", 22, user, password)

if __name__ == '__main__':
    unittest.main()