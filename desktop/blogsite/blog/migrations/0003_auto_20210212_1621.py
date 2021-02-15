# Generated by Django 3.0.6 on 2021-02-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_create_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='quote',
        ),
        migrations.AlterField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(upload_to='static'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
