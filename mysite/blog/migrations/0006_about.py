# Generated by Django 3.0.6 on 2020-06-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('written_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
    ]