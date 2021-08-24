# Generated by Django 3.2.6 on 2021-08-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chains", "0020_block_explorer_templates"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chain",
            name="safe_apps_rpc_authentication",
            field=models.CharField(
                choices=[
                    ("API_KEY_PATH", "Api Key Path"),
                    ("NO_AUTHENTICATION", "No Authentication"),
                ],
                default="NO_AUTHENTICATION",
                max_length=255,
            ),
        ),
    ]