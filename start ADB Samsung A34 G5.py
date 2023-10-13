import subprocess, time

# Названия приложений для удаления
appListDel = {
    'com.netflix.mediaclient', #Netflix
    'com.spotify.music', #Spotify
    'com.samsung.android.app.spage', #Samsung Free
    'com.microsoft.office.outlook', #MS Outlook
    'com.linkedin.android', #Linkedin
    'com.microsoft.office.officehubrow', #MS Office 365
    'com.samsung.sree', #Samsung Global Goals
    'com.google.android.apps.youtube.music', #Youtube music

    'com.facebook.katana',#Facebook
    'com.facebook.appmanager', #Facebook
    'com.facebook.services', #Facebook
    'com.facebook.system', #Facebook
    'com.samsung.android.voc', #Samsung Members
    'com.samsung.android.game.gamehome', #Game Launher
    'com.samsung.android.game.gametools', #Game Launher
    'com.samsung.android.game.gos', #Game Launher
    'com.microsoft.skydrive', #MS OneDrive
    'com.samsung.android.bixby.agent', #Bixby
    'com.samsung.android.bixby.es.globalaction', #Bixby
    'com.samsung.android.bixbyvision.framework', #Bixby
    'com.samsung.android.bixby.wakeup', #Bixby
    'com.samsung.android.bixby.plmsync', #Bixby
    'com.samsung.android.bixby.voiceinput', #Bixby
    'com.samsung.systemui.bixby', #Bixby
    'com.samsung.android.bixby.agent.dummy', #Bixby
    'com.samsung.android.app.settings.bixby', #Bixby
    'com.samsung.systemui.bixby2', #Bixby
    'com.samsung.android.bixby.service', #Bixby
    'com.samsung.android.app.routines', #Bixby
    'com.samsung.android.visionintelligence', #Bixby
    'com.samsung.android.app.spage' #Bixby
}

#путь к папке с файлами для установки
pathAppInstall = 'C:/install/'

# Файлы для установки. Важно! Указывай названия без пробелов и +
appListInstall = {
    'Adobe-Acrobat-23.9.1.29623.apk',
    'Signal-6.35.3.134102.apk',
    'Telegram-10.1.3-(Android4.4,arm64).apk',
    'WhatsApp_v.2.23.19.84(231984004)(5.0-14.0)(arm64-8a).apk',
    'Яндекс.Браузер_v.23.9.4.86(1918436706)(7.0-14.0)(arm64-8a).apk',
    'MyOffice-Documents-v.2.6.1.apk'
}
# Функция удаления приложений из списка
def delApp():
    for app in appListDel:
        commandCheck = 'adb shell pm list packages ' + app
        returned_output = str(subprocess.check_output(commandCheck))
        print(f'│ ► Выполняется поиск: {app} ')
        if (returned_output.__contains__(app)):
            print(f'│   ► Начинаю удаление: {app}')
            commandDel = 'adb shell pm uninstall -k --user 0 ' + app
            subprocess.run(commandDel,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f'│    ► Удаление {app} завершено')
            print('├────────────────────────────────────────────')
            time.sleep(0.5)
        else:
            print(f'│   ► {app} тут нет ')
            print('├────────────────────────────────────────────')
            time.sleep(0.5)
# Функция установки приложений
def installApp():
    for app in appListInstall:
        commandInstall = 'adb install ' + pathAppInstall + app
        print(f'│ Идет установка {app}')
        subprocess.run(commandInstall,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Отключение режима разработчика (эксперементальная)
def devOff():
    commandDevOff = 'adb shell settings put global development_settings_enabled 0'
    commandDebagOff = 'adb shell settings put global adb_enabled 0'
    subprocess.run(commandDevOff, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(commandDebagOff, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# ----------------------

print('v.1.1 (13.10.2023)')
print()
print('Скрипт предназначен для автоматического удаления и установки приложений на телефон Samsung А34 G5 через ADB')
print('Root не требуется, перед началом активируйте режим разработчика и отладку через USB!')
input("Нажмите Enter для продолжения...")
print('┌────────────────────────────────────────────')
print('│ Начало процедуры удаления приложений')
delApp()
print('│ Удаление заверешено')
print('├────────────────────────────────────────────')
print('│ Начало установки приложений')
installApp()
print('├────────────────────────────────────────────')
print('│ Установка завершена')
print('├────────────────────────────────────────────')
devOff()
print('│ Режим разработчика отключен')
print('└────────────────────────────────────────────')
input("Нажмите Enter для выхода...")
exit()
