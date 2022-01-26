from django.db import models
from userauth.models import User

class Update(models.Model):
    class Meta:
        db_table = "updates"
    update_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)