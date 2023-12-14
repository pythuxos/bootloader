import edk2toollib
version = "Everest"
# planned codenames:
# version = "Kilamanjaro"
# version = "Matterhorn"
# version = "1.0 Beta"
# version = "1.0 Release Candiate"
# version = "Zeus"
print(f"Pythux version {version}")
print("Loading system modules...")
import sys
import time
print("Finding a Pythux kernel...")
print("Error: Could not find a supported Pythux kernel.")
print("Do not install pythux bootloaders to boot linux, windows, etc.")
print("Such OSes are incompatible with Pythux bootloaders. Use GRUB for dualbooting.")
time.sleep(5)
exit(1)
