import os


def create_alias_pycharm() -> None:
    path = os.path.expandvars(r'%USERPROFILE%\\OneDrive\\Documentos\\')

    file_path = os.path.join(path, 'Microsoft.PowerShell_profile.ps1')
    with open(file_path, 'a+') as file:
        file.write("\n")
        file.write(r'function pycharm { start "" "%USERPROFILE%\\AppData\\Local\\JetBrains\\'
                   r'Toolbox\\apps\\PyCharm-C\ch-0\231.8109.197\bin\pycharm64.exe" $args; & cd $args }')


if __name__ == '__main__':
    create_alias_pycharm()
