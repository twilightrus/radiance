# Generated by Django 2.0.2 on 2018-03-02 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20180302_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='article_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Article'),
        ),
    ]