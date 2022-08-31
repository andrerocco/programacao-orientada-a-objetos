lista = ["fibonacci", "fatorial", "ano", "editora", "edicao", "volume"]

for x in lista:
    print("def get_{}(self):".format(x))
    print("    return self.{}".format(x))

for x in lista:
    print("def set_{}(self, {}):".format(x, x))
    print("    self.{} = {}".format(x, x))

