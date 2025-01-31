# Generated by Django 4.2.1 on 2024-10-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0010_delete_pageview'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=255, unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
