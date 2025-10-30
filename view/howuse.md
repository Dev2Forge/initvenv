---
layout: page
title: How to Use
permalink: /view/howto
---

In any case, you must have a requirements.txt file for PIP to detect the libraries. If you add the requirements.txt file after running `initvenv`, it won't have any effect. This is because at the time of [`initvenv`](https://github.com/Dev2Forge/Init-Venv/), it depends entirely on PIP commands, so when you run `pip check` without a requirements.txt file, it won't stop to search on its own. I will update this in a future version.

Knowing this, the first step is to put a `requirements.txt` file in the working directory (You can safely omit it, then obviously you will have to use `pip install` — Again, if you don't add this —)

---

### Method 1: Windows File Explorer (Recommended)

For it to work, you must specify the path, either relative or absolute, that is:

<div class="center">
    <img src="https://cdn.jsdelivr.net/gh/tutosrive/images-projects-srm-trg@591ea68b0a5c28922df1cc9471fba52746db48e1/dev2forge/InitVenv/initvenv-explain-explorer1.png"/>
</div>

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
