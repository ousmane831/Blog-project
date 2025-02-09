from django.db import models

# Create your models here.
class POST(models.Model):
    title = models.CharField(max_length=50)
    contener = models.TextField(max_length=50)
    created_at = models.DateTimeField( auto_now_add= True)
    categorie =  models.CharField(max_length=50)
    frequence = models.CharField(max_length=50)   
    def __str__(self):
        return self.title
    

    
      
     
     
