class Token:
    """
       A Tkinter widget

       ...

       Attributes
       ----------
       widget_type : WidgetType
           the type of the tkinter widget
       widget_name : str
           unique name of the widget
       info : dict
           widget info such as width, height etc. Varies depending on the type of widget

       Methods
       -------
       get_type():
           get the type of the widget
       get_name():
            get the name of the widget
       get_info():
            get the widget information
       get_text():
            get the text label of the widget
       """
    def __init__(self, widget_type, widget_name, info, text):
        self.widget_type = widget_type
        self.widget_name = widget_name
        self.info = info
        self.text = text
        self.parent = None

    def __eq__(self, item):
        return True if self.widget_name == item.widget_name else False

    def get_type(self):
        return self.widget_type

    def get_name(self):
        return self.widget_name

    def get_info(self):
        return self.info

    def get_text(self):
        return self.text

    def get_parent(self):
        return self.parent

    def __str__(self):
        stype = "TYPE: " + str(self.widget_type) + "\n"
        stext = "TEXT: " + self.text + "\n"
        swidth = "WIDTH: " + str(self.info["width"]) + "\n"
        sheight = "HEIGHT: " + str(self.info["height"]) + "\n"
        sbg = "BACKGROUND: " + self.info["bg"] + "\n"
        sfg = "FOREGROUND: " + self.info["fg"] + "\n"

        return stype + stext + swidth + sheight + sbg + sfg
