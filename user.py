class User:
    """
    Represents a single library user.
    Stores personal and contact details of the user.
    """

    def __init__(self, username, firstname, surname, house_no, street, postcode, email, dob):
        """
        Constructor to create a new user.
        Performs basic validation on provided values.
        """

        # Validate username
        if not username or not isinstance(username, str):
            raise ValueError("Username must be a non-empty string")

        # Validate email
        if "@" not in email:
            raise ValueError("Invalid email address")

        # Validate date of birth
        if not isinstance(dob, str):
            raise ValueError("Date of birth must be a string (e.g. YYYY-MM-DD)")

        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_no = house_no
        self.street = street
        self.postcode = postcode
        self.email = email
        self.dob = dob

    # ---------------- GETTER METHODS ----------------
    def get_username(self):
        """Return the username"""
        return self.username

    def get_firstname(self):
        """Return the user's first name"""
        return self.firstname

    def get_surname(self):
        """Return the user's surname"""
        return self.surname

    def get_house_no(self):
        """Return the house number"""
        return self.house_no

    def get_street(self):
        """Return the street name"""
        return self.street

    def get_postcode(self):
        """Return the postcode"""
        return self.postcode

    def get_email(self):
        """Return the email address"""
        return self.email

    def get_dob(self):
        """Return the date of birth"""
        return self.dob

    # ---------------- EDIT METHODS ----------------
    def edit_firstname(self, firstname):
        """Edit the user's first name"""
        if not firstname:
            raise ValueError("First name cannot be empty")
        self.firstname = firstname

    def edit_surname(self, surname):
        """Edit the user's surname"""
        if not surname:
            raise ValueError("Surname cannot be empty")
        self.surname = surname

    def edit_email(self, email):
        """Edit the user's email address"""
        if "@" not in email:
            raise ValueError("Invalid email address")
        self.email = email

    def edit_dob(self, dob):
        """Edit the user's date of birth"""
        if not dob:
            raise ValueError("Date of birth cannot be empty")
        self.dob = dob
        
    def edit_house_number(self, house_no):
        self.house_no = house_no

    def edit_street_name(self, street):
        self.street = street

    def edit_postcode(self, postcode):
        self.postcode = postcode

