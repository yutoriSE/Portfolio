# Generated by Django 3.2.4 on 2021-06-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='description',
            options={'verbose_name_plural': 'スキルの概要文'},
        ),
        migrations.AddField(
            model_name='profile',
            name='mail',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]