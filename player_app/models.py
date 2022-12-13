from django.db import models

from django.db import models

# Create your models here.

HOBBIES_CHOICES = [
        ('M', 'Music'),
        ('S', 'Sports'),
        ('R', 'Reading'),
        ('O', 'Others'),
        
    ]
class Player(models.Model):
    name = models.CharField(max_length=100)
    birthDate = models.DateField()
    country = models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    tshirtNumber=models.PositiveSmallIntegerField()
    photo=models.ImageField(upload_to='photos/', blank=True,null=True)
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices=(('F','Female'),('M','Male')),default='M')
    description=models.TextField(blank=True,null=True)
    hobbies=models.CharField(max_length=1,choices=HOBBIES_CHOICES,default='M')
    def __str__(self):
        return self.name
    class Meta:
        db_table = "player"
        verbose_name = "Player"
        verbose_name_plural = "Players"
        ordering=['name']
    def __str__(self):
        return self.name
