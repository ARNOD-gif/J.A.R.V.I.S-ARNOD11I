[app]
title = J.A.R.V.I.S
package.name = jarvis
package.domain = org.arnod
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3
version = 0.1

# Keep requirements clean to prevent C-extension compilation errors
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 24
# FORCE STABLE NDK VERSION (Prevents auto-downloading broken NDK r28)
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
