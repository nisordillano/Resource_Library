from django.db import models

class Purpose(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class User(models.Model):
    Name = models.CharField(max_length=500)
    Link = models.CharField(max_length=500)
    Notes = models.CharField(max_length=500)
    Purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    
    # Add any other fields or methods as needed
