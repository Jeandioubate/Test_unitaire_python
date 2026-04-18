"""
Tests unitaires de la classe Student.
"""

from ecole.models.student import Student
from ecole.models.course import Course
from datetime import date


def setup_function():
    """
    Réinitialise le compteur avant chaque test.
    Important pour éviter les effets de bord.
    """
    Student.students_nb = 0


def test_student_creation():
    """
    Vérifie que le numéro étudiant est bien incrémenté.
    """
    s1 = Student("Jean", "Dupont", 20)
    s2 = Student("Marie", "Martin", 22)

    assert s1.student_nbr == 1
    assert s2.student_nbr == 2


def test_add_course():
    """
    Vérifie l'ajout bidirectionnel d'un cours.
    """
    student = Student("Jean", "Dupont", 20)
    course = Course("Math", date(2024, 1, 1), date(2024, 6, 1))

    student.add_course(course)

    assert course in student.courses_taken
    assert student in course.students_taking_it


def test_student_str():
    """
    Vérifie la représentation textuelle.
    """
    student = Student("Jean", "Dupont", 20)

    assert "n° étudiant" in str(student)