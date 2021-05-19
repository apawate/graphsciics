class Custom:
    def __init__(self):
        self.content = ""
    def build(self):
        nextentry = ""
        while (nextentry != "asdf"):
            nextentry = input("Enter the next line of your shape. (asdf to quit) ")
            if nextentry != "asdf":
                self.content = self.content + nextentry + "\n"
    def display(self):
        print(self.content)

