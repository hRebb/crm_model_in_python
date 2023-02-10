import faker

fake = faker.Faker()

# Créer une fonction "get_user" pour générer un utilisateur
def get_user():
    return f"{fake.first_name()} {fake.last_name()}"

# Créer une fonction " get_users" pour générer tous les utilisateurs
def get_users(n):
    return [get_user() for _ in range(n)]

# Créer une fonction "delete_user" pour supprimer un utilisateur
def delete_user(user_id):
    return f"User {user_id} deleted"
