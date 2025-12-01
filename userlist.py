
# ============================================================
#                       USERLIST CLASS
# ============================================================

from user import User


class UserList:
    """
    Stores multiple User objects.
    """

    def __init__(self):
        self.users = {}   # key = username, value = User instance

    def add_user(self, user: User):
        self.users[user.username] = user

    def remove_user_by_firstname(self, firstname):
        matches = [u for u in self.users.values() if u.firstname == firstname]

        if len(matches) == 0:
            return "No user found with that first name."

        if len(matches) > 1:
            return "More than one user has this first name. Please specify username."

        # Remove the matching user
        user_to_remove = matches[0]
        del self.users[user_to_remove.username]
        return "User removed successfully."

    def count_users(self):
        return len(self.users)

    def get_user_by_username(self, username):
        return self.users.get(username, None)