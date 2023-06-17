from django.db import models
# from django.db import models

class book(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    tittle=models.CharField(max_length=50)
    publisher=models.CharField(max_length=100)
    year=models.IntegerField()
    status=models.CharField(max_length=20)
    roll = models.IntegerField()

    def __str__(self):
        return self.name
        return self.email
        return self.tittle
        return self.publisher
        return self.year
        return self.status
        return self.roll

    

# # Create your models here.

