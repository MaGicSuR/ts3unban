import winreg
import random

class Spoofer():
    def __init__(self, path) -> None:
        self.path = path
        self.reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        self.key = winreg.OpenKey(self.reg, self.path, access=winreg.KEY_ALL_ACCESS)
        self.keys_len = winreg.QueryInfoKey(self.key)[1]
        self.pid = winreg.QueryValueEx(self.key, 'ProductId')[0]
        print('Spoofer Initialized')

    def make_copy(self) -> None:
        with open('pid_backup_key.txt', 'w+') as file:
            file.write(self.pid)
            print('Key backup created!')
        file.close()

    def get_random(self) -> None:
        chars = ['A',
        'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'U', 'P', 'R', 'S', 'T', 'W', 'Y', 'Z',
        '1','2', '3', '4', '5', '6', '7', '8', '9', '0']
        numbers = ['1','2', '3', '4', '5', '6', '7', '8', '9', '0']

        v0 = ''.join(random.sample(numbers, 5))
        v1 = ''.join(random.sample(numbers, 5))
        v2 = ''.join(random.sample(numbers, 5))
        v3 = ''.join(random.sample(chars, 5))

        new_pid = f'{v0}-{v1}-{v2}-{v3}'
        return new_pid

    def set_value(self) -> None:
        new_key = self.get_random()
        try:
            if self.pid != new_key:
                winreg.SetValueEx(self.key, 'ProductId', 0, winreg.REG_SZ, new_key)
        except Exception as err:
            print(err)

        print(f'Old key: {self.pid}\nNew key: {new_key}')


if __name__ == '__main__':
    print('Remember to run as admin!')
    try:
        sp = Spoofer('SOFTWARE\Microsoft\Windows NT\CurrentVersion')
        sp.make_copy()
        sp.set_value()
    except Exception as err:
        print(err)