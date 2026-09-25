from adb.devices import get_connected_devices
from collector.scanner import (
    get_fight_history_files,
    get_battle_record_files,
)


def main():
    print("MLBB Automatic Collector")
    print("------------------------")

    devices = get_connected_devices()

    if not devices:
        print("No Android device detected.")
        return

    device = devices[0]

    print(f"\nUsing device: {device}")

    fight_history = get_fight_history_files(device)
    battle_records = get_battle_record_files(device)

    print("\nFightHistory")
    print("------------")
    print(f"Found {len(fight_history)} file(s)")

    for filename in fight_history:
        print(f"- {filename}")

    print("\nBattleRecord")
    print("------------")
    print(f"Found {len(battle_records)} file(s)")

    for filename in battle_records:
        print(f"- {filename}")


if __name__ == "__main__":
    main()