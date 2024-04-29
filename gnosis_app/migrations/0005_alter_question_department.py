# Generated by Django 5.0.3 on 2024-04-29 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnosis_app', '0004_alter_question_preferred_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='department',
            field=models.CharField(choices=[('gen', 'General'), ('cse', 'Computer Science and Engineering'), ('me', 'Mechanical Engineering'), ('ce', 'Civil Engineering'), ('eee', 'Electrical and Electronics Engineering'), ('ece', 'Electronics and Communication Engineering')], default='gen', max_length=100),
        ),
    ]
