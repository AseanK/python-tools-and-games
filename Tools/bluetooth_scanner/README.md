# Bluetooth Scanner using PyQt5

A Python application that scans for nearby Bluetooth devices using PyQt5's QtBluetooth module. It lists both discovered and connected Bluetooth devices, providing a simple interface to manage Bluetooth peripherals directly from the application.

## Features

- **Device Scanning**: Searches for nearby Bluetooth devices.
- **Device Filtering**: Ignores devices without names or with default naming patterns.
- **Connected Devices**: Identifies and lists devices that are already paired or connected.
- **Cross-Platform**: Works on any operating system supported by PyQt5 and QtBluetooth.

## Requirements

- **Python 3.5+**
- **PyQt5**
  - Ensure that PyQt5 is installed with Bluetooth support.
- **QtBluetooth Module**
  - Some operating systems might require additional packages for Bluetooth functionality.

## Usage

### Run the Application

```bash
python bluetooth_scanner.py
```

### Understanding the Output

- **Discovered Devices**: The application will print out all Bluetooth devices found during the scan.
- **Connected Devices**: It will list devices that are currently paired or connected to your system.

## How It Works

### Initialization:

- Creates an instance of `QBluetoothDeviceDiscoveryAgent` to manage the scanning process.
- Connects signals to handle device discovery and completion of the scan.

### Device Discovery:

- The `device_discovered` method is called whenever a new device is found.
- Filters out devices without a name or with default naming patterns like "Bluetooth XX:XX:XX:XX:XX".
- Stores valid devices in a list and checks their pairing status.

### Completion:

- Once scanning is finished, `scan_finished` is called.
- Prints out lists of all discovered devices and connected devices.
- Exits the application gracefully.

## Customization

### Filtering Devices:

- Modify the regular expression in the `device_discovered` method to change how devices are filtered.
- Currently, it filters out devices matching the pattern: `Bluetooth XX:XX:XX:XX:XX:XX`.

### Extending Functionality:

- Implement additional features like initiating pairing, connecting to devices, or handling data transfer.
- Utilize other classes from the QtBluetooth module as needed.

## Troubleshooting

### No Devices Found:

- Ensure that your Bluetooth adapter is enabled and working properly.
- Check that the devices you're trying to discover are discoverable.

### Import Errors:

- Verify that PyQt5 is installed correctly with Bluetooth support.
- Some Linux distributions require additional Qt Bluetooth packages.

### Permission Issues:

- On Linux, you might need to run the application with `sudo` to access Bluetooth hardware.
- Alternatively, add your user to the `bluetooth` group:

  ```bash
  sudo usermod -a -G bluetooth $(whoami)
  ```

## Notes

### Cross-Platform Compatibility:

- While PyQt5 aims to be cross-platform, Bluetooth support might vary depending on the operating system and hardware drivers.
- Testing has been primarily conducted on Windows 10 and Ubuntu 20.04.

### PyQt5 Version:

- This application requires PyQt5 version that includes the QtBluetooth module.
- You can check your PyQt5 version using:

  ```python
  import PyQt5
  print(PyQt5.QT_VERSION_STR)
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the PyQt5 and Qt communities for providing extensive documentation and support.
- Inspired by the need for simple Bluetooth management in Python applications.
