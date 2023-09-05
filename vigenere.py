class Vigenere():
    def __init__(self):
        self.alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
    def compoeChave(self, chave, mensagem):
        if len(chave) < len(mensagem):
            novaChave = chave * int((len(mensagem)/len(chave)))
            if len(novaChave):
                novaChave += chave[:len(novaChave)]
            return novaChave.upper()
        return chave.upper()
 
    def criptografa(self, mensagem, chave, descriptografa = False):
        chave = self.compoeChave(chave, mensagem)
        mensagem = mensagem.replace(' ', '').upper()

        res = ''
        for index, letra in enumerate(mensagem.upper()):
            letraCifra = self.alfabeto.find(chave[index])
            alfabetoCifra = self.alfabeto[letraCifra:] + self.alfabeto[:letraCifra]
 
            if descriptografa:
                indexLetra = alfabetoCifra.find(letra)
                res += self.alfabeto[indexLetra]
            else:
                indexLetra = self.alfabeto.find(letra)
                res += alfabetoCifra[indexLetra]
 
        return res
 
    def descriptografa(self, mensagem, chave):
        return self.criptografa(mensagem, chave, True)