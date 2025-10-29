<h1 align="center">InitVenv <sub><sub><small><small>pypi version</small></small></sub></sub></h1>

<div align="center">
  <a href="https://github.com/Dev2Forge/Init-Venv/"><img src="https://cdn.jsdelivr.net/gh/tutosrive/images-projects-srm-trg@dd775fc24cf6c63171b85694bd0b7d567f055676/dev2forge/InitVenv/icon.ico" width="200"></a>
</div>

<!-- [Download](./view/download) - [About](./view/about) -->

<div align="center">
  <a href="./view/download">Download</a>
  <a href="./view/about">About</a>
</div>

---

<a href="https://github.com/tutosrive"><img alt="Static Badge" src="https://img.shields.io/badge/author-tutosrive-black?style=plastic"></a>
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/initvenv?period=total&units=INTERNATIONAL_SYSTEM&left_color=ORANGE&right_color=GREEN&left_text=total+downloads)](https://pepy.tech/projects/initvenv)
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/initvenv?label=pypi-dm">
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/initvenv">
<img alt="SourceForge Downloads" src="https://img.shields.io/sourceforge/dt/init-venv?label=sourceforge.net">
<img alt="PyPI - Version" src="https://img.shields.io/pypi/v/initvenv">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/initvenv">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/initvenv">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/initvenv">
<a href="https://github.com/Dev2Forge/initvenv/actions/workflows/build-and-publish-wheels.yml"><img src="https://github.com/Dev2Forge/initvenv/actions/workflows/build-and-publish-wheels.yml/badge.svg"/></a>

> See original version: Download the latest [release](https://github.com/Dev2Forge/Init-Venv/releases)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Original Version (C# native version)](#original-version-c-native-version)
  - [This (`pip install`)](#this-pip-install)
- [Usage](#usage)
  - [Method 1: Windows File Explorer (Recommended)](#method-1-windows-file-explorer-recommended)
  - [Method 2: Command Line](#method-2-command-line)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Important Notes](#important-notes)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)
  - [Pipy version](#pipy-version)
  - [Original version](#original-version)
- [Contributors](#contributors)

**InitVenv** is a cross-platform automation tool that streamlines Python development workflow by automatically creating Python virtual environments, installing project dependencies from `requirements.txt`, and activating the environment with a single command execution. Currently supports Windows, with **Linux** and **macOS** support planned for future releases.

## Features

- **One-command setup**: Create Python virtual environment, install requirements, and activate with a single command
- **Windows integration**: Works seamlessly with Windows File Explorer
- **Automatic detection**: Finds and installs requirements from `requirements.txt` automatically
- **Path flexibility**: Supports both absolute and relative paths
- **Zero configuration**: Just run and go

## Requirements

- Python installed and added to system PATH
- **Windows operating system** (_currently Windows-only_)

## Usage

### Method 1: Windows File Explorer (Recommended)

> If you want to have full compatibility, please consider installing the original executable version.
Download the latest [release](https://github.com/Dev2Forge/Init-Venv/releases)

---

### Method 2: Command Line

```bash
initvenv "C:\path\to\your\project"
```

You can use both absolute and relative paths:
```bash
# This
initvenv ".\my-project"
# Or
initvenv ".."
# or
initvenv "C:\path\to\folder\"
```

## How It Works

The installer creates a simple batch file that launches the main executable (Pass current path if you don't pass any):

```shell
@echo off
if "%~1"=="" (
  set "target=%CD%"
) else (
  set "target=%~1"
)

setlocal
"%~dp0initvenv.exe" "%target%"
endlocal
exit /b %ERRORLEVEL%
```

When you run `initvenv`, it:
1. Detects the current directory
2. Creates a Python virtual environment (`.venv`)
3. Activates the virtual environment
4. Installs packages from `requirements.txt` (if present)
5. Keeps the terminal open for continued work

## Screenshots

| Scenario | Preview |
| :------- | :------ |
| Program startup error - missing working directory | <img height="30%" alt="Program startup error showing missing working directory configuration" src="https://github.com/user-attachments/assets/8b4243a0-4c83-4956-b5e6-7a02d92135bb" /> |
| Successful program initialization without requirements file | <img height="30%" alt="Program successfully started without requirements file installation" src="https://github.com/user-attachments/assets/7e5edffb-4ddc-41df-abe8-b77e88162f61" /> |
| Console with virtual environment activated for user | <img height="30%" alt="Terminal console showing activated virtual environment for user interaction" src="https://github.com/user-attachments/assets/c2acd251-88cb-4285-bd31-10c7c463051a" /> |
| Program execution with requirements file installation | <img height="30%" alt="Program running with automatic requirements file installation process" src="https://github.com/user-attachments/assets/f7e995e2-ff1c-4daf-bc73-9ee5a5430597" /> |
| User terminal session maintained after setup | <img height="30%" alt="User terminal session preserved and ready for continued interaction" src="https://github.com/user-attachments/assets/bc28f7fa-3024-4461-ad58-6462c871fdd6" /> |

## Important Notes

- The `requirements.txt` file must contain the dependencies **before** running InitVenv
- The program will not understand requirements once the virtual environment is created
- Currently supports Windows systems only

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. **I’d be glad to receive help writing the Linux and macOS versions, and adding compatibility with the Windows file system (in this PyPI version — the original version already includes that compatibility).
**

See the [Release Notes](https://github.com/Dev2Forge/Init-Venv/releases) for detailed development history and changelog.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](https://github.com/Dev2Forge/initvenv/blob/main/LICENSE) file for details.

## Links

### Pipy version

- [GitHub Home](https://github.com/Dev2Forge/initvenv/)
- [Releases](https://github.com/Dev2Forge/initvenv/releases)
- [Issues](https://github.com/Dev2Forge/initvenv/issues)
- [Pull Requests](https://github.com/Dev2Forge/initvenv/pulls)

### Original version

- [GitHub Home](https://github.com/Dev2Forge/Init-Venv/)
- [Releases](https://github.com/Dev2Forge/Init-Venv/releases)
- [Issues](https://github.com/Dev2Forge/Init-Venv/issues)
- [Pull Requests](https://github.com/Dev2Forge/Init-Venv/pulls)
- [Download from SourceForge](https://sourceforge.net/projects/Init-Venv/)

## Contributors

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/tutosrive/"><img src="https://avatars.githubusercontent.com/tutosrive?v=4?s=100" width="100px;" alt="Tutos Rive Profile Github Logo"/><br /><sub><b>tutosrive</b></sub></a><br /><a href="https://github.com/Dev2Forge/Init-Venv/commits?author=tutosrive" title="Code">💻</a></td>
  </tr>
</table>

---

⭐ If you find this tool useful, please consider giving it a star!


<a href="https://github.com/Dev2Forge/"><img src="https://cdn.jsdelivr.net/gh/tutosrive/images-projects-srm-trg@main/dev2forge/thumbanil-dev2forge1.webp"/> </a>
