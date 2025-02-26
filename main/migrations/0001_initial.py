# Generated by Django 5.1.6 on 2025-02-26 09:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('yosh', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('kasb', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=255)),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('matn', models.TextField(blank=True, null=True)),
                ('mavzu', models.CharField(max_length=255)),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.muallif')),
            ],
        ),
    ]
