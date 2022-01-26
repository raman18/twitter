# Generated by Django 3.1.12 on 2022-01-26 18:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.TextField(db_index=True, help_text='The token itself')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created timestamp')),
                ('expires_at', models.DateTimeField(default=datetime.datetime(2099, 12, 31, 0, 0, tzinfo=utc), help_text='Expires timestamp')),
                ('user', models.ForeignKey(db_column='user_id', default=0, help_text='ID of user to whom this token belongs', on_delete=django.db.models.deletion.CASCADE, to='userauth.user')),
            ],
            options={
                'db_table': 'access_tokens',
            },
        ),
    ]