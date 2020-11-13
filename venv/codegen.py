from tokentype import TokenType


def write_runner():
    runner = "def main():\n\twindow = tk.Tk()\n\twidgets = setup()\n\tfor key in widgets.keys():\n\t\twidgets[" \
             "key].pack()\n\twindow.mainloop()"
    return runner


def write_start():
    start = "if __name__ == '__main__':\n\tmain()"
    return start


def write_setup(tokens):
    setup = "def setup():"

    setup = insert_statement("widgets = {}", setup)
    for token in tokens:
        info = token.get_info()
        name = token.get_name()
        print(info)
        print(name)
        width = int(info["width"]) if info["width"] != "" else 0
        height = int(info["height"]) if info["height"] != "" else 0
        bg = info["bg"] if info["bg"] != "" else -1
        fg = info["fg"] if info["fg"] != "" else -1

        if token.get_type() == TokenType.LABEL:
            if bg == - 1 and fg != -1:
                setup = insert_statement(
                    f"widgets['{name}'] = tk.Label(text='{token.get_text()}',width={width},height={height},fg={fg})",
                    setup)
            elif fg == -1 and bg != -1:
                setup = insert_statement(
                    f"widgets['{name}'] = tk.Label(text='{token.get_text()}',width={width},height={height},bg={bg})",
                    setup)
            elif bg == -1 and fg == -1:
                setup = insert_statement(
                    f"widgets['{name}'] = tk.Label(text='{token.get_text()}',width={width},height={height})", setup)
            else:
                setup = insert_statement(
                    f"widgets['{name}'] = tk.Label(text='{token.get_text()}',width={width},height={height},bg={bg},"
                    f"fg={fg})", setup)
        elif token.get_type() == TokenType.BUTTON:
            if bg == - 1 and fg != -1:
                setup = insert_statement(
                    f"widgets['{name}'] = tk.Button(text='{token.get_text()}',width={width},height={height},fg={fg})",
                    setup)
            elif fg == -1 and bg != -1:
                setup = insert_statement(
                    f"widgets['{name}'] = tk.Button(text='{token.get_text()}',width={width},height={height},bg={bg})",
                    setup)
            elif bg == -1 and fg == -1:
                setup = insert_statement(
                    f"widgets['{name}'] = tk.Button(text='{token.get_text()}',width={width},height={height})", setup)
            else:
                setup = insert_statement(
                    f"widgets['{name}'] = tk.Button(text='{token.get_text()}',width={width},height={height},bg={bg},"
                    f"fg={fg})", setup)

    setup = insert_statement("return widgets", setup)
    return setup


def insert_statement(statement, block):
    block += "\n\t" + statement
    return block


def gen_source(tokens):
    imports = "import tkinter as tk"
    setup = write_setup(tokens)
    runner = write_runner()
    start = write_start()
    with open("template.py", "w") as src:
        src.write(imports + "\n\n" + setup + "\n\n" + runner + "\n\n" + start)
