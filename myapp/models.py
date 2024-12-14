from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Question(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.text
