class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"User: {self.username}, Role: {self.role}"


# Sample users (for now, hardcoded for testing purposes)
users = [
    User("admin", "admin123", "Admin"),
    User("manager", "manager123", "Manager"),
    User("sales", "sales123", "Sales Staff"),
    User("inventory", "inventory123", "Inventory Staff")
]


def authenticate_user(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None
