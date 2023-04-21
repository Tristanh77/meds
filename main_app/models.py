from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# medication model
class Med(models.Model):
  name = models.CharField(max_length=100)
  quantity = models.IntegerField()
  perscribed = models.DateField()
  expiration = models.DateField()
  instructions = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    # display medication name
    return self.name
  
  def get_absolute_url(self):
    # returns the correct route for the detail route with the defined value of med_id
    return reverse('detail', kwargs={'med_id': self.id})


# Model for instance of taking medication 
class WhenTaken(models.Model):
  date = models.DateField()
  time = models.CharField(max_length=100)
  quantity = models.IntegerField()
  
  # Foreign Key
  med = models.ForeignKey(Med, on_delete=models.CASCADE)
  
  def __str__(self):
    # make time & date more readable
    return f"{self.date}"
  
  # orders the entries from most recent to oldest entry
  class Meta:
    ordering = ['-date', '-time']