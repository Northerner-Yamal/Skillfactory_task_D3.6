# Generated by Django 4.0.3 on 2022-04-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_category_options_alter_postcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default=0),
        ),
    ]
