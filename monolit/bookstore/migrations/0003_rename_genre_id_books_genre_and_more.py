# Generated by Django 4.0.4 on 2022-04-29 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_alter_books_genre_id_alter_books_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='seller_id',
            new_name='seller',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='state_id',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='user_id',
            new_name='user',
        ),
    ]
