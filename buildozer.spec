[app]

# (str) Title of your application
title = J.A.R.V.I.S

# (str) Package name (must contain only letters/numbers, no spaces or special characters)
package.name = jarvis

# (str) Package domain (needed for Android package ID: org.arnod.jarvis)
package.domain = org.arnod

# (str) Source code directory where main.py lives (. represents current directory)
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3,ico

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.3.0,plyer,requests,urllib3,certifi,idna

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Fullscreen mode (0 or 1)
fullscreen = 0


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 or 1)
warn_on_root = 1


[app:android]

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 24

# (str) Android NDK version
android.ndk = 25b

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

# (list) Target architecture
android.archs = arm64-v8a

# (list) Android application permissions
android.permissions = INTERNET, RECORD_AUDIO, ACCESS_NETWORK_STATE

# (bool) Enable AndroidX / Multidex support
android.enable_multidex = True
