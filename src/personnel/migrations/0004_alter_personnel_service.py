# Generated by Django 4.2.3 on 2023-08-10 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0003_remove_personnel_responsable_service_responsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personnel.service'),
        ),
    ]
