[app]

# Title of your application
title = J.A.R.V.I.S

# Package name
package.name = jarvis

# Package domain (needed for android/ios packaging)
package.domain = org.arnod

# Source code location
source.dir = .

# Source files to include (add extension of files you use)
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3

# Application version
version = 0.1

# Application requirements
# Add any python packages your project uses separated by commas (e.g. kivy,requests,numpy)
requirements = python3,kivy

# Supported orientations (landscape, sensorLandscape, portrait or all)
orientation = portrait

# Fullscreen mode
fullscreen = 0

# (Permissions) Add permissions required by your app
# android.permissions = INTERNET,RECORD_AUDIO

# Android specific configurations
[buildozer]

# Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1

# Android build configuration
[app:android]

# Target API level (33 is Android 13 standard)
android.api = 33

# Minimum API level required (21 is Android 5.0)
android.minapi = 21

# Android NDK version
android.ndk = 25b

# Automatically accept Android SDK license
android.accept_sdk_license = True

# Format of the package (apk or aab)
android.archs = arm64-v8a, armeabi-v7a
