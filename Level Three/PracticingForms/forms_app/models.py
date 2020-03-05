from django.db import models

class Suggestion(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    message = models.CharField(max_length = 2000)

    def __str__(self):
        return self.email
