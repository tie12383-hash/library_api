from django.db import models
from django.conf import settings

class BorrowRecord(models.Model):
    class Status(models.TextChoices):
        ISSUED = 'issued', 'Выдана'
        RETURNED = 'returned', 'Возвращена'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='borrow_records'
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE,
        related_name='borrow_records'
    )
    issued_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ISSUED
    )

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"