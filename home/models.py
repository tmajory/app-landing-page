from django.db import models

class PlusOne(models.Model):
    yes_or_no = [('y', 'yes'), ('n', 'no')]
    choice = models.CharField(
        max_length=1,
        choices=yes_or_no
    )
    email = models.EmailField(max_length=100)
    feedback = models.TextField(    )
