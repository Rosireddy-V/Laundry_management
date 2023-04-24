# Generated by Django 4.2 on 2023-04-24 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0002_clothes'),
    ]

    operations = [
        migrations.CreateModel(
            name='query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.TextField(max_length=200)),
                ('cloth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laundry.clothes')),
            ],
        ),
    ]