import faker

fake = faker.Faker()

# Créer une fonction "get_user" pour générer un utilisateur
def get_user():
    return f"{fake.first_name()} {fake.last_name()}"

# Créer une fonction " get_users" pour générer tous les utilisateurs
def get_users(n):
    return [get_user() for _ in range(n)]

# Créer une fonction "get_identity" pour générer l'identifiant d'un utilisateur
def get_identity(user):
    user = get_user()
    user_id = fake.pyint(min_value=1, max_value=10000)
    return f"User {user_id} is {user}"

# Créer une fonction "delete_user" pour supprimer un utilisateur
def delete_user(user_id):
    return f"User {user_id} deleted"
