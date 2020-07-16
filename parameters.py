import configparser


class Parameters(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("split.ini",encoding='utf8')
    def Path(self):
        return self.config['DEFAULT']['path']