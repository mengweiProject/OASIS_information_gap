"""
被@property修饰的方法
"""


class Man:
    def __init__(self):
        print('init----------')
        self.name = 'wei'
        self.weight = 100
        self.__activity = None

    @property
    def activity(self):
        print('activity----------')
        self.__activity = 'play basketball'
        print('play basketball')
        return self.__activity


if __name__ == '__main__':
    print('start...')
    m = Man()
    print('middle...')
    print(m.name)
    print('end...')