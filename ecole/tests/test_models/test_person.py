"""
Tests unitaires de la classe abstraite Person.
On utilise une classe concrète fictive pour tester.
"""

from models.person import Person
from models.address import Address


class DummyPerson(Person):
    """Classe concrète pour tester Person."""
    pass


def test_person_creation():
    """
    Vérifie l'initialisation d'une personne.
    """
    person = DummyPerson("Jean", "Dupont", 30)

    assert person.first_name == "Jean"
    assert person.last_name == "Dupont"
    assert person.age == 30
    assert person.address is None


def test_person_str_without_address():
    """
    Vérifie le __str__ sans adresse.
    """
    person = DummyPerson("Jean", "Dupont", 30)

    assert str(person) == "Jean Dupont (30 ans)"


def test_person_str_with_address():
    """
    Vérifie le __str__ avec adresse.
    """
    person = DummyPerson("Jean", "Dupont", 30)
    person.address = Address("10 rue A", "Paris", 75000)

    assert "Paris" in str(person)