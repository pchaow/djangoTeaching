# Generated by Django 3.1 on 2020-08-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_activitytimeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='participant',
            field=models.ManyToManyField(blank=True, to='activity.Student'),
        ),
    ]
