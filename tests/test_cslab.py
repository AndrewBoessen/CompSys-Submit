import unittest
import sys
import tempfile
import os
from unittest.mock import Mock, patch

sys.path.append("src/cslab")
from cslab import (
    resolve_absolute_path,
    copy_file_to_cslab,
    create_ssh_client,
    create_scp_client,
    connect_ssh,
    copy_file,
)

class TestYourFunctions(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, 'test.txt')
        # Create a temporary file
        with open(self.test_file, 'w') as f:
            f.write("Hello, world!")

    def tearDown(self):
        # Remove the temporary directory and its contents
        os.remove(self.test_file)
        os.rmdir(self.test_dir)

    def test_resolve_absolute_path(self):
        # Test resolving an absolute path
        input_path = self.test_file
        result = resolve_absolute_path(input_path)
        self.assertEqual(result, os.path.abspath(input_path))

    @patch('cslab.create_ssh_client')
    @patch('cslab.create_scp_client')
    def test_copy_file_to_cslab(self, mock_create_scp_client, mock_create_ssh_client):
        # Mock SSH and SCP client functions
        mock_ssh = Mock()
        mock_scp = Mock()
        mock_create_ssh_client.return_value.__enter__.return_value = mock_ssh
        mock_create_scp_client.return_value.__enter__.return_value = mock_scp

        # Mock the 'copy_file' function
        with patch('cslab.copy_file') as mock_copy_file:
            # Test copying a file to a remote server
            in_file = self.test_file
            out_file = '/remote/path/test.txt'
            user = 'testuser'
            password = 'testpassword'

            copy_file_to_cslab(in_file, out_file, user, password)

            # Assert that the SSH and SCP functions were called with the correct arguments
            mock_create_ssh_client.assert_called_once()
            mock_create_scp_client.assert_called_once()
            mock_copy_file.assert_called_once_with(mock_scp, os.path.abspath(in_file), out_file)

if __name__ == '__main__':
    unittest.main()
