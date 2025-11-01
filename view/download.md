---
layout: page
title: Download
permalink: /view/download
---

<div class="center">
    <iframe frameborder="0" src="https://itch.io/embed/4005004?linkback=true&amp;border_width=5&amp;bg_color=1e1e1e&amp;fg_color=00c3e8&amp;link_color=fae45b&amp;border_color=1caefa" width="560" height="175"><a href="https://tutosrive.itch.io/initvenv">Init Venv - CLI Virtual Python Environments by tutosrive</a></iframe>
</div>

<nav id="toc">
  <h3>Table of Contents</h3>
  <ul>
    <li><a href="#original-version-c-native-version">Original Version (C# native version)</a></li>
    <ul>
      <li><a href="#blue-screen-solution-windows-run-prevention">Blue Screen Solution (Windows Run Prevention)</a></li>
    </ul>
    <li><a href="#pip-install">pip install</a></li>
  </ul>
</nav>

## Original Version (C# native version)
1. Download from [itch.io](https://tutosrive.itch.io/initvenv)
2. Run the installer
3. The installer will:
   - Copy `InitVenv-{architecture}.exe` and `InitVenv.bat` to your chosen directory
   - Add the installation directory to system PATH

### Blue Screen Solution (Windows Run Prevention)
- <img src="https://cdn.jsdelivr.net/gh/tutosrive/images-projects-srm-trg@main/dev2forge/InitVenv/probl1.png" alt="probl1" loading="lazy">
- <img src="https://cdn.jsdelivr.net/gh/tutosrive/images-projects-srm-trg@main/dev2forge/InitVenv/probl2.png" alt="probl2" loading="lazy">

---

## pip install

> Important: If you want the command to be available globally, you must install .__. in the global Python installation — that is, outside of virtual environments.

1. open a CMD and write
   ```shell
    pip install initvenv
   ```
2. Once installed, you can use it (As I said before, this version only allows calls from the console, not from Windows File Explorer)
