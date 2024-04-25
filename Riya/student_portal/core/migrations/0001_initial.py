# Generated by Django 5.0.4 on 2024-04-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('math_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('science_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('english_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hindi_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('physics_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('chemistry_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('mathematics_marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]