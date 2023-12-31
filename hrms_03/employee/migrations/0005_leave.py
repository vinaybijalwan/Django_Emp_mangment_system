# Generated by Django 4.1.5 on 2023-06-12 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0004_delete_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('CL', 'Casual Leave'), ('EL', 'Earned Leave'), ('LWP', 'Leave Without Pay'), ('SL', 'Sick Leave')], max_length=3)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('approved', models.BooleanField(default=False)),
                ('reason', models.CharField(max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
