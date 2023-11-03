class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def lecionar_curso(self, curso):
        self.cursos.append(curso)

    def listar_cursos_lecionados(self):
        return self.cursos


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None

    def designar_professor(self, professor):
        self.professor = professor
        professor.lecionar_curso(self)

    def get_professor(self):
        return self.professor.nome if self.professor else "Nenhum professor designado"


class Universidade:
    def __init__(self):
        self.cursos = {} 
        self.professores = {}  

    def designar_professor_para_curso(self, curso, professor):
  
        self.cursos[curso] = professor
    
        if professor in self.professores:
            self.professores[professor].append(curso)
        else:
            self.professores[professor] = [curso]

    def listar_cursos_lecionados_por_professor(self, professor):

        if professor in self.professores:
            return self.professores[professor]
        else:
            return []

universidade = Universidade()
curso1 = "Matemática"
curso2 = "História"
professor1 = "João"
professor2 = "Maria"

universidade.designar_professor_para_curso(curso1, professor1)
universidade.designar_professor_para_curso(curso2, professor1)

cursos_do_professor1 = universidade.listar_cursos_lecionados_por_professor(professor1)
print(f"Cursos lecionados pelo {professor1}: {cursos_do_professor1}")



