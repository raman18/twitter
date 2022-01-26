from django.db import models

class User(models.Model):
    class Meta:
        db_table = "users"
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    text = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)
