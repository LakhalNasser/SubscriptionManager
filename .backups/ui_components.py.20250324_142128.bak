# ui_components.py

from PyQt5.QtWidgets import *
from config import Config

class WirelessSettings(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("الاتصال اللاسلكي", parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # IP عنصر قائمة عناوين
        ip_layout = QHBoxLayout()
        self.ip_combo = QComboBox()
        self.ip_combo.setEditable(False)
        self.refresh_ip_button = QPushButton("تحديث")
        self.refresh_ip_button.setToolTip("تحديث قائمة عناوين IP المتاحة")
        ip_layout.addWidget(QLabel("عنوان IP:"))
        ip_layout.addWidget(self.ip_combo)
        ip_layout.addWidget(self.refresh_ip_button)
        
        # أزرار التحكم
        buttons_layout = QHBoxLayout()
        self.connect_wireless_button = QPushButton("اتصال لاسلكي")
        self.connect_wireless_button.setToolTip("اتصال لاسلكي بالجهاز المحدد")
        self.disconnect_wireless_button = QPushButton("قطع الاتصال")
        self.disconnect_wireless_button.setToolTip("قطع الاتصال اللاسلكي")
        buttons_layout.addWidget(self.connect_wireless_button)
        buttons_layout.addWidget(self.disconnect_wireless_button)
        
        layout.addLayout(ip_layout)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

class DisplaySettings(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("إعدادات العرض", parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QGridLayout()
        
        # Max Size
        self.max_size_spin = QSpinBox()
        self.max_size_spin.setRange(100, 4096)
        self.max_size_spin.setValue(1920)
        self.max_size_spin.setToolTip('الحد الأقصى لعرض الشاشة')
        layout.addWidget(QLabel('الحد الأقصى للعرض:'), 0, 0)
        layout.addWidget(self.max_size_spin, 0, 1)
        
        # FPS
        self.fps_spin = QSpinBox()
        self.fps_spin.setRange(1, 120)
        self.fps_spin.setValue(60)
        layout.addWidget(QLabel('معدل الإطارات:'), 1, 0)
        layout.addWidget(self.fps_spin, 1, 1)
        
        # Bitrate
        self.bitrate_spin = QSpinBox()
        self.bitrate_spin.setRange(1, 50)
        self.bitrate_spin.setValue(8)
        self.bitrate_spin.setSuffix(' Mbps')
        layout.addWidget(QLabel('جودة البث:'), 2, 0)
        layout.addWidget(self.bitrate_spin, 2, 1)
        
        # تحديث خيارات الدوران
        self.orientation_combo = QComboBox()
        # إضافة العناصر مع نصوص العرض العربية
        for value in Config.ORIENTATIONS:
            self.orientation_combo.addItem(Config.ORIENTATIONS_DISPLAY[value], value)
        self.orientation_combo.setToolTip('اختر اتجاه دوران الشاشة')
        layout.addWidget(QLabel('دوران الشاشة:'), 3, 0)
        layout.addWidget(self.orientation_combo, 3, 1)

        # Display Options
        self.borderless_check = QCheckBox('بدون إطار')
        self.fullscreen_check = QCheckBox('ملء الشاشة')
        self.always_on_top_check = QCheckBox('دائماً في المقدمة')
        self.show_touches_check = QCheckBox('إظهار اللمسات')
        
        layout.addWidget(self.borderless_check, 4, 0)
        layout.addWidget(self.fullscreen_check, 4, 1)
        layout.addWidget(self.always_on_top_check, 5, 0)
        layout.addWidget(self.show_touches_check, 5, 1)
        
        self.setLayout(layout)

class AudioSettings(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("إعدادات الصوت", parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QGridLayout()
        
        self.audio_enabled = QCheckBox('تمكين الصوت')
        self.audio_bit_rate = QSpinBox()
        self.audio_bit_rate.setRange(8, 256)
        self.audio_bit_rate.setValue(128)
        self.audio_bit_rate.setSuffix(' kbps')
        
        layout.addWidget(self.audio_enabled, 0, 0)
        layout.addWidget(QLabel('معدل بت الصوت:'), 1, 0)
        layout.addWidget(self.audio_bit_rate, 1, 1)
        
        self.setLayout(layout)

class InputSettings(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("إعدادات الإدخال", parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QGridLayout()
        
        # Mouse Settings
        self.mouse_type = QComboBox()
        self.mouse_type.addItems(Config.MOUSE_TYPES)
        self.mouse_type.setToolTip('نوع الفأرة')
        layout.addWidget(QLabel('نوع الفأرة:'), 0, 0)
        layout.addWidget(self.mouse_type, 0, 1)

        # Keyboard Settings
        self.keyboard_type = QComboBox()
        self.keyboard_type.addItems(Config.KEYBOARD_TYPES)
        self.keyboard_type.setToolTip('نوع لوحة المفاتيح')
        layout.addWidget(QLabel('نوع لوحة المفاتيح:'), 1, 0)
        layout.addWidget(self.keyboard_type, 1, 1)
        
        self.setLayout(layout)

class ControlSettings(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("إعدادات التحكم", parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QGridLayout()
        
        self.stay_awake = QCheckBox('إبقاء الشاشة مضاءة')
        self.turn_screen_off = QCheckBox('إيقاف شاشة الجهاز')
        self.power_off_on_close = QCheckBox('إيقاف الشاشة عند الإغلاق')
        
        layout.addWidget(self.stay_awake, 0, 0)
        layout.addWidget(self.turn_screen_off, 0, 1)
        layout.addWidget(self.power_off_on_close, 1, 0)
        
        self.setLayout(layout)