# Generated by Django 5.1 on 2024-10-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_newarrival'),
    ]

    operations = [
        migrations.CreateModel(
            name='newbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cover_image', models.ImageField(upload_to='book_covers')),
            ],
        ),
        migrations.DeleteModel(
            name='Newarrival',
        ),
    ]
