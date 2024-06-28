class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()



class Filme(Programa): 
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)    #receber atributo da super classe(mãe)
        self.duracao = duracao

    #def imprime (self):
        #print(f"{self._nome} - {self.ano}" 
        #f" - {self.duracao}min - {self.likes} ")
    def __str__ (self):
        return f"{self._nome} - {self.ano} - {self.duracao} min - {self.likes} Likes"
           

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__ (self): 
        return f"{self.nome} - {self.ano} - {self.temporadas} temp - {self.likes} Likes"


class Playlist():
    def __init__(self, nome, midia):
        
        self.nome = nome
        self.midia = midia

    def __getitem__ (self, item): #método para iteração 
        return self.midia[item]
    
    def __len__ (self):  #método para uso de função len
        return len(self.midia)
    
    


                
vingadores = Filme("Vingadores Guerra Infinita", 2018, 160)
gameofthrones = Serie("Game Of Thrones", 2015, 8)
loki = Serie ("Loki", 2023, 2)
hobbit = Filme("Hobbit - Uma Jornada Inesperada", 2012, 169 )

gameofthrones.dar_like()
vingadores.dar_like()
hobbit.dar_like()
loki.dar_like()


ficcao = [vingadores, gameofthrones, loki, hobbit]
playlist_ficcao = Playlist("Ficção", ficcao)


print(f"Tamanho da Playlist: {len(playlist_ficcao)}")
for midia in playlist_ficcao:
    print(midia)
    




