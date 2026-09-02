[app]
# Basic Information
title = JARVIS
package.name = jarvis
package.domain = org.jarvis

# Source Files
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

# Version
version = 1.0.0

# Requirements (Matching your cleaned requirements)
requirements = python3,kivy,google-genai,google-generativeai,pillow,requests,beautifulsoup4,ddgs,numpy,youtube-transcript-api,python-pptx,fastapi,uvicorn,cryptography,python-multipart,qrcode

# Permissions required for Microphone, Internet, and Audio Output
android.permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA

# Android Specific Configuration
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Prevent screen sleep while JARVIS is active
android.wakelock = True
