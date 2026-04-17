"""
Tests unitaires de la classe Course.
Utilisation de mocker pour isoler les dépendances.
"""

from ecole.models.course import Course
from ecole.models.teacher import Teacher
from ecole.models.student import Student
from datetime import date


def test_course_creation():
    """
    Vérifie l'initialisation d'un cours.
    """
    course = Course("Math", date(2024, 1, 1), date(2024, 6, 1))

    assert course.name == "Math"
    assert course.teacher is None
    assert course.students_taking_it == []


def test_set_teacher():
    """
    Vérifie l'affectation d'un enseignant
    """
    course = Course("Math", date(2024, 1, 1), date(2024, 6, 1))
    teacher = Teacher("Sophie", "Dubois", 41, date(2012, 9, 1))


    course.set_teacher(teacher)

    assert course.teacher == teacher
    assert course in teacher.courses_teached


def test_add_student():
    """
    Vérifie l'ajout d'un étudiant avec mock.
    """
    course = Course("Math", date(2024, 1, 1), date(2024, 6, 1))
    student = Student("Thomas", "André", 15)

    course.add_student(student)

    assert student in course.students_taking_it
    assert course in student.courses_taken


def test_course_str_without_teacher():
    """
    Vérifie l'affichage sans enseignant.
    """
    course = Course("Math", date(2024, 1, 1), date(2024, 6, 1))

    assert "pas d'enseignant" in str(course)