import winreg
import random

class Spoofer():
    def __init__(self, path) -> None:
        self.path = path
        self.reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        self.key = winreg.OpenKey(self.reg, self.path, access=winreg.KEY_ALL_ACCESS)
        self.keys_len = winreg.QueryInfoKey(self.key)[1]
        self.pID = winreg.QueryValueEx(self.key, 'ProductId')[0]
        print('Spoofer Initialized')

    def make_copy(self) -> None:
        with open('pid_backup_key.txt', 'w+') as file:
            file.write(self.pID)
            print('Key backup created!')
        file.close()

    def set_value(self) -> None:
        strings = ['A',
        'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'U', 'P', 'R', 'S', 'T', 'W', 'Y', 'Z',
        '1','2', '3', '4', '5', '6', '7', '8', '9', '0']
        numbers = ['1','2', '3', '4', '5', '6', '7', '8', '9', '0']
        
        val1 = ''.join(random.sample(numbers, 5))
        val2 = ''.join(random.sample(numbers, 5))
        val3 = ''.join(random.sample(numbers, 5))
        val4 = ''.join(random.sample(strings, 5))
        
        new_pID = f'{val1}-{val2}-{val3}-{val4}'
        try:
            if self.pID != new_pID:
                winreg.SetValueEx(self.key, 'ProductId', 0, winreg.REG_SZ, f'{val1}-{val2}-{val3}-{val4}')
        except Exception as err:
            print(err)

        print(f'Old key: {self.pID}\nNew key: {new_pID}')


if __name__ == '__main__':
    print('Remember to run as admin!')
    try:
        sp = Spoofer('SOFTWARE\Microsoft\Windows NT\CurrentVersion')
        sp.make_copy()
        sp.set_value()
    except Exception as err:
        print(err)