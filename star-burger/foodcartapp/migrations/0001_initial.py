# Generated by Django 3.2.15 on 2022-12-29 13:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', verbose_name='Телефон')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('status', models.CharField(choices=[('NP', 'Необработанный'), ('PR', 'Обработанный'), ('FN', 'Завершенный')], db_index=True, default='NP', max_length=20, verbose_name='Статус заказа')),
                ('comments', models.TextField(blank=True, verbose_name='Комментарии к заказу')),
                ('registered_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Зарегистрирован')),
                ('processed_at', models.DateTimeField(blank=True, null=True, verbose_name='Обработан')),
                ('delivered_at', models.DateTimeField(blank=True, null=True, verbose_name='Доставлен')),
                ('payment_type', models.CharField(blank=True, choices=[('El', 'Банковской картой'), ('Ca', 'Наличными')], max_length=20, verbose_name='Способ оплаты')),
            ],
            options={
                'verbose_name': ('Заказ',),
                'verbose_name_plural': 'Заказы',
                'ordering': ['status', 'registered_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='адрес')),
                ('contact_phone', models.CharField(blank=True, max_length=50, verbose_name='контактный телефон')),
            ],
            options={
                'verbose_name': 'ресторан',
                'verbose_name_plural': 'рестораны',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена')),
                ('image', models.ImageField(upload_to='', verbose_name='картинка')),
                ('special_status', models.BooleanField(db_index=True, default=False, verbose_name='спец.предложение')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='описание')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='foodcartapp.productcategory', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена позиции')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='foodcartapp.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='foodcartapp.product', verbose_name='Товар')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='chosen_restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='foodcartapp.restaurant', verbose_name='Ресторан, взявший заказ'),
        ),
        migrations.CreateModel(
            name='RestaurantMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.BooleanField(db_index=True, default=True, verbose_name='в продаже')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='foodcartapp.product', verbose_name='продукт')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='foodcartapp.restaurant', verbose_name='ресторан')),
            ],
            options={
                'verbose_name': 'пункт меню ресторана',
                'verbose_name_plural': 'пункты меню ресторана',
                'unique_together': {('restaurant', 'product')},
            },
        ),
    ]
