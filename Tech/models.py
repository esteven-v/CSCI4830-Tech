from django.db import models

class Amiibo(models.Model):
    Condtion_CHOICES = [
        ('box', 'BOX'),
        ('not_box', 'Not in BOX'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    is_owned = models.BooleanField(default=True)
    condition_status = models.CharField(
        max_length = 15,
        choices = Condtion_CHOICES,
        default = 'not_box'
    )
    


    def __str__(self):
        return self.name
