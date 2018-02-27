from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=255, default="")
    image = models.URLField(default="")
    description = models.TextField(default="")
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

    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Comment')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content[:200]
