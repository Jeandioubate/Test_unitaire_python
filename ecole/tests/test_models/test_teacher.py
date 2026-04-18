"""
Tests unitaires de la classe Teacher.
"""

from ecole.models.teacher import Teacher
from ecole.models.course import Course
from datetime import date


def test_teacher_creation():
    """
    Vérifie l'initialisation d'un enseignant.
    """
    teacher = Teacher("Jean", "Dupont", 40, date(2020, 1, 1))

    assert teacher.hiring_date.year == 2020
    assert teacher.courses_teached == []


def test_add_course():
    """
    Vérifie l'affectation d'un cours à un enseignant.
    """
    teacher = Teacher("Jean", "Dupont", 40, date(2020, 1, 1))
    course = Course("Math", date(2024, 1, 1), date(2024, 6, 1))

    teacher.add_course(course)

    #assert course.teacher == teacher

    assert teacher.courses_teached == [course]

    # courses_teached reste vide c'est un bug
    #assert teacher.courses_teached == []
    # Correction suggérée : teacher.courses_teached.append(course)


def test_teacher_str():
    """
    Vérifie la représentation textuelle.
    """
    teacher = Teacher("Jean", "Dupont", 40, date(2020, 1, 1))

    assert "arrivé(e) le" in str(teacher)