from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])


class ExamQuestion(models.Model):
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question
    

class ExamAnswer(models.Model):
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer