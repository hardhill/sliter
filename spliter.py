from parameters import Parameters


def GetDirectoriesRaion(param):
    pass


class Application(object):
    def Start(self):
        print('====================================================================')
        print('=                     Spliter ver. 1.0                             =')
        print('====================================================================')
        params = Parameters()
        dirs_raion = GetDirectoriesRaion(params.Path())

if __name__ == '__main__':
    app = Application()
    app.Start()