---
# layout: home
layout: page
permalink: /
title: Home
---
[Watch Posts](/initvenv/posts)
<h1>InitVenv<sub>
    <small class="so-small text-info">pypi version</small>
  </sub>
</h1>

<div class="align-center">
  <a href="https://github.com/Dev2Forge/Init-Venv/"><img src="https://cdn.jsdelivr.net/gh/tutosrive/images-projects-srm-trg@dd775fc24cf6c63171b85694bd0b7d567f055676/dev2forge/InitVenv/icon.ico" width="200"></a>
</div>

---

{% comment %} Badges {% endcomment %}
<article class="align-center badges-article">
  <a href="https://github.com/tutosrive"><img alt="Static Badge" src="https://img.shields.io/badge/author-tutosrive-black?style=plastic"></a>
  <a href="https://pepy.tech/projects/initvenv"><img alt="Pypi Downloads" src="https://static.pepy.tech/personalized-badge/initvenv?period=total&units=INTERNATIONAL_SYSTEM&left_color=gray&right_color=blue&left_text=pypi"></a>
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/initvenv?label=pypi-dm">
  <img alt="PyPI - License" src="https://img.shields.io/pypi/l/initvenv">
  <img alt="SourceForge Downloads" src="https://img.shields.io/sourceforge/dt/init-venv?label=sourceforge.net">
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/initvenv">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/initvenv">
  <img alt="PyPI - Format" src="https://img.shields.io/pypi/format/initvenv">
  <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/initvenv">
  <a href="https://github.com/Dev2Forge/initvenv/actions/workflows/build-and-publish-wheels.yml"><img src="https://github.com/Dev2Forge/initvenv/actions/workflows/build-and-publish-wheels.yml/badge.svg" /></a>
</article>

> See original version: Download the latest [release](https://github.com/Dev2Forge/Init-Venv/releases)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Requirements](#requirements)
- [Important Notes](#important-notes)

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

## Important Notes

- The `requirements.txt` file must contain the dependencies **before** running InitVenv
- The program will not understand requirements once the virtual environment is created
- Currently supports Windows systems only
