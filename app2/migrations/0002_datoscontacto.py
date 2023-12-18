# Generated by Django 4.2.7 on 2023-11-24 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='datosContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCelular', models.CharField(blank=True, max_length=32, null=True)),
                ('emailEstudiante', models.CharField(blank=True, max_length=32, null=True)),
                ('estudianteRelacionado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app2.estudianteinfo')),
            ],
        ),
    ]
