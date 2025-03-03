<<<<<<< HEAD
# Generated by Django 5.1 on 2024-08-21 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_book_cover_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(through='app1.CartItem', to='app1.book'),
        ),
    ]
=======
# Generated by Django 5.1 on 2024-08-21 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_book_cover_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(through='app1.CartItem', to='app1.book'),
        ),
    ]
>>>>>>> 2c9025f (Initial commit with requirements.txt)
