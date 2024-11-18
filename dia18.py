#coding: utf-8

def Demo_Max():
    vet = [-4, 12 ,0 ,3]
    nome = "Igor"
    dic = {"Igor": 18,"Xenia": 13, "Ana Julia": 16, "Rafael": 21}
    print(f"O maior valor é {max(vet)}")
    print(f"A letra mais adiantada de {nome} é {max(nome)}")
    print(f"Metrica no dicionário: {max(dic)}")



def MediaAluno(p1, p2, p3, p4, Nome = None, Idade = None):
    media = (p1+p2+p3+p4)/4
    if Nome!=None:
        print("A média do aluno", Nome," é ", media)
    if Idade!=None:
        print("A idade do aluno é", Idade)
    return media














if __name__=="__main__":
    Demo_Max()
    media = MediaAluno(2,5,7,8, Nome = "Claudio Peixoto", Idade = 19)
    print(media)