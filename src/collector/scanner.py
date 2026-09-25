import subprocess


FIGHT_HISTORY_PATH = (
    "/storage/emulated/999/Android/data/com.mobile.legends/"
    "files/dragon2017/FightHistory"
)

BATTLE_RECORD_PATH = (
    "/storage/emulated/999/Android/data/com.mobile.legends/"
    "files/dragon2017/BattleRecord"
)


def list_files(device, remote_path):
    try:
        result = subprocess.run(
            [
                "adb",
                "-s",
                device,
                "shell",
                "ls",
                "-1",
                remote_path,
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        return [
            line.strip()
            for line in result.stdout.splitlines()
            if line.strip()
        ]

    except subprocess.CalledProcessError as error:
        print(f"Could not scan {remote_path}")
        print(error.stderr)
        return []


def get_fight_history_files(device):
    files = list_files(device, FIGHT_HISTORY_PATH)

    return [
        filename
        for filename in files
        if filename.startswith("His-")
    ]


def get_battle_record_files(device):
    files = list_files(device, BATTLE_RECORD_PATH)

    return [
        filename
        for filename in files
        if filename.endswith(".bytes")
    ]