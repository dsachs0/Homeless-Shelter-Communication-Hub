from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def toggle_pin(self):
        self.pinned = not self.pinned
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, default="", on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return 'Comment by {}'.format(self.author)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.id})
