import os
import sys
import shutil
import PyInstaller.__main__
from PIL import Image  # تأكد من تثبيت Pillow: pip install pillow

def convert_png_to_ico(png_path, ico_path):
    """تحويل PNG إلى ICO"""
    try:
        img = Image.open(png_path)
        img.save(ico_path, format='ICO')
        return True
    except Exception as e:
        print(f"خطأ في تحويل الأيقونة: {e}")
        return False

def main():
    # تحديد المسارات
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(current_dir, 'dist')
    build_dir = os.path.join(current_dir, 'build')
    assets_dir = os.path.join(current_dir, 'assets')
    scrcpy_dir = os.path.join(current_dir, 'scrcpy')
    
    # مسارات الأيقونة
    png_icon = os.path.join(assets_dir, 'icon.png')
    ico_icon = os.path.join(assets_dir, 'icon.ico')

    # حذف الملفات القديمة
    for dir_path in [dist_dir, build_dir]:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

    # التحقق من وجود الأيقونة وتحويلها
    if not os.path.exists(png_icon):
        print("خطأ: ملف الأيقونة PNG غير موجود!")
        return

    # تحويل PNG إلى ICO
    if not convert_png_to_ico(png_icon, ico_icon):
        print("خطأ في تحويل الأيقونة!")
        return

    # تجميع الملفات المطلوبة
    data_files = [
        ('assets/*', 'assets'),
        ('scrcpy/*', 'scrcpy'),
    ]

    # خيارات البناء
    options = [
        'main.py',
        '--name=ScrcpyManager',
        '--onefile',
        '--windowed',
        f'--icon={ico_icon}',  # استخدام ملف ICO
        '--noconfirm',
        '--clean',
        '--uac-admin',
    ]

    # إضافة الملفات المطلوبة
    for src, dst in data_files:
        options.extend(['--add-data', f'{src};{dst}'])

    # إضافة خيارات تحسين الأداء
    options.extend([
        '--noupx',
        '--noconsole',
    ])

    try:
        # تشغيل عملية البناء
        PyInstaller.__main__.run(options)
        
        print("تم بناء التطبيق بنجاح!")
        print(f"الملف التنفيذي موجود في: {os.path.join(dist_dir, 'ScrcpyManager.exe')}")
        
        # حذف ملف ICO المؤقت
        if os.path.exists(ico_icon):
            os.remove(ico_icon)
            
    except Exception as e:
        print(f"حدث خطأ أثناء البناء: {e}")
        
    finally:
        # تأكد من حذف ملف ICO المؤقت في جميع الحالات
        if os.path.exists(ico_icon):
            try:
                os.remove(ico_icon)
            except:
                pass

if __name__ == "__main__":
    # التأكد من تثبيت المكتبات المطلوبة
    required_packages = ['pyinstaller', 'pillow']
    for package in required_packages:
        try:
            __import__(package.replace('pillow', 'PIL'))
        except ImportError:
            print(f"تثبيت {package}...")
            os.system(f"pip install {package}")
    
    main()