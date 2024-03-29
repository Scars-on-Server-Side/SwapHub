# Generated by Django 4.2.7 on 2024-03-16 01:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='thing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.thing'),
        ),
        migrations.AddField(
            model_name='thing',
            name='avatar',
            field=models.CharField(default='', max_length=300),
        ),
    ]
