from pyexpat import model
from django.db import models

LANGUAGE_CHOICES = (
        ('pythno', 'Python'),
        ('java', 'Java'),
        ('rust', 'Rust'),
        ('c++', 'C++'),
)

class Project(models.Model):
    language = models.CharField(max_length=6, choices=LANGUAGE_CHOICES, default='')
    project_title = models.CharField(max_length=300)
    source = models.CharField(max_length=300)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.project_title
    