[app]

# Application title
title = J.A.R.V.I.S

# Package name
package.name = jarvis

# Package domain
package.domain = org.jarvis.ai

# Source code location
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt

# Application version
version = 1.0.0

# Application requirements
requirements = python3,kivy,numpy,requests

# Path to your custom App Icon (place icon.png in your main repo folder)
icon.filename = %(source.dir)s/icon.png

# Supported orientations
orientation = portrait

# Android permissions
android.permissions = INTERNET, RECORD_AUDIO

# Android API target
android.api = 33
android.minapi = 21

# Target architecture
android.archs = arm64-v8a