# Generated by Django 4.1.5 on 2023-01-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_category_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='images/categories'),
        ),
    ]
