from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.utils.html import escape


class Article(models.Model):

    title = models.CharField(max_length=255, default="")
    image = models.URLField(default="")
    description = models.TextField(default="")
    pub_date = models.DateTimeField('date published')
    count_comments = models.BigIntegerField('Count comments', default=0)


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

    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Comment')
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.content[:200]

    def as_dict(self):
        return {
            "id": self.id,
            "content": escape(self.content),
            "pub_date": self.pub_date.strftime('%B %d, %Y, %H:%M:%S'),  # DateTime format
            "user_id": self.user_id.username,
        }
