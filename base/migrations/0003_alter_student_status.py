# Generated by Django 5.0.1 on 2024-01-31 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Ex-Student', 'Ex-Student')], default='Pending', max_length=40, null=True),
        ),
    ]
