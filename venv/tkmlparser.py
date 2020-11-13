import sys


class Parser:

    def __init__(self, tkml):
        """Open the tkml file"""
        try:
            self.tkml = open(tkml, "r", encoding="utf-8")
        except FileNotFoundError as e:
            print("Could not find the file: " + tkml)
            sys.exit(0)
        finally:
            self.lineCache = []
            self.pos = 0

    def cache_lines(self):
        """Load all the lines of the file into a list"""
        """Suitable for small files"""
        self.lineCache = self.tkml.readlines()
        try:
            self.tkml.close()
        except Exception as e:
            print("Could not close source file")
            sys.exit()

    def get_next_line(self):
        return self.tkml.readline()

