# Generated by Django 4.2.1 on 2023-09-28 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tm', models.CharField(choices=[('terra', 'Terra'), ('mare', 'Mare')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Uscita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('rientrato', models.BooleanField()),
                ('non_socio', models.BooleanField()),
                ('barca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barche.barca')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barche.proprietario')),
            ],
        ),
    ]
