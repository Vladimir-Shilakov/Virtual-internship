# Generated by Django 4.2.6 on 2023-10-19 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
            options={
                'verbose_name': 'Координаты',
                'verbose_name_plural': 'Координаты',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б'), ('6a', '6А'), ('6b', '6Б')], max_length=2, null=True, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б'), ('6a', '6А'), ('6b', '6Б')], max_length=2, null=True, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б'), ('6a', '6А'), ('6b', '6Б')], max_length=2, null=True, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б'), ('6a', '6А'), ('6b', '6Б')], max_length=2, null=True, verbose_name='Весна')),
            ],
            options={
                'verbose_name': 'Уровень сложности перевала',
                'verbose_name_plural': 'Уровни сложности перевала',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('otc', models.CharField(max_length=255)),
                ('fam', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beautyTitle', models.CharField(max_length=255, verbose_name='Титульное название')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('other_titles', models.CharField(max_length=255, verbose_name='Альтернативное название')),
                ('connect', models.TextField(verbose_name='Соединяет')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('coords', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.user')),
            ],
            options={
                'verbose_name': 'Перевал',
                'verbose_name_plural': 'Перевалы',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('mountain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.mountain')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]