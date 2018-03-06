from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.utils.html import escape


class Article(models.Model):

    title = models.CharField(max_length=255, default='')
    image = models.URLField(default='')
    description = models.TextField(default='')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def get_next_id(self):
        """ Returns next id of Article """
        try:
            return self.get_next_by_pub_date().id
        except self.DoesNotExist:
            return False

    def get_previous_id(self):
        """ Returns previous id of Article """
        try:
            return self.get_previous_by_pub_date().id
        except self.DoesNotExist:
            return False


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Comment')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.content[:200]

    def as_dict(self, request):
        return {
            'id': self.id,
            'content': escape(self.content),
            'pub_date': self.pub_date.strftime('%B %d, %Y, %H:%M:%S'),  # DateTime format
            'username': self.user.username,
            'count_likes': self.like_set.count(),
            'is_liked': self.like_set.filter(user=request.user).count(),
            'user_id': self.user.id
        }


class Like(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
