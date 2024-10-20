# Generated by Django 4.2.16 on 2024-10-19 03:11

from django.db import migrations

from furc.models import UserRole


class Migration(migrations.Migration):

    def create_admin_role(apps, schema_editor):
        if not UserRole.objects.filter(role_id=1).exists():
            UserRole.objects.create(role_id=1, user_role='Admin')
    dependencies = [
        ('furc', '0025_alter_chemical_uom_alter_order_order_status'),
    ]

    operations = [
        migrations.RunPython(create_admin_role),
    ]
