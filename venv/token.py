class Token():

    def __init__(self, tokentype, token_name, info, text):
        self.tokentype = tokentype
        self.token_name = token_name
        self.info = info
        self.text = text

    def __contains__(self, item):
        return True if self.token_name == item.token_name else False

    def get_type(self):
        return self.tokentype

    def get_name(self):
        return self.token_name

    def get_info(self):
        return self.info

    def get_text(self):
        return self.text

    def __str__(self):
        stype = "TYPE: " + str(self.tokentype) + "\n"
        stext = "TEXT: " + self.text + "\n"
        swidth = "WIDTH: " + str(self.info["width"]) + "\n"
        sheight = "HEIGHT: " + str(self.info["height"]) + "\n"
        sbg = "BACKGROUND: " + self.info["bg"] + "\n"
        sfg = "FOREGROUND: " + self.info["fg"] + "\n"

        return stype + stext + swidth + sheight + sbg + sfg
