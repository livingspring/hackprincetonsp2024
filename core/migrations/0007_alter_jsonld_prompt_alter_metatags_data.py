# Generated by Django 5.0.3 on 2024-03-31 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_metatags_prompt_alter_jsonld_prompt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsonld',
            name='prompt',
            field=models.TextField(default="Generate a JSON-LD using a schema from schema.org that is most appropriate for the JSON data provided below. Your response should only be the JSON-LD as a string and nothing else, which should start with the opening curly braces character '{' and end with closing curly braces character '}'."),
        ),
        migrations.AlterField(
            model_name='metatags',
            name='data',
            field=models.JSONField(null=True),
        ),
    ]
