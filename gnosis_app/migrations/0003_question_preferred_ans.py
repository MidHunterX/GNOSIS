# Generated by Django 5.0.3 on 2024-04-28 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnosis_app', '0002_comment_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='preferred_ans',
            field=models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('video', 'Audio'), ('audio', 'Video')], default='text', max_length=100),
        ),
    ]
