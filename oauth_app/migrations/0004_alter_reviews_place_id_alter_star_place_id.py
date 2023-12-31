# Generated by Django 4.2.5 on 2023-11-30 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_app', '0003_alter_restaurant_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='place_id',
            field=models.ForeignKey(db_column='place_id', default='default', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='oauth_app.restaurant', to_field='place_id'),
        ),
        migrations.AlterField(
            model_name='star',
            name='place_id',
            field=models.ForeignKey(db_column='place_id', default='default', on_delete=django.db.models.deletion.CASCADE, related_name='stars', to='oauth_app.restaurant', to_field='place_id'),
        ),
    ]
