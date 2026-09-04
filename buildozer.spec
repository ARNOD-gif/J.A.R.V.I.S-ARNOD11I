[app:android]
# Set minapi to 24 (API 21 is incompatible with modern NDK toolchains)
android.minapi = 24

# Set target api
android.api = 33

# Set NDK version
android.ndk = 25b

# Target ONLY 64-bit architecture (arm64-v8a)
android.archs = arm64-v8a

# Enable multidex
android.enable_multidex = True
