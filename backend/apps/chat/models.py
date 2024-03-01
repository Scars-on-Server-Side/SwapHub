from django.db import models
from django.contrib.auth.models import User


class Dialog(models.Model):

    user_A = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dialog_user_A"
    )
    user_B = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dialog_user_B"
    )
    start_on = models.DateTimeField(auto_now_add=True)


class Message(models.Model):

    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
