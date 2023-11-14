from django.db import models

# Create your models here.
class profile(models.Model):
    GENDER=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    RELAGION=(
        ('Hindu','Hindu'),
        ('Muslim','Muslim'),
        ('Buddha','Buddha'),
        ('Christan','Christan'),
    )


    def __str__(self):
        return self.name
    
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    image=models.ImageField(upload_to='prof_pic/',default='def.png')
    number=models.TextField(max_length=20)
    Adress=models.CharField(max_length=20)
    gender=models.CharField(choices=GENDER,max_length=20,default='Male')
    relagion=models.CharField(choices=RELAGION,max_length=20,default='Hindu')
    