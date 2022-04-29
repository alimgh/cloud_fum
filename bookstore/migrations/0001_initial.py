# Generated by Django 4.0.4 on 2022-04-29 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('publisher', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('token', models.CharField(max_length=500)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review_text', models.CharField(max_length=500)),
                ('is_positive', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.books')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.users')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_id', to='bookstore.users')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_id', to='bookstore.users')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.states')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='genre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.genres'),
        ),
    ]
