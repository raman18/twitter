from django.db import models
from userauth.models import User

class UserFollower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="user_id", related_name="user")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, to_field="user_id", related_name="follower")
    class Meta:
        db_table = "userfollowers"
        unique_together = (("user", "follower"),)
