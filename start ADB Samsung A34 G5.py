import subprocess


def show_nav():
    print("┌────────────────────────────────────────────")
    print("│ Меню:")
    print("│ 1. Автоматический режим (удаление -> установка -> отключение ADB)")
    print("│ 2. Установка приложений")
    print("│ 3. Удаление приложений")
    print("│ 4. Отключение ADB")
    print("│ 5. Выход")


# Названия приложений для удаления
appListDel = {
    "com.netflix.mediaclient",  # Netflix
    "com.spotify.music",  # Spotify
    "com.samsung.android.app.spage",  # Samsung Free
    "com.microsoft.office.outlook",  # MS Outlook
    "com.linkedin.android",  # Linkedin
    "com.microsoft.office.officehubrow",  # MS Office 365
    "com.samsung.sree",  # Samsung Global Goals
    "com.google.android.apps.youtube.music",  # YouTube music
    "com.facebook.katana",  # Facebook
    "com.facebook.appmanager",  # Facebook
    "com.facebook.services",  # Facebook
    "com.facebook.system",  # Facebook
    "com.samsung.android.voc",  # Samsung Members
    "com.samsung.android.game.gamehome",  # Game Launher
    "com.samsung.android.game.gametools",  # Game Launher
    "com.samsung.android.game.gos",  # Game Launher
    "com.microsoft.skydrive",  # MS OneDrive
    "com.samsung.android.bixby.agent",  # Bixby
    "com.samsung.android.bixby.es.globalaction",  # Bixby
    "com.samsung.android.bixbyvision.framework",  # Bixby
    "com.samsung.android.bixby.wakeup",  # Bixby
    "com.samsung.android.bixby.plmsync",  # Bixby
    "com.samsung.android.bixby.voiceinput",   # Bixby
    "com.samsung.systemui.bixby",  # Bixby
    "com.samsung.android.bixby.agent.dummy",  # Bixby
    "com.samsung.android.app.settings.bixby",  # Bixby
    "com.samsung.systemui.bixby2",  # Bixby
    "com.samsung.android.bixby.service",  # Bixby
    "com.samsung.android.app.routines",  # Bixby
    "com.samsung.android.visionintelligence",  # Bixby
    "com.samsung.android.app.spage"  # Bixby
}

# Файлы для установки. Важно! Указывай названия без пробелов и +
appListInstall = {
    "Adobe-Acrobat-23.9.1.29623.apk": "com.adobe.reader",
    "Signal-6.35.3.134102.apk": "org.thoughtcrime.securesms",
    "Telegram-10.1.3-(Android4.4,arm64).apk": "org.telegram.messenger",
    "WhatsApp_v.2.23.19.84(231984004)(5.0-14.0)(arm64-8a).apk": "com.whatsapp",
    "Яндекс.Браузер_v.23.9.4.86(1918436706)(7.0-14.0)(arm64-8a).apk": "com.yandex.browser",
    "MyOffice-Documents-v.2.6.1.apk": "com.ncloudtech.cloudoffice",
    "Chestny+ZNAK+–+Quality+Control_4.46.1.apk": "ru.crptech.mark"
}

# Функция проверки наличия


def check_device():
    print("│ Ожидание подключения устройства")
    subprocess.run("adb wait-for-device")
    print("│ Устройство подключено")


def check_app(app):
    command_check = "adb shell pm list packages " + app
    return_output = str(subprocess.check_output(command_check))
    print(f"│ ► Выполняется поиск на устройстве: {app} ")
    return return_output.__contains__(app)

# Удаление приложений из списка "appListDel"


def del_app():
    print("│  Удаление приложений ")
    for app in appListDel:
        if check_app(app):
            print(f"│   ► Удаление: {app}")
            command_del = "adb shell pm uninstall -k --user 0 " + app
            subprocess.run(command_del, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"│    ► {app} удалено")
            print("├────────────────────────────────────────────")
        else:
            print(f"│   ► {app} не найдено")
            print("├────────────────────────────────────────────")

# Установка приложений


def install_app():
    # путь к папке с файлами для установки
    path_app_install = "C:/install/"

    for nameApk, app in appListInstall.items():
        if not (check_app(app)):
            command_install = "adb install " + path_app_install + nameApk
            print(f"│    ► Идет установка {app}")
            subprocess.run(command_install, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"│    ► Установка {nameApk} завершена")
            print("├────────────────────────────────────────────")
        else:
            print(f"│    ► {app} уже установленно")
            print("├────────────────────────────────────────────")

# Отключение режима разработчика


def dev_off():
    command_dev_off = "adb shell settings put global development_settings_enabled 0"
    command_debag_off = "adb shell settings put global adb_enabled 0"
    subprocess.run(command_dev_off, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(command_debag_off, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# -----------------------


print("v.1.2 (20.10.2023)")
print()
print("Скрипт предназначен для автоматического удаления и установки приложений на Android через ADB")
print("Root не требуется, перед началом активируйте режим разработчика и отладку через USB!")

check_device()

nav = 0
show_nav()
while nav != 4:
    nav = int(input("│ Выберите действие: "))

    if nav == 1:
        print("├────────────────────────────────────────────")
        del_app()
        print("│ Удаление заверешено")
        print("├────────────────────────────────────────────")
        print("│ Начало установки приложений")
        install_app()
        print("├────────────────────────────────────────────")
        print("│ Установка завершена")
        print("├────────────────────────────────────────────")
        dev_off()
        print("│ Режим разработчика отключен")
        show_nav()

    elif nav == 2:
        print("├────────────────────────────────────────────")
        install_app()
        print("│ Удаление заверешено")
        print("├────────────────────────────────────────────")
        show_nav()

    elif nav == 3:
        print("├────────────────────────────────────────────")
        print("│ Начало установки приложений")
        del_app()
        print("├────────────────────────────────────────────")
        show_nav()

    elif nav == 4:
        print("├────────────────────────────────────────────")
        dev_off()
        print("│ Режим разработчика на утройстве отключен")
        print("├────────────────────────────────────────────")
        show_nav()

    elif nav == 5:
        print("│ Удачного дня! ;) ")
        exit()
