class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name=None, hours=None, rest_days=None, email=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name=name, hours=hours, rest_days=rest_days, email=email)

    @classmethod
    def get_email(cls, name=None, hours=None, rest_days=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name=name, hours=hours, rest_days=rest_days, email=email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment
