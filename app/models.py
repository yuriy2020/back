from django.db import models


class CountryModel(models.Model):
    label = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.label


class UserModel(models.Model):
    GENDER_CHOICES = [
        ('М', 'Муж.'),
        ('Ж', 'Жен.'),
    ]
    family = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, )
    phone = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    traditional = models.BooleanField(default=False)
    dietician = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.family
