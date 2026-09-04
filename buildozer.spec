[app]
# ... keep existing app configurations ...

[app:android]
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True

# ENABLE MULTIDEX TO FIX D8/DX HANGS
android.enable_multidex = True
