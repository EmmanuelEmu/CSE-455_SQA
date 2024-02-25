# Generated by Django 5.0.1 on 2024-02-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Ex-Student', 'Ex-Student')], default='Regular', max_length=40, null=True),
        ),
    ]