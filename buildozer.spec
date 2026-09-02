[app]
title = J.A.R.V.I.S
package.name = jarvis
package.domain = org.arnod
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
# Android Target Settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
