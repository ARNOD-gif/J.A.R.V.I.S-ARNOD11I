[app]
title = J.A.R.V.I.S
package.name = jarvis
package.domain = org.arnod
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3
version = 0.1

# Pin python3 to 3.11 to prevent target python 3.14 build errors
requirements = python3==3.11.0,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True
