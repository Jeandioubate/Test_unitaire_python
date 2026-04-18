"""
Tests unitaires de la classe Address.
"""

from ecole.models.address import Address


def test_address_creation():
    """
    Vérifie que les attributs sont correctement initialisés.
    """
    address = Address("10 rue A", "Paris", 75000)

    assert address.street == "10 rue A"
    assert address.city == "Paris"
    assert address.postal_code == 75000


def test_address_str():
    """
    Vérifie la représentation textuelle de l'adresse.
    """
    address = Address("10 rue A", "Paris", 75000)

    assert str(address) == "10 rue A, 75000 Paris"