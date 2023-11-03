class Cabeça:
    def __init__(self, cor_olhos):
        self.cor_olhos = cor_olhos

class Boneco:
    def __init__(self, altura, peso, cor_olhos):
        self.altura = altura
        self.peso = peso
        self.cabeça = Cabeça(cor_olhos)

    def destruir(self):
       
        print(f"O boneco foi destruído!")

meu_boneco = Boneco(50, 1.5, "azul")

print(f"Altura do boneco: {meu_boneco.altura} cm")
print(f"Peso do boneco: {meu_boneco.peso} kg")
print(f"Cor dos olhos da cabeça do boneco: {meu_boneco.cabeça.cor_olhos}")


meu_boneco.destruir()

try:
    print(f"Cor dos olhos da cabeça do boneco: {meu_boneco.cabeça.cor_olhos}")
except AttributeError:
    print("A cabeça do boneco foi destruída!")
