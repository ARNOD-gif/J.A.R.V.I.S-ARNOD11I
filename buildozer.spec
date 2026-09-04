[app]

# (str) Title of your application
title = JARVIS Mobile

# (str) Package name
package.name = jarvisapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.jarvis

# (str) Source code where the main.py file is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,plyer,requests,urllib3,certifi,idna,charset_normalizer

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Use --private data directory (1) or --dir public storage (0)
android.private_storage = 1

# (list) List of Java .jar files to add to the libs so that your application can use them
# android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project
# android.add_src =

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libdir and symlinks.
android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
