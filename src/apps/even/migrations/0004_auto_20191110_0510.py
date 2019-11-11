# Generated by Django 2.2.6 on 2019-11-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('even', '0003_auto_20191110_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='co_promoters',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='co_promoters', to='even.EventPromoter'),
        ),
        migrations.AlterField(
            model_name='event',
            name='subcategories',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='subcategories', to='even.EventCategory'),
        ),
    ]
