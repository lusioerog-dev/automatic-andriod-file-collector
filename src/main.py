from adb.devices import get_connected_devices


def main():
    print("MLBB Automatic Collector")
    print("------------------------")

    devices = get_connected_devices()

    if not devices:
        print("No Android device detected.")
        return

    print(f"Found {len(devices)} device(s):")

    for device in devices:
        print(f"- {device}")


if __name__ == "__main__":
    main()