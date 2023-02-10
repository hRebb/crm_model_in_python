"""Module to generate random users"""
import faker

import logging
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent

logging.basicConfig(filename=FILE_PATH / 'users.log', level=logging.DEBUG)

fake = faker.Faker()

# Créer une fonction "get_user" pour générer un utilisateur
def get_user():
    """Generate a random user""

    Returns:
        str: user
    """
    logging.info("Generating a random user")
    return f"{fake.first_name()} {fake.last_name()}"

# Créer une fonction " get_users" pour générer tous les utilisateurs
def get_users(n):
    """Generate a list of users

    Args:
        n (int): numbers of users

    Returns:
        list[str]: a list of users
    """
    logging.info('Generating {} users'.format(n))
    return [get_user() for _ in range(n)]

# Créer une fonction "delete_user" pour supprimer un utilisateur
def delete_user(user_id):
    """Little helper function to delete a user

    Args:
        user_id (int): the id of the user to delete

    Returns:
        List[str]: the updated list of users
    """
    logging.info("Deleting user {}".format(user_id))
    return f"User {user_id} deleted"
