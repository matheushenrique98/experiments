import argparse
import os
import winreg


def add_environment_variable(name, value):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_ALL_ACCESS)

        winreg.SetValueEx(key, name, 0, winreg.REG_EXPAND_SZ, value)

        winreg.CloseKey(key)

        print(f"The environment variable {name} has been added with the value {value}")
    except Exception as e:
        print(f"Error adding the environment variable: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add a permanent environment variable to the user')
    parser.add_argument('name', type=str, help='Name of the environment variable')
    parser.add_argument('value', type=str, help='Value of the environment variable')
    args = parser.parse_args()

    add_environment_variable(args.name, args.value)
