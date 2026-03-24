# 3-mashq
class User:
    users = []

    def __init__(self, name, email):
        if any(user.email == email for user in User.users):
            raise ValueError("Bu email allaqachon mavjud")

        self.name = name
        self.email = email

        User.users.append(self)

    def get_info(self):
        return f"Name: {self.name}, Email: {self.email}"

    @classmethod
    def find_user(cls, email):
        for user in cls.users:
            if user.email == email:
                return user
        return None

    @classmethod
    def delete_user(cls, email):
        user = cls.find_user(email)
        if user is None:
            raise ValueError("User topilmadi")
        cls.users.remove(user)

# 4-mashq
class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width va height 0 dan katta bo'lishi kerak")

        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height
