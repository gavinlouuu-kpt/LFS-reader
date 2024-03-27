import sys
import os
import unittest

# Add the 'src' directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', 'src')
sys.path.append(src_dir)
import unittest
from unittest.mock import patch
from json_extract import DataProcessor  # Adjust import path based on your project structure

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.sample_data = """
        /dev/cu.wchusbserial220 has been opened successfully.
        Received command: ls
        Listing directory: /
        DIR : /E4:65:B8:80:22:A4
        Listing directory: /E4:65:B8:80:22:A4
        FILE: /d_2024_03_20_t08_26_49
        FILE: /t_0
        FILE: /t_1
        FILE: /t_2
        FILE: /t_3
        FILE: /t_4
        FILE: /t_5
        FILE: /TouchCalData1
        FILE: /config.json
        DIR : /factory
        Listing directory: /factory
        FILE: /preset.json
        FILE: /wifiCredentials.json
        """

    def test_extract_mac_address(self):
        expected_mac_address = "E4:65:B8:80:22:A4"  # Remove the leading slash
        extracted_mac_address = DataProcessor.extract_mac_address(self.sample_data)
        self.assertEqual(extracted_mac_address, expected_mac_address, "MAC address extraction did not return the expected result.")


    def test_path_constructor(self):
        expected_paths = [
            '/E4:65:B8:80:22:A4/t_0', '/E4:65:B8:80:22:A4/t_1',
            '/E4:65:B8:80:22:A4/t_2', '/E4:65:B8:80:22:A4/t_3',
            '/E4:65:B8:80:22:A4/t_4', '/E4:65:B8:80:22:A4/t_5'
        ]
        constructed_paths = DataProcessor.path_constructor(self.sample_data)
        self.assertListEqual(constructed_paths, expected_paths, "Constructed paths did not match the expected paths.")

if __name__ == "__main__":
    unittest.main()
