from django.db import models
from django.utils import dateformat


class School_details(models.Model):
    City_Choices=(('AJMER','Ajmer'),
                  ('JAIPUR','Jaipur'),
                  ('BANSWARA','Banswara'),
                  ('AJMER','Ajmer'),
                  )
    State= models.CharField(max_length=30,default='Rajasthan')
    City= models.CharField(max_length=20,choices=City_Choices,default='AJMER')
    Pin_Code=models.IntegerField()
    School_Name=models.CharField(max_length=250)





# Create your models here.
