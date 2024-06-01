from django.db import models

class Employee(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    foto = models.ImageField(upload_to="images/", default = "static/images/blank.png")
    Nama = models.CharField(max_length = 30)
    Employment_Status = models.CharField(max_length = 10)
    Monthly_Performance = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return(f"{self.Nama} ({self.Employment_Status})")