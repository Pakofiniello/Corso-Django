class printer:
    def __init__(self, text):
        self.text = text

    def print_text(self):
        print(self.text)

        
p = printer("Hello, World!")
p.print_text()