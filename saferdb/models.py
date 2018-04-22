from django.db import models

# Create your models here.

# from django.db import models


class Question(models.Model):

    # def __str__(self):
        # return self.DOT_Number

    cardNumber = models.IntegerField(primary_key=True, default='0')#q.DOT_Number = tr[25].contents[3].get_text(, default='0')
    cardName= models.CharField(max_length=200, default='0')#18
    cardFound= models.IntegerField(default='0')
    cardUrl= models.CharField(max_length=200, default='0')#18



class Query(models.Model):

    # def __str__(self):
        # return self.DOT_Number
    fields = models.CharField(max_length=200)
