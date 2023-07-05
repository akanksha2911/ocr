from django.db import models
import os
from uuid import uuid4


class Upload(models.Model):
    text_Img = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.img_name

class SetTimer(models.Model):
    setTimer = models.IntegerField()

    
