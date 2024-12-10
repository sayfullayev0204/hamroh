from django.db import models
from accounts.models import User

class Question(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tasks/')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    image_url = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='answer/')
    created_at = models.DateTimeField(auto_now=True)
    image_url = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:  # Only update status if this is a new answer
            self.question.status = True
            self.question.save()
        super().save(*args, **kwargs)


