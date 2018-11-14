import json
import os
import ctypes


def main():
    profiles = get_profiles_directories()
    for profile in profiles:
        get_posh_history_of_profile(profile)


def get_posh_history_of_profile(profile):
    path = os.path.join(profile, 'AppData/Roaming/Microsoft/Windows/PowerShell/PSReadline/ConsoleHost_history.txt')
    try:
        with open(path) as f:
            print(profile)
            hist_txt = f.read()
            with open(os.path.dirname(profile), 'w') as wf:
                json.dumps(wf)
    except Exception as e:
        print(e)


def get_profiles_directories():
    user_dir = base_profile_path()
    return [(os.path.join(base_profile_path(), d)) for d in os.listdir(user_dir)]


def base_profile_path():
    os_drive = os.getenv("SystemDrive")
    user_dir = os.path.join(os_drive, '/users/')
    return user_dir


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == '__main__':
    if is_admin():
        main()
    else:
        print('You need to run this as admin!')
