# Generated by Django 4.0.4 on 2022-04-29 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='genre_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore.genres'),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='publisher',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_id', to='bookstore.users'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='seller_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_id', to='bookstore.users'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore.states'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='book_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore.books'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='is_positive',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore.users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='type',
            field=models.IntegerField(null=True),
        ),
    ]
