# Generated by Django 3.2.9 on 2022-04-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20220427_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo1',
            field=models.ImageField(max_length=254, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo2',
            field=models.ImageField(max_length=254, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo3',
            field=models.ImageField(max_length=254, null=True, upload_to='photos'),
        ),
    ]
