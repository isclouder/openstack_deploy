import os
import ConfigParser

class Config(object):
    def __init__(self, filename):
        self.file = filename
        self.parser = ConfigParser.ConfigParser()
        if not os.path.exists(self.file):
            open(self.file, 'w').close()
        self.parser.read(self.file)

    def set(self, contents):
        for section, options in contents.items():
            for option, value in options.items():
                self.parser.set(section, option, value)

    def write(self):
        self.parser.write(open(self.file, "w"))

