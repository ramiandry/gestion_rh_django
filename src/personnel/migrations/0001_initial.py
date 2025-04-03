# Generated by Django 4.2.3 on 2023-07-15 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fonction', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=150)),
                ('cin', models.CharField(max_length=150)),
                ('fonction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personnel.fonction')),
                ('responsable', models.ManyToManyField(related_name='responsable', to='personnel.service')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personnel.service')),
                ('utilisateur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilisateur.utilisateur')),
            ],
        ),
    ]
