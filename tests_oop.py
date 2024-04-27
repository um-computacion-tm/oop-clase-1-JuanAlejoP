import unittest
from oop import Subject, Professor, Student

class TestOop(unittest.TestCase):
    def setUp(self):
        self.daniel = Professor('Daniel', '003', 'Titular')
        self.elio = Professor('Elio', '006', 'JTP')
        self.student1 = Student('Camila', '321', '21')
        self.student2 = Student('Ian', '322', '21')
        self.student3 = Student('Juan', '611', '21', 'j.patino@alumno.um.edu.ar')
        self.comp_professors = [self.daniel, self.elio]
        self.comp_students = [self.student1, self.student2, self.student3]
        self.subject = Subject('Computación', self.comp_professors, self.comp_students)

    def test_subject_constructor(self):
        self.assertEqual(self.subject.__name__, 'Computación')
        self.assertEqual(self.subject.__professors__, [self.daniel, self.elio])
        self.assertEqual(self.subject.__students__, [self.student1, self.student2, self.student3])
    
    def test_subject_change_name(self):
        self.assertEqual(self.subject.__name__, 'Computación')
        self.subject.change_name('Computación 2')
        self.assertNotEqual(self.subject.__name__, 'Computación')
        self.assertEqual(self.subject.__name__, 'Computación 2')
        
    def test_subject_get_professors(self):
        self.assertEqual(self.subject.get_professors(), self.subject.__professors__)
        self.assertEqual(self.subject.get_professors(), self.comp_professors)
        self.assertEqual(self.subject.get_professors(), [self.daniel, self.elio])

    def test_subject_get_students(self):
        self.assertEqual(self.subject.get_students(), self.subject.__students__)
        self.assertEqual(self.subject.get_students(), self.comp_students)
        self.assertEqual(self.subject.get_students(), [self.student1, self.student2, self.student3])

    def test_professor_constructor(self):
        self.assertEqual(self.daniel.__name__, 'Daniel')
        self.assertEqual(self.daniel.__file__, '003')
        self.assertEqual(self.daniel.__position__, 'Titular')
    
    def test_professor_get_name(self):
        self.assertEqual(self.elio.get_name(), self.elio.__name__)
        self.assertNotEqual(self.elio.get_name(), 'Daniel')
        self.assertEqual(self.elio.get_name(), 'Elio')

    def test_professor_get_file(self):
        self.assertEqual(self.elio.get_file(), self.elio.__file__)
        self.assertNotEqual(self.elio.get_file(), '003')
        self.assertEqual(self.elio.get_file(), '006')

    def test_professor_get_position(self):
        self.assertEqual(self.elio.get_position(), self.elio.__position__)
        self.assertNotEqual(self.elio.get_position(), 'Titular')
        self.assertEqual(self.elio.get_position(), 'JTP')

    def test_student_constructor(self):
        self.assertEqual(self.student3.__name__, 'Juan')
        self.assertEqual(self.student3.__file__, '611')
        self.assertEqual(self.student3.__age__, '21')
        self.assertEqual(self.student1.__email__, None)
        self.assertEqual(self.student3.__email__, 'j.patino@alumno.um.edu.ar')
        self.assertEqual(self.student3.__non_attendances__, 0)
        self.assertEqual(self.student3.__tutor__, None)

    def test_student_change_age(self):
        self.assertEqual(self.student3.__age__, '21')
        self.assertEqual(self.student3.change_age('22'), self.student3.__age__)
        self.assertNotEqual(self.student3.change_age('22'), '21')
        self.assertEqual(self.student3.change_age('22'), '22')

    def test_student_change_email(self):
        self.assertEqual(self.student3.__email__, 'j.patino@alumno.um.edu.ar')
        self.assertEqual(self.student3.change_email('a.patino@alumno.um.edu.ar'), self.student3.__email__)
        self.assertEqual(self.student3.change_email('a.patino@alumno.um.edu.ar'), 'a.patino@alumno.um.edu.ar')

    def test_student_add_mentor(self):
        self.assertEqual(self.student3.__tutor__, None)
        self.assertEqual(self.student3.add_mentor('Claudio'), self.student3.__tutor__)
        self.assertEqual(self.student3.add_mentor('Claudio'), 'Claudio')
        self.assertNotEqual(self.student3.add_mentor('Claudio'), None)
        
unittest.main()