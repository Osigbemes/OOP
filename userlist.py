from user import User


class UserList:
    """
    Manages a collection of User objects in the library system.
    Provides functionality to add, remove, search, and count users.
    """

    def __init__(self):
        """
        Constructor to create a new UserList object.
        Initializes an empty dictionary to store users.
        """
        self.users = {}  # key = username, value = User instance

    def add_user(self, user):
        """
        Adds a User object to the collection.

        :param user: User instance to be added
        """
        if not isinstance(user, User):
            raise TypeError("Only User objects can be added to UserList")

        if user.get_username() in self.users:
            raise ValueError("A user with this username already exists")

        self.users[user.get_username()] = user

    def remove_user_by_firstname(self, firstname):
        """
        Removes a user from the collection by first name.
        If multiple users share the same first name, informs the user.
        """

        if not firstname:
            raise ValueError("First name must be provided")

        matches = [u for u in self.users.values() if u.get_firstname() == firstname]

        if len(matches) == 0:
            return "No user found with that first name."

        if len(matches) > 1:
            return "More than one user has this first name. Please remove by username."

        user_to_remove = matches[0]
        del self.users[user_to_remove.get_username()]
        return "User removed successfully."

    def count_users(self):
        """
        Returns the total number of users in the system.
        """
        return len(self.users)

    def get_user_by_username(self, username):
        """
        Returns a user's details using their username.

        :param username: Username of the user
        :return: User object if found, otherwise None
        """

        if not username:
            raise ValueError("Username must be provided")

        return self.users.get(username, None)
