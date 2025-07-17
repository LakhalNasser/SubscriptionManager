# config.py
import os
import sys
import tempfile

def get_resource_path(relative_path):
    """الحصول على المسار الصحيح للموارد سواء في وضع التطوير أو التشغيل"""
    if hasattr(sys, '_MEIPASS'):
        # إذا كان التطبيق مجمّع
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

class Config:
    APP_NAME = "Scrcpy Manager"
    APP_VERSION = "1.0.0"
    
    # المسارات
    BASE_DIR = get_resource_path('')
    SCRCPY_PATH = get_resource_path('scrcpy')
    ASSETS_PATH = get_resource_path('assets')
    
    # مسار الأيقونة
    ICON_PATH = os.path.join(ASSETS_PATH, "icon.png")
    
    # أوامر التشغيل
    SCRCPY_COMMAND = os.path.join(SCRCPY_PATH, "scrcpy.exe")
    ADB_COMMAND = os.path.join(SCRCPY_PATH, "adb.exe")

    # Default Settings
    DEFAULT_WINDOW_SIZE = (800, 600)
    DEFAULT_WINDOW_POS = (100, 100)
    DEFAULT_TIMEOUT = 30
    DEFAULT_MAX_SIZE = 1920
    DEFAULT_FPS = 60
    DEFAULT_BITRATE = 8
    DEFAULT_AUDIO_BITRATE = 128

    # UI Settings
    MOUSE_TYPES = ["uhid", "sdk", "aoa"]
    KEYBOARD_TYPES = ["uhid", "sdk", "aoa"]
    LANGUAGES = ["English", "Arabic"]
    ROTATIONS = ["0°", "90°", "180°", "270°"]
    ORIENTATIONS = ["0", "90", "180", "270", "flip0", "flip90", "flip180", "flip270"]
    ORIENTATIONS_DISPLAY = {
        "0": "طبيعي",
        "90": "90 درجة",
        "180": "180 درجة",
        "270": "270 درجة",
        "flip0": "عكس أفقي",
        "flip90": "عكس أفقي + 90 درجة",
        "flip180": "عكس أفقي + 180 درجة",
        "flip270": "عكس أفقي + 270 درجة"
    }
