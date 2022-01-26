import base64
from datetime import datetime

import pytz
from Crypto import Random
from django.db import models

from userauth.model.user_auth_model import User


class AccessToken(models.Model):
    """
    Stores access tokens for individual users.
    """

    class Meta:
        db_table = "access_tokens"

    user = models.ForeignKey(
        User,
        db_column="user_id",
        on_delete=models.CASCADE,
        help_text="ID of user to whom this token belongs",
        db_index=True,
        default=0,
    )


    access_token = models.TextField(help_text="The token itself", db_index=True)

    created_at = models.DateTimeField(help_text="Created timestamp", auto_now_add=True)

    expires_at = models.DateTimeField(
        help_text="Expires timestamp", default=datetime(2099, 12, 31, tzinfo=pytz.utc)
    )

    def expired(self):
        return self.expires_at < datetime.now(pytz.utc)

    @staticmethod
    def generate(num_bytes=32):
        token = Random.new().read(num_bytes)
        return base64.b32encode(token).decode("utf-8")
