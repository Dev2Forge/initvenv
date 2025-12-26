import os
import sys
import platform
from pathlib import Path
import subprocess

def main():
    """Launcher entry point that runs the bundled initvenv.bat (or initvenv.exe).
    On Windows this will execute the shipped .bat (preferred) or the .exe.
    If the user does not pass a path, uses "." as default.
    """

    if platform.system().lower().startswith("win"):
        # Prevent recursive re-invocation
        if os.environ.get("INITVENV_LAUNCHED") == "1":
            return 0

        pkg_root = Path(__file__).resolve().parent
        scripts_dir = pkg_root / "scripts"

        bat = scripts_dir / "initvenv.bat"
        exe = scripts_dir / "initvenv.exe"

        if not bat.exists() and not exe.exists():
            pkg_root_up = pkg_root.parent
            scripts_dir = pkg_root_up / "scripts"
            bat = scripts_dir / "initvenv.bat"
            exe = scripts_dir / "initvenv.exe"

        # If no path provided, default to current directory "."
        user_args = sys.argv[1:]
        if not user_args:
            target = "."
        else:
            target = user_args[0]

        env = os.environ.copy()
        env["INITVENV_LAUNCHED"] = "1"

        cmd = os.environ.get("COMSPEC", "cmd.exe")

        if bat.exists():
            bat_path = str(bat)
            argv = [cmd, "/c", bat_path, target]
            try:
                subprocess.run(argv, check=True, env=env)
                return 0
            except subprocess.CalledProcessError as e:
                print(f"Error executing {bat}: {e}", file=sys.stderr)
                return e.returncode

        if exe.exists():
            exe_path = str(exe)
            argv = [exe_path, target]
            try:
                subprocess.run(argv, check=True, env=env)
                return 0
            except subprocess.CalledProcessError as e:
                print(f"Error executing {exe}: {e}", file=sys.stderr)
                return e.returncode

        print("Error: neither initvenv.bat nor initvenv.exe were found in package scripts/", file=sys.stderr)
        return 2
    elif platform.system().lower() == "linux":
        # Prevent recursive re-invocation
        if os.environ.get("INITVENV_LAUNCHED") == "1":
            return 0

        # Detect architecture
        machine = platform.machine().lower()
        if machine in ["x86_64", "amd64"]:
            arch = "x64"
        elif machine in ["aarch64", "arm64"]:
            arch = "arm64"
        else:
            print(f"Unsupported architecture: {machine}", file=sys.stderr)
            return 1

        pkg_root = Path(__file__).resolve().parent
        bin_dir = pkg_root / "bin" / f"linux-{arch}"
        binary = bin_dir / "initvenv"

        if not binary.exists():
            print(f"Error: Binary not found at {binary}", file=sys.stderr)
            return 2

        # If no path provided, default to current directory "."
        user_args = sys.argv[1:]
        if not user_args:
            target = "."
        else:
            target = user_args[0]

        env = os.environ.copy()
        env["INITVENV_LAUNCHED"] = "1"

        argv = [str(binary), target]
        try:
            subprocess.run(argv, check=True, env=env)
            return 0
        except subprocess.CalledProcessError as e:
            print(f"Error executing {binary}: {e}", file=sys.stderr)
            return e.returncode
    else:
        print(f"This platform {platform.system()} is coming soon!")
        return 0

if __name__ == "__main__":
    sys.exit(main())