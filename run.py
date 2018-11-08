from bearlibterminal import terminal

terminal.open()
terminal.printf(1, 1, 'Hello, world!')
terminal.printf(1, 2, "THIS IS A TEST.")
terminal.refresh()

while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()
