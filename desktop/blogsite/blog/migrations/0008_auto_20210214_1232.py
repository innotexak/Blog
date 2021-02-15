# Generated by Django 3.0.6 on 2021-02-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210213_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the sender', max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_rec', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='post',
            new_name='comment',
        ),
    ]