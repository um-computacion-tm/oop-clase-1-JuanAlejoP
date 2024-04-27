#Clase Materia
class Subject:
    def __init__(self, name, professors, students):
        self.__name__ = name
        self.__professors__ = professors
        self.__students__ = students

    def change_name(self, name):
        self.__name__ = name

    def get_professors(self):
        return self.__professors__

    def get_students(self):
        return self.__students__

#Clase Profesor
class Professor:
    def __init__(self, name, file, position):
        self.__name__ = name
        self.__file__ = file
        self.__position__ = position

    def get_name(self):
        return self.__name__
    
    def get_file(self):
        return self.__file__

    def get_position(self):
        return self.__position__

#Clase Alumno
class Student:
    def __init__(self, name, file, age, email=None):
        self.__name__ = name
        self.__file__ = file
        self.__age__ = age
        self.__email__ = email
        self.__non_attendances__ = 0
        self.__tutor__ = None

    def change_age(self, age):
        self.__age__ = age
        return self.__age__

    def change_email(self, email):
        self.__email__ = email
        return self.__email__

    def add_mentor(self, tutor):
        self.__tutor__ = tutor
        return self.__tutor__

#Objetos Alumno
student1 = Student(name='Camila', file='321', age='21')
student2 = Student(name='Ian', file='322', age='21')

#Ejecución ejemplo
def main():
    print(f'Instancia de la clase Alumno: {student1.__name__}.')
    student1.add_mentor('Claudio')
    print(f'El mentor de {student1.__name__} es {student1.__tutor__}.')
    student2.change_age(19)
    print(f'La edad de {student2.__name__} es {student2.__age__} años.')

main()