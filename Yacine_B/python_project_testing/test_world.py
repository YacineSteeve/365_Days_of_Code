"""
    Learning how to test projects in Python.
    The training project is on https://github.com/celine-m-s/le_monde_est_petit/tree/master
"""

import pytest

# Doctests

# Command line: python -m doctest -v mytests.py

def sum(a, b):
    """
    >>> a = 4
    >>> b = 7
    >>> sum(a, b)
    11
    """
    return a + b


# Pytest

# - Agent : 
#   - modifier un attribut position
#   - récupérer un attribut position
#   - assigner un dictionnaire en tant qu'attributs

# - Position :
#   - modifier un attribut longitude_degrees
#   - modifier un attribut latitude_degrees
#   - modifier un attribut longitude_degrees avec une valeur supérieure à 180 renvoie une erreur. 
#   - modifier un attribut latitide_degrees avec une valeur supérieure à 90 renvoie une erreur. 
#   - récupérer une latitude
#   - récupérer une longitude

# - Zone :
#   - trouver une zone qui contient une position
#   - ajouter un habitant dans une zone
#   - récupérer toutes les instances Zone (Zone.ZONES)
#   - récupérer la densité de population d'une zone
#   - récupérer l'agréabilité moyenne d'une zone

# - AgreeablenessGraph :
#   - récupérer un titre
#   - récupérer x_label
#   - récupérer y_label
#   - récupérer xy_values sous forme de tuples
#   - la première valeur de xy_values est la densité de population moyenne
#   - la seconde valeur de xy_values est l'agréabilité moyenne
