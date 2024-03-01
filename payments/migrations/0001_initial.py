# Generated by Django 4.2.10 on 2024-03-01 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('Credit Card', 'Credit Card'), ('Wire Transfer/EFT', 'Wire Transfer/EFT'), ('Cash on Delivery', 'Cash on Delivery')], max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('process_ID', models.CharField(blank=True, max_length=255)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
