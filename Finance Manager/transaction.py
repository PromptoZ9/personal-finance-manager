class Transaction:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }
    
    @staticmethod
    def from_dict(data):
        return Transaction(data["date"], data["category"], data["description"], data["amount"])