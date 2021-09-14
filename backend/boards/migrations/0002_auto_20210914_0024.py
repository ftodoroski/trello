# Generated by Django 3.2.7 on 2021-09-14 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='boards.list'),
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]