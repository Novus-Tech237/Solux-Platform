# Generated by Django 4.0 on 2023-11-19 22:21

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tutos', '0001_initial'),
        ('shop', '0007_rename_username_profile_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('progress', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tutos.course')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='PDF',
        ),
    ]
