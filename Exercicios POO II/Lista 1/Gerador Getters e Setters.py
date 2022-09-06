lista = ["__nome", "__idade", "__cpf", "__iaa"]

for x in lista:
    print("def get_{}(self):".format(x))
    print("    return self.{}".format(x))

for x in lista:
    print("def set_{}(self, {}):".format(x, x))
    print("    self.{} = {}".format(x, x))

