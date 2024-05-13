from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# class App(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True)
#     message = models.CharField(max_length=5000)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Auth(models.Model):
#     login = models.CharField(max_length=10)
#     password = models.CharField(max_length=10)

# class Auth(models.Model):
#     login = models.CharField(max_length=10)
#     password = models.CharField(max_length=60)  # Increase the maximum length to accommodate the hashed password
#
#     def set_password(self, password):
#         self.password = password
#
#     def check_password(self, password):
#         return self.password == password

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class App(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField(default='')
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']