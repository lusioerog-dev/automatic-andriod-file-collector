import subprocess


def get_connected_devices():
    try:
        result = subprocess.run(
            ["adb", "devices"],
            capture_output=True,
            text=True,
            check=True
        )
    except FileNotFoundError:
        print("ADB was not found.")
        return []

    lines = result.stdout.strip().splitlines()

    devices = []

    for line in lines[1:]:
        if "\tdevice" in line:
            serial = line.split("\t")[0]
            devices.append(serial)

    return devices