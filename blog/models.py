from django.db import models


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_image = models.URLField(max_length=300)
    article_text = models.TextField(default="")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.article_title

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
