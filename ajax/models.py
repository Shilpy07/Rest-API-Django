from django.db import models


# Create your models here.
class Profile(models.Model):
    GENDER_CHOICE = (
        ("F", "Female"),
        ("M", "Male"),
    )
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=25, blank=False, null=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default="Female",blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name
