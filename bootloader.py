import edk2toollib
version = "Everest"
# planned codenames:
# version = "Kilamanjaro"
# version = "Matterhorn"
# version = "1.0 Beta"
# version = "1.0 Release Candiate"
# version = "Zeus"
print()
print("Kernel Loader for EFI Systems (Pythux KLES)")
print(f"Pythux version {version}")
print("Loading system modules...")
import sys
import time
print("Finding a Pythux kernel...")
print("Error: Could not find a supported Pythux kernel.")
print("Do not install Pythux KLES to boot linux, windows nt, etc.")
print("Such OSes are incompatible with KLES. Use GRUB for dualbooting.")
time.sleep(5)
exit(1)
