# Generated by Django 5.1.1 on 2024-09-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_authority_alter_case_case_type_case_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='authority_photos/'),
        ),
    ]
