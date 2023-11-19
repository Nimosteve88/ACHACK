# Generated by Django 4.2.6 on 2023-11-19 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('btac_score', models.IntegerField()),
                ('eas_score', models.IntegerField()),
                ('fl_score', models.IntegerField()),
                ('hr_score', models.IntegerField()),
                ('kf_score', models.IntegerField()),
                ('mhawb_score', models.IntegerField()),
            ],
        ),
    ]