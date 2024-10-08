# Generated by Django 5.1.1 on 2024-09-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaunchedGovProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('IN_PROGRESS', 'In Progress'), ('STALLED', 'Stalled'), ('COMPLETED', 'Completed')], max_length=20)),
                ('location', models.CharField(max_length=200)),
                ('launched_by', models.CharField(max_length=200)),
                ('contractor', models.CharField(max_length=200)),
                ('amount_allocated', models.DecimalField(decimal_places=2, max_digits=15)),
                ('overview', models.TextField()),
                ('reporter_name', models.CharField(blank=True, max_length=200, null=True)),
                ('reporter_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('project_start_date', models.DateTimeField(auto_now_add=True)),
                ('project_end_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
