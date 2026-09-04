[app]
title = J.A.R.V.I.S
package.name = jarvis
package.domain = org.arnod
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,wav,mp3,ico
version = 0.1

# Direct pointer to your .ico file
icon.filename = %(source.dir)s/jarvis.ico

requirements = python3,kivy

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
android.enable_multidex = True
