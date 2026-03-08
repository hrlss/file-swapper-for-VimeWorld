import os
import shutil
from pathlib import Path

logo = r"""
 ________.__  .__          __                              .___
/  _____/|  | |__| _______/  |_  ____ ______  ____     __| _/
/   \  ___|  | |  |/  ___/\   __\/  _ \\____ \/    \  / __ | 
\    \_\  \  |_|  |\___ \  |  | (  <_> )  |_> >   |  \/ /_/ |
 \______  /____/__/____  > |__|  \____/|   __/|___|  /\____ |
        \/             \/              |__|         \/      \/
        glistopad swapper  by hrlss & glistopad.lol
        github.com/hrlss
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_DIR = os.path.join(BASE_DIR, "Default")
MODIFIED_DIR = os.path.join(BASE_DIR, "Modified")

appdata = Path(os.getenv("APPDATA"))

JAR_TARGET = appdata / ".vimeworld" / "1.8.8_new_anticheat"
DLL_TARGET = appdata / ".vimeworld" / "jre" / "brainstorm_new" / "windows-amd64" / "bin"


def replace_files(source_folder):
    for file in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file)

        if file.endswith(".jar"):
            dest_path = JAR_TARGET / file

        elif file.endswith(".dll"):
            dest_path = DLL_TARGET / file

        else:
            continue

        shutil.copy2(source_path, dest_path)
        print(f"Заменен файл: {file}")


print(logo)

while True:
    print("\n1 - Load Default")
    print("2 - Load Modified")
    print("0 - Exit")

    choice = input("Select: ")

    if choice == "1":
        replace_files(DEFAULT_DIR)

    elif choice == "2":
        replace_files(MODIFIED_DIR)

    elif choice == "0":
        break

    else:
        print("Wrong choice")
