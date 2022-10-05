# Generated by Django 4.0.3 on 2022-06-25 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_portal', '0002_alter_usersubscribers_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscribers',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='news_portal.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='usersubscribers',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Подписчик'),
        ),
    ]
