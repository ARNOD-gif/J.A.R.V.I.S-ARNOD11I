[app]

# (str) Title of your application
title = J.A.R.V.I.S

# (str) Package name
package.name = jarvis

# (str) Package domain
package.domain = org.arnod

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3,ico

# (str) Application versioning
version = 0.1

# (str) Application icon file
icon.filename = %(source.dir)s/jarvis.ico

# (list) Requirements: Explicitly include python3, kivy, and common dependencies
requirements = python3,kivy==2.3.0,requests,urllib3,certifi,idna,chardet,plyer

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]

# (int) Log level (2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
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

# (list) Gradle dependencies
android.gradle_dependencies =
