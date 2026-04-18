"""
Tests unitaires de la classe School (couche métier).

Objectifs :
- tester les méthodes d'ajout
- tester l'affichage
- tester l'initialisation du jeu de données (init_static)

Ces tests utilisent pytest et pytest-mock.
"""

from datetime import date
from business.school import School
from models.course import Course
from models.teacher import Teacher
from models.student import Student


def test_school_creation():
    """
    Vérifie qu'une école est créée avec des listes vides.
    """
    school = School()

    assert school.courses == []
    assert school.teachers == []
    assert school.students == []


def test_add_course():
    """
    Vérifie l'ajout d'un cours dans la liste des cours.
    """
    school = School()
    course = Course("Python", date(2024, 1, 1), date(2024, 2, 1))

    school.add_course(course)

    assert course in school.courses
    assert len(school.courses) == 1


def test_add_teacher():
    """
    Vérifie l'ajout d'un enseignant.
    """
    school = School()
    teacher = Teacher("Jean", "Dupont", 35, date(2023, 9, 1))

    school.add_teacher(teacher)

    assert teacher in school.teachers
    assert len(school.teachers) == 1


def test_add_student():
    """
    Vérifie l'ajout d'un élève.
    """
    school = School()
    student = Student("Paul", "Martin", 12)

    school.add_student(student)

    assert student in school.students
    assert len(school.students) == 1


def test_display_courses_list(mocker):
    """
    Vérifie que la méthode display_courses_list affiche bien les cours.

    On mock print pour éviter un affichage réel en console.
    """
    school = School()

    course = Course("Mathématiques", date(2024, 1, 1), date(2024, 2, 1))
    student = Student("Paul", "Martin", 12)

    course.add_student(student)
    school.add_course(course)

    mocked_print = mocker.patch("builtins.print")

    school.display_courses_list()

    assert mocked_print.called
    assert mocked_print.call_count >= 2


def test_init_static_creates_expected_data():
    """
    Vérifie que init_static crée les données principales attendues.
    """
    Student.students_nb = 0  # reset compteur global

    school = School()
    school.init_static()

    # Données prévues par l'énoncé / code source
    assert len(school.students) == 3
    assert len(school.courses) == 8
    assert len(school.teachers) == 6


def test_init_static_students_have_addresses():
    """
    Vérifie que les élèves créés possèdent bien une adresse.
    """
    Student.students_nb = 0

    school = School()
    school.init_static()

    for student in school.students:
        assert student.address is not None


def test_init_static_courses_have_teachers():
    """
    Vérifie que chaque cours a bien un enseignant affecté.
    """
    Student.students_nb = 0

    school = School()
    school.init_static()

    for course in school.courses:
        if course.teacher is None:
            print("Bug !")
        assert course.teacher is not None


def test_init_static_some_students_have_courses():
    """
    Vérifie que les élèves suivent au moins un cours.
    """
    Student.students_nb = 0

    school = School()
    school.init_static()

    assert any(len(student.courses_taken) > 0 for student in school.students)