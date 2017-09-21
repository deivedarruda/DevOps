alunos = {}
alunos[1111]= "Alberto"
alunos[2222]= "Joana"
alunos = {1111:"Alberto", 2222:"Joana"}
alunos[2222]= "Josefa"
alunos[3333]= "Camila"
print(alunos.get(4444,"Não existe esse aluno"))

print(alunos)
for chave, valor in alunos.items():
    print("codigo:%d nome:%s"%(chave,valor))