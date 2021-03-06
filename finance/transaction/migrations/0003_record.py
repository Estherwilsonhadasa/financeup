# Generated by Django 2.0.5 on 2018-06-13 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0002_auto_20180613_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('account_name', models.CharField(max_length=200)),
                ('account_number', models.IntegerField()),
                ('depositors_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('comment', models.TextField(default='')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
