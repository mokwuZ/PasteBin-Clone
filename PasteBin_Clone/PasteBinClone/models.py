from django.db import models

class usersText(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    userText = models.TextField()

    def __str__(self):
        return self.userName 