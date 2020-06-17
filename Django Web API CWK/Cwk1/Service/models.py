from django.db import models

# Create your models here.

class Module(models.Model):
    moduleID = models.CharField(max_length = 5)
    moduleName = models.CharField(max_length = 50)
    year = models.CharField(max_length = 5)
    semester = models.CharField(max_length = 1)
    professorID = models.CharField(max_length = 5)
    professorName = models.CharField(max_length = 35)

    def __str__(self):
        return self.moduleID


class Rating(models.Model):
    userName = models.CharField(max_length = 10)
    moduleID = models.CharField(max_length = 5)
    professorID = models.CharField(max_length = 5, default = "JE1")
    year = models.CharField(max_length = 5)
    semester = models.CharField(max_length = 1)
    ratings = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    rating = models.CharField(max_length = 5, choices = ratings)


class Users(models.Model):
    userName = models.CharField(max_length = 35)
    email = models.CharField(max_length = 35)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.userName
