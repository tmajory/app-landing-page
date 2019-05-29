from django.db import models

class PlusOne(models.Model):
    yes_or_no = [('y', 'yes'), ('n', 'no')]
    choise = models.CharField(
        max_length=1,
        choices=yes_or_no
    )
    data = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100)
