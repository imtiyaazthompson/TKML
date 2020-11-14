from widget_type import WidgetType


# Order for packing widgets

def write_runner():
    """Main entry point source code generation"""
    runner = "def main():\n\twindow = tk.Tk()\n\twidgets = setup()\n\tfor widget in PACKING:\n\t\twidgets[" \
             "widget].pack()\n\twindow.mainloop()"
    return runner


def write_start():
    """Source code generation for statment that starts the application"""
    start = "if __name__ == '__main__':\n\tmain()"
    return start


def write_setup(tokens):
    """Source code generation for widget creation"""
    setup = "def setup():"
    callbacks = []

    for token in tokens:
        info = token.get_info()
        name = token.get_name()

        # Extract data depending on whether the widget is a label/button or entry
        # TODO: cases for different widgets
        if token.get_type() == WidgetType.LABEL or token.get_type == WidgetType.BUTTON:
            width = int(info["width"]) if info["width"] != "" else 0
            height = int(info["height"]) if info["height"] != "" else 0
            bg = info["bg"] if info["bg"] != "" else -1
            fg = info["fg"] if info["fg"] != "" else -1
        elif token.get_type() == WidgetType.ENTRY:
            width = int(info["width"]) if info["width"] != "" else 0
            bg = info["bg"] if info["bg"] != "" else -1
            fg = info["fg"] if info["fg"] != "" else -1

        parent = token.get_parent()
        if token.get_type() == WidgetType.LABEL:
            # Deal with different cases of back/foreground information
            if bg == - 1 and fg != -1:
                # Check if this widget was defined in a frame
                if parent is None:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Label(text='{token.get_text()}',width={width},height={height},fg={fg})",
                        setup)
                else:
                    # If this widget was defined in a frame, set the master appropriately
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Label(master=widgets[\"{parent}\"],text='{token.get_text()}',width={width},"
                        f"height={height},fg={fg})", setup)
            elif fg == -1 and bg != -1:
                if parent is None:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Label(text='{token.get_text()}',width={width},height={height},bg={bg})",
                        setup)
                else:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Label(master=widgets[\"{parent}\"]text='{token.get_text()}',width={width},"
                        f"height={height},bg={bg})", setup)
            elif bg == -1 and fg == -1:
                if parent is None:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Label(text='{token.get_text()}',width={width},height={height})", setup)
                else:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Label(master=widgets[\"{parent}\"],text='{token.get_text()}',width={width},"
                        f"height={height})", setup)
            else:
                if parent is None:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Label(text='{token.get_text()}',width={width},"
                        f"height={height},bg={bg},fg={fg})", setup)
                else:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Label(master=widgets[\"{parent}\"],text='{token.get_text()}',width={width},"
                        f"height={height},bg={bg},fg={fg})", setup)
        elif token.get_type() == WidgetType.BUTTON:
            callback_name = name + "_callback"
            callback = "def " + callback_name + "():\n\t# Callback for this button when clicked\n\tpass\n\n"
            callbacks.append(callback)
            if bg == - 1 and fg != -1:
                if parent is None:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Button(text='{token.get_text()}',width={width},height={height},fg=\"{fg}\","
                        f"command=lambda: {callback_name}('''Your arguments go here'''))", setup)
                else:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Button(master=widgets[\"{parent}\"],text='{token.get_text()}',width={width},"
                        f"height={height},fg=\"{fg}\",command=lambda: {callback_name}('''Your arguments go here'''))", setup)
            elif fg == -1 and bg != -1:
                if parent is None:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Button(text='{token.get_text()}',width={width},height={height},bg=\"{bg}\","
                        f"command=lambda: {callback_name}('''Your arguments go here'''))", setup)
                else:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Button(master=widgets[\"{parent}\"],text='{token.get_text()}',width={width},"
                        f"height={height},bg=\"{bg}\",command=lambda: {callback_name}('''Your arguments go here'''))", setup)
            elif bg == -1 and fg == -1:
                if parent is None:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Button(text='{token.get_text()}',width={width},height={height},"
                        f"command=lambda: {callback_name}('''Your arguments go here'''))", setup)
                else:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Button(master=widgets[\"{parent}\"],text='{token.get_text()}',width={width},"
                        f"height={height},command=lambda: {callback_name}('''Your arguments go here'''))", setup)
            else:
                if parent is None:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Button(text='{token.get_text()}',width={width},height={height},bg=\"{bg}\","
                        f"fg=\"{fg}\",command=lambda: {callback_name}('''Your arguments go here'''))", setup)
                else:
                    setup = insert_statement(
                        f"widgets['{name}'] = tk.Button(master=widgets[\"{parent}\"],text='{token.get_text()}',width={width},"
                        f"height={height},bg=\"{bg}\",fg=\"{fg}\",command=lambda: {callback_name}('''Your arguments go here'''))",
                        setup)
        elif token.get_type() == WidgetType.ENTRY:
            if bg == - 1 and fg != -1:
                if parent is None:
                    setup = insert_statement(f"widgets['{name}'] = tk.Entry(fg=\"{fg}\",width={width})", setup)
                else:
                    setup = insert_statement(f"widgets['{name}'] = tk.Entry(master=widgets[\"{parent}\"],fg=\"{fg}\","
                                             f"width={width})", setup)
            elif fg == -1 and bg != -1:
                if parent is None:
                    setup = insert_statement(f"widgets['{name}'] = tk.Entry(bg=\"{bg}\",width={width})", setup)
                else:
                    setup = insert_statement(f"widgets['{name}'] = tk.Entry(master=widgets[\"{parent}\"],bg=\"{bg}\","
                                             f"width={width})", setup)
            elif bg == -1 and fg == -1:
                if parent is None:
                    setup = insert_statement(f"widgets['{name}'] = tk.Entry(width={width})", setup)
                else:
                    setup = insert_statement(f"widgets['{name}'] = tk.Entry(master=widgets[\"{parent}\"],width={width})", setup)
            else:
                if parent is None:
                    setup = insert_statement(f"widgets['{name}'] = tk.Entry(fg=\"{fg}\",bg=\"{bg}\",width={width})", setup)
                else:
                    setup = insert_statement(f"widgets['{name}'] = tk.Entry(master=widgets[\"{parent}\"],fg=\"{fg}\","
                                             f"bg=\"{bg}\",width={width})", setup)
            if token.get_text() != "":
                # If the entry widget had some text info, set the default entry of the field
                setup = insert_statement(f"widgets['{name}'].insert(0,\"{token.get_text()}\")", setup)
        elif token.get_type() == WidgetType.STARTFRAME:
            # If the current widget indicates a start frame (Highest precedence)
            # Also save the current frame
            # TODO: Use a stack to save the current frame
            if parent is None:
                setup = insert_statement(f"widgets[\"{name}\"] = tk.Frame()", setup)
                # current_frame.insert(0, name)
            else:
                setup = insert_statement(f"widgets[\"{name}\"] = tk.Frame(master=widgets[\"{parent}\"])", setup)
                # current_frame.insert(0, name)
        elif token.get_type() == WidgetType.ENDFRAME:
            #current_frame.pop(0)
            pass

    callbacks.append("def get_text_from(entry):\n\treturn entry.get()\n\n")
    setup = insert_statement("return widgets", setup)
    return setup, callbacks


def insert_statement(statement, block):
    """Append a string to an existing line within a generated code block"""
    block += "\n\t" + statement
    return block


def gen_source(tokens, packing):
    """Write the fully generated source code to file: template.py"""
    imports = "import tkinter as tk\n\n\nwidgets = {}"
    setup, callbacks = write_setup(tokens)
    runner = write_runner()
    start = write_start()
    with open("template.py", "w") as src:
        src.write(imports + "\n\n")
        src.write("PACKING = " + str(packing) + "\n\n")
        for callback in callbacks:
            src.write(callback)

        src.write(setup + "\n\n" + runner + "\n\n" + start + "\n\n")
