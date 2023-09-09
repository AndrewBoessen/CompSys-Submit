import unittest
from unittest.mock import Mock, patch
import pathlib
from paramiko import SSHClient
from scp import SCPClient
import sys

sys.path.append("../src/cslab")
from scp_util import create_scp_client, copy_file

class TestSCPFunctions(unittest.TestCase):
    def setUp(self):
        # Create mock objects for SSHClient and SCPClient
        self.mock_ssh = Mock(spec=SSHClient)
        self.mock_transport = Mock()
        self.mock_ssh.get_transport.return_value = self.mock_transport
        self.mock_scp = Mock(spec=SCPClient)
        self.mock_transport.open_session.return_value = self.mock_scp

        # Define test file paths
        self.in_file_path = pathlib.PurePath("test_file.txt")
        self.out_file_path = pathlib.PurePath("/remote/test_file.txt")

    @patch('sys.stdout')
    def test_create_scp_client(self, mock_stdout):
        # Test create_scp_client function
        scp_client = create_scp_client(self.mock_ssh)
        
        # Assert that a valid SCPClient object is returned
        self.assertIsInstance(scp_client, SCPClient)
        
        # Assert that SSHClient's get_transport method is called
        self.mock_ssh.get_transport.assert_called_once()
        
        # Assert that sys.stdout.write is not called in this case
        mock_stdout.write.assert_not_called()

    @patch('sys.stdout')
    def test_copy_file_success(self, mock_stdout):
        # Test copy_file function when the copy operation succeeds
        with patch('builtins.open', create=True), patch('os.path.getsize', return_value=100):
            copy_file(self.mock_scp, self.in_file_path, self.out_file_path)
        
        # Assert that SCPClient's put method is called with the correct arguments
        self.mock_scp.put.assert_called_once_with(self.in_file_path, self.out_file_path)
        
        # Assert that sys.stdout.write is not called in this case
        mock_stdout.write.assert_not_called()

    @patch('sys.stdout')
    def test_copy_file_failure(self, mock_stdout):
        # Test copy_file function when the copy operation raises an exception
        self.mock_scp.put.side_effect = Exception("Invalid file path")
        copy_file(self.mock_scp, self.in_file_path, self.out_file_path)
        
        # Assert that SCPClient's put method is called with the correct arguments
        self.mock_scp.put.assert_called_once_with(self.in_file_path, self.out_file_path)
        
        # Assert that sys.stdout.write is called with the error message
        mock_stdout.write.assert_called_with("Invalid file path: Invalid file path\n")

if __name__ == '__main__':
    unittest.main()