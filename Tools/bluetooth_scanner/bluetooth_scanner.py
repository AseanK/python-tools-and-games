import sys
import re

from utils import package_installer
package_installer.install_dependencies()

from PyQt5.QtBluetooth import (
    QBluetoothDeviceDiscoveryAgent,
    QBluetoothLocalDevice,
    QBluetoothAddress,
    QBluetoothDeviceInfo
)
from PyQt5.QtCore import QCoreApplication, QObject, pyqtSlot


class BluetoothScanner(QObject):
    def __init__(self):
        super().__init__()
        self.devices = []
        self.connected_devices = []
        self.agent = QBluetoothDeviceDiscoveryAgent()
        self.agent.deviceDiscovered.connect(self.device_discovered)
        self.agent.finished.connect(self.scan_finished)

        # Local Bluetooth adapter
        self.local_device = QBluetoothLocalDevice()

        # Start scanning
        self.agent.start()

    @pyqtSlot("QBluetoothDeviceInfo")
    def device_discovered(self, device):
        name = device.name()
        address = device.address().toString()

        # Skip devices with no name or names matching 'Bluetooth XX:XX:XX:XX:XX:XX' pattern
        if not name:
            return

        pattern = r'^Bluetooth ([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
        if re.match(pattern, name):
            return

        # Save device info
        device_info = {
            "name": name,
            "address": address,
            "device_info": device,  # QBluetoothDeviceInfo object
        }
        self.devices.append(device_info)
        print(f"Discovered device: {name} ({address})")

        # Check pairing status
        pairing_status = self.local_device.pairingStatus(device.address())
        if pairing_status != QBluetoothLocalDevice.Unpaired:
            self.connected_devices.append(device_info)

    @pyqtSlot()
    def scan_finished(self):
        print("\nScan completed!\n")
        print("=== Discovered Bluetooth Devices ===")
        for idx, device in enumerate(self.devices, 1):
            print(f"{idx}. {device['name']} ({device['address']})")

        print("\n=== Connected Bluetooth Devices ===")
        if self.connected_devices:
            for idx, device in enumerate(self.connected_devices, 1):
                print(f"{idx}. {device['name']} ({device['address']})")
        else:
            print("No connected Bluetooth devices found.")

        # Exit the application
        QCoreApplication.quit()


if __name__ == "__main__":
    app = QCoreApplication(sys.argv)
    scanner = BluetoothScanner()
    sys.exit(app.exec_())
