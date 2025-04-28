class DateCalculator:
    def __init__(self, year, month, day):
        self.day = day
        if month < 3:
            month += 12
            year -= 1
        self.month = month
        self.year = year
        self.K = year % 100
        self.J = year // 100

    def calculate_weekday(self):
        q = self.day
        m = self.month
        K = self.K
        J = self.J

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

# Example usage
date = DateCalculator(2005, 5, 3)
print(date.calculate_weekday())  # Output: Saturday
