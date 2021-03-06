# Generated by Django 3.2.9 on 2022-04-29 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20220429_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, default=' ', max_length=254, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo1',
            field=models.ImageField(blank=True, default=' ', max_length=254, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo2',
            field=models.ImageField(blank=True, default=' ', max_length=254, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo3',
            field=models.ImageField(blank=True, default=' ', max_length=254, upload_to='img'),
            preserve_default=False,
        ),
    ]
