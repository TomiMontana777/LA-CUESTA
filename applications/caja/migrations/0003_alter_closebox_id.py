# Generated by Django 5.1 on 2024-10-20 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closebox',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
