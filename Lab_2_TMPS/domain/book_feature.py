
class BookDiscountDecorator:
    def __init__(self, book, discount):
        self.book = book
        self.discount = discount

    @property
    def discounted_price(self):
        return self.book.price * (1 - self.discount)

    def __str__(self):
        return f"{self.book.title} by {self.book.author} - Discounted Price: ${self.discounted_price:.2f}"
