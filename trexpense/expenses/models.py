from django.db import models

class Expense(models.Model):
  name = models.CharField(max_length=255)
  amount = models.IntegerField(default=0)
  date = models.DateField(null=True)

  def __str__(self):
    return f"{self.name}"
