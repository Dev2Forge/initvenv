import os
import sys
import platform
from pathlib import Path


def main():
    """Launcher entry point that runs the bundled initvenv.bat (or initvenv.exe).

    On Windows this will execute the shipped .bat (preferred) or the .exe.
    On other platforms it prints a short message with the platform name.
    """
    system_name = platform.system()
    # If not Windows, inform the user and exit gracefully
    if not system_name.lower().startswith("win"):
        print(f"Próximamente funcionará en esta plataforma {system_name}")
        return 0

    # location of this module -> package root
    pkg_root = Path(__file__).resolve().parent
    # scripts directory inside the package
    scripts_dir = pkg_root / "scripts"

    # prefer the .bat next to the installed script
    bat = scripts_dir / "initvenv.bat"
    exe = scripts_dir / "initvenv.exe"

    # If not found where expected, try one level up (defensive)
    if not bat.exists() and not exe.exists():
        pkg_root_up = pkg_root.parent
        scripts_dir = pkg_root_up / "scripts"
        bat = scripts_dir / "initvenv.bat"
        # exe = scripts_dir / "initvenv.exe"

    if bat.exists():
        # On Windows run the .bat through cmd.exe so associations work
        cmd = "cmd.exe" # os.environ.get("COMSPEC", "cmd.exe")
        args = [cmd, "/c", str(bat)] + sys.argv[1:]
        os.execv(cmd, args)

    # if exe.exists():
    #     # Execute the exe directly, replacing the current process
    #     os.execv(str(exe), [str(exe)] + sys.argv[1:])

    print("Error: neither initvenv.bat nor initvenv.exe were found in package scripts/", file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main())
