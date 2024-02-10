# Generated by Django 5.0.2 on 2024-02-10 19:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='Admin', max_length=30)),
                ('receiver', models.CharField(max_length=20, null=True)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(choices=[('Block A', 'Block A'), ('Block B', 'Block B'), ('Block C', 'Block C'), ('Block D', 'Block D'), ('Block E', 'Block E')], max_length=20, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hsc_roll', models.CharField(max_length=10, null=True, unique=True)),
                ('hsc_reg', models.CharField(max_length=16, null=True, unique=True)),
                ('reg_no', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('roll', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('session', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('dob', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('fathers_name', models.CharField(max_length=30, null=True)),
                ('mothers_name', models.CharField(max_length=30, null=True)),
                ('guardian_phone', models.CharField(max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('status', models.CharField(choices=[('Regular', 'Regular'), ('Ex-Student', 'Ex-Student')], default='Regular', max_length=40, null=True)),
                ('CGPA', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('result_description', models.CharField(blank=True, default='No Details Available now.', max_length=3000, null=True)),
                ('dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('reg_no', models.CharField(max_length=10, unique=True)),
                ('rank', models.CharField(choices=[('Lecturer', 'Lecturer'), ('Assistant Professor', 'Assistant Professor'), ('Professor', 'Professor'), ('Head of The Department', 'Head of The Department')], max_length=40, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('description', models.CharField(max_length=3000, null=True)),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.department')),
            ],
        ),
    ]
