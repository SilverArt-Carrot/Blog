# Generated by Django 3.0.3 on 2020-04-04 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visits',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='访问量'),
        ),
    ]
