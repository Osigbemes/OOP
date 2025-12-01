
# ============================================================
#                       USERS CLASS
# ============================================================

class User:
    """
    Represents a single library user.
    """

    def __init__(self, username, firstname, surname, house_no, street, postcode, email, dob):
        try:
            self.username = username
            self.firstname = firstname
            self.surname = surname
            self.house_no = house_no
            self.street = street
            self.postcode = postcode
            self.email = email
            self.dob = dob
        except Exception as e:
            raise ValueError(f"Error creating user: {e}")

    # -------------- GETTER METHODS --------------
    def get_username(self): return self.username
    def get_firstname(self): return self.firstname
    def get_surname(self): return self.surname
    def get_house_no(self): return self.house_no
    def get_street(self): return self.street
    def get_postcode(self): return self.postcode
    def get_email(self): return self.email
    def get_dob(self): return self.dob

    # -------------- EDIT METHODS --------------
    def edit_firstname(self, name):
        self.firstname = name

    def edit_surname(self, name):
        self.surname = name

    def edit_email(self, email):
        self.email = email

    def edit_dob(self, dob):
        self.dob = dob
