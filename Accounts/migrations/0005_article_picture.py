# Generated by Django 2.2.10 on 2020-02-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_article_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.CharField(default='https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500', max_length=1000),
        ),
    ]
