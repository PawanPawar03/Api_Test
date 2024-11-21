# Generated by Django 5.1.3 on 2024-11-20 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=255)),
                ('user_lastname', models.CharField(max_length=255)),
                ('user_mail', models.EmailField(max_length=255)),
                ('user_phonenumber', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.AlterField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.user'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.user'),
        ),
    ]