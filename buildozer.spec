[app]

# (str) Title of your application
title = J.A.R.V.I.S

# (str) Package name
package.name = jarvis

# (str) Package domain (needed for android/ios packaging)
package.domain = org.arnod

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (file extensions)
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3,ico

# (str) Application versioning
version = 0.1

# (str) Application icon file (.ico is supported automatically via ImageMagick in our build pipeline)
icon.filename = %(source.dir)s/jarvis.ico

# (list) Application requirements
# Add any pure-Python packages your main.py imports here (separated by commas)
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO, ACCESS_NETWORK_STATE

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
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

# (list) Architectures to build for
android.archs = arm64-v8a

# (bool) Enable AndroidX / Multidex support
android.enable_multidex = True
