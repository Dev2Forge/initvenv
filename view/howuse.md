---
layout: page
title: How to Use
permalink: /view/howto
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
