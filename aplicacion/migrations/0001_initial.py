# Generated by Django 4.2.4 on 2023-08-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equiposProteccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('nivel_tension', models.CharField(max_length=50)),
                ('edificio', models.CharField(max_length=50)),
                ('gabinete', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('mask', models.CharField(max_length=50)),
                ('defGW', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='equiposRed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('nivel_tension', models.CharField(max_length=50)),
                ('edificio', models.CharField(max_length=50)),
                ('gabinete', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('mask', models.CharField(max_length=50)),
                ('defGW', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='equiposTelecontrol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('nivel_tension', models.CharField(max_length=50)),
                ('edificio', models.CharField(max_length=50)),
                ('gabinete', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('mask', models.CharField(max_length=50)),
                ('defGW', models.CharField(max_length=50)),
            ],
        ),
    ]
