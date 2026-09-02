[app]

# Application title
title = J.A.R.V.I.S

# Package name
package.name = jarvis

# Package domain
package.domain = org.jarvis.ai

# Source code location
source.dir = .

# Include subdirectories (actions, config, core, dashboard, memory)
source.include_dirs = actions, config, core, dashboard, memory

# Include file extensions
source.include_exts = py, png, jpg, kv, atlas, json, txt, xlsx

# Main file entry point
source.filename = main.py

# Application version
version = 1.0.0

# Application requirements
requirements = python3, kivy, numpy, requests

# Custom App Icon path (pointing to icon.png in your config folder)
icon.filename = %(source.dir)s/config/icon.png

# Orientation
orientation = portrait

# Permissions needed
android.permissions = INTERNET, RECORD_AUDIO

# Android SDK / Target details
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
