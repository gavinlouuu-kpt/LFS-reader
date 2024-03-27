# Serial Data Extractor and JSON Saver

This Python script is designed to communicate with a serial device, read a directory listing, open specific files, and extract and save JSON content from those files.

## Features

- List available serial ports
- Open and close a serial connection
- Read a directory listing from the serial device
- Construct file paths based on the directory listing
- Open and read files from the serial device
- Extract JSON content from the file data
- Save the extracted JSON content to separate files

## Prerequisites

- Python 3.x
- pyserial library (`pip install pyserial`)

## Usage

1. Update the `target_com` variable in the `if __name__ == "__main__":` section with the correct serial port for your device.
2. Run the script: `python script.py`
3. The script will open the specified serial port, read the directory listing, construct file paths, open the files, extract JSON content, and save the JSON data to separate files in the `data_extract` directory.

## Classes

### `JSONDataManager`

This class provides static methods for extracting JSON content from a file's data and saving it to a file.

- `extract_json_content(file_data)`: Extracts the JSON content from the file data using a regular expression pattern.
- `save_json_to_file(json_data, path)`: Saves the provided JSON data to a file with a filename derived from the given path.

### `SerialManager`

This class manages the serial communication with the device.

- `list_serial_ports()`: Lists the available serial ports on the system.
- `open_com()`: Opens the serial connection with the specified port and baud rate.
- `close_com()`: Closes the serial connection.
- `read_data_list()`: Sends the `ls` command to the serial device and reads the directory listing.
- `open_file(path)`: Opens a file on the serial device by sending the `open` command and the provided file path.

### `DataProcessor`

This class provides static methods for processing and extracting data from the serial device's output.

- `extract_mac_address(message)`: Extracts the MAC address from the provided message string using a regular expression pattern.
- `path_constructor(data)`: Constructs file paths based on the directory listing data from the serial device.

## Example Output

```
/dev/cu.wchusbserial220 has been opened successfully.

DIR : /E4:65:B8:80:22:A4 
 FILE: /t_0
 FILE: /t_1
 FILE: /t_2

Command executed
Ready to open file.
Paths to open: ['/E4:65:B8:80:22:A4/t_0', '/E4:65:B8:80:22:A4/t_1', '/E4:65:B8:80:22:A4/t_2']
File opened successfully: /E4:65:B8:80:22:A4/t_0
File saved successfully: data_extract/E4_65_B8_80_22_A4_t_0.json
File opened successfully: /E4:65:B8:80:22:A4/t_1
File saved successfully: data_extract/E4_65_B8_80_22_A4_t_1.json
File opened successfully: /E4:65:B8:80:22:A4/t_2
File saved successfully: data_extract/E4_65_B8_80_22_A4_t_2.json
/dev/cu.wchusbserial220 has been closed successfully.
```
