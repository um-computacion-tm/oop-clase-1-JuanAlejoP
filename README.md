# Juan Alejo Patiño - OOP

##### La programación orientada a objetos (OOP) es un paradigma de programación que utiliza "objetos" para diseñar aplicaciones y programas. Cada objeto es una instancia de una "clase", que define un conjunto de atributos y métodos que operan en esos atributos.

### El archivo `oop.py` contiene definiciones de clases y ejemplos de objetos en Python.

#### Clase Materia (`Subject`)
##### La clase `Subject` representa una materia y tiene los siguientes atributos y métodos:
##### `__init__(self, name, professors, students)`: Constructor que inicializa una materia con un nombre, una lista de profesores y una lista de estudiantes.
##### `change_name(self, name)`: Método para cambiar el nombre de la materia.
##### `get_professors(self)`: Método para obtener la lista de profesores.
##### `get_students(self)`: Método para obtener la lista de estudiantes.

#### Clase Profesor (`Professor`)
##### La clase `Professor` representa a un profesor y tiene los siguientes atributos y métodos:
##### `__init__(self, name, file, position)`: Constructor que inicializa un profesor con un nombre, un legajo, y un cargo.
##### `get_name(self)`: Método para obtener el nombre del profesor.
##### `get_file(self)`: Método para obtener el legajo del profesor.
##### `get_position(self)`: Método para obtener el cargo del profesor.

#### Clase Alumno (`Student`)
##### La clase `Student` representa a un alumno y tiene los siguientes atributos y métodos:
##### `__init__(self, name, file, age, email=None)`: Constructor que inicializa un alumno con un nombre, un legajo, una edad y un correo electrónico (opcional).
##### `change_age(self, age)`: Método para cambiar la edad del alumno.
##### `change_email(self, email)`: Método para cambiar el correo electrónico del alumno.
##### `add_mentor(self, tutor)`: Método para agregar un mentor al alumno.

### En el archivo `tests_oop.py` se encuentran los casos de testeo.