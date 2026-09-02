[app]

# (str) Title of your application
title = J.A.R.V.I.S

# (str) Package name
package.name = jarvis

# (str) Package domain (needed for android packaging)
package.domain = org.jarvis.ai

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (python files, images, text, datasets)
source.include_exts = py, png, jpg, kv, atlas, json, txt, xlsx, ico

# (list) List of directory to include
source.include_dirs = actions, config, core, dashboard, memory

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# Comma separated e.g. requirements = sqlite3,kivy
requirements = python3, kivy, numpy, requests

# (str) Custom icon path (points to the png generated during build)
icon.filename = %(source.dir)s/config/icon.png

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 21

# (list) List of Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Indicate whether the screen should stay on
android.wakelock = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
