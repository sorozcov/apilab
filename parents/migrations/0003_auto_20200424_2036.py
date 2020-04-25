# Generated by Django 3.0.4 on 2020-04-25 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parents', '0002_parent_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='id',
        ),
        migrations.AlterField(
            model_name='parent',
            name='user',
            field=models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]