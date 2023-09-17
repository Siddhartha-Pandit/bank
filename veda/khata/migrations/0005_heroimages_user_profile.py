# Generated by Django 4.1.5 on 2023-09-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khata', '0004_remove_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='heroImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(default='default_image.jpg', upload_to='media/images/')),
                ('image2', models.ImageField(default='default_image.jpg', upload_to='media/images/')),
                ('image3', models.ImageField(default='default_image.jpg', upload_to='media/images/')),
                ('image4', models.ImageField(default='default_image.jpg', upload_to='media/images/')),
                ('image5', models.ImageField(default='default_image.jpg', upload_to='media/images/')),
                ('image6', models.ImageField(default='default_image.jpg', upload_to='media/images/')),
                ('image7', models.ImageField(default='default_image.jpg', upload_to='media/images/')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(default='default_image.jpg', upload_to='media/images/'),
        ),
    ]