# Generated by Django 4.2.1 on 2024-10-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0006_quiz_updated_at_alter_quiz_created_at_and_more'),
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
