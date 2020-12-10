from django.db import models
from django.contrib.auth.models import User #User-Modell wird von Django zur Verfügung gestellt
from PIL import Image

# Create your models here.


class Profile(models.Model): # erbt von import. Modell
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 1:1 Beziehung: User <-> Profil, Cascade: wenn User gelöscht wird, dann lösche auch das Profil (Einwegfunktion), wenn Profil gelöscht wird, dann wird der User nicht gelöscht
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # default und dir Einstellung

    def __str__(self):
        return f'{self.user.username} Profile'  # Profil mit dem vorhandenen Username wird ausgegeben 

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
