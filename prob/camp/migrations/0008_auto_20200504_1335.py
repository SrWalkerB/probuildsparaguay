# Generated by Django 3.0.2 on 2020-05-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0007_auto_20200503_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campeao',
            name='bota',
        ),
        migrations.AddField(
            model_name='campeao',
            name='item6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item6', to='camp.Item'),
        ),
    ]
