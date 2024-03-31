# Generated by Django 5.0.3 on 2024-03-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_seocontent_prompt_twittercard_prompt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzedimage',
            name='alt_prompt',
            field=models.TextField(default='Analyze the contents of this image and generate 125 character that are search engine optimized for the alt attribute in the HTML img tag for this image. It is very important that your response is under 125 characters. Do your best to generate the most search engine optimized response and descriptive. Your response should be only the alt text to be used and nothing else: '),
        ),
        migrations.AddField(
            model_name='analyzedimage',
            name='json_ld_prompt',
            field=models.TextField(default="Attempt to identify the main object of this image. After identifying the main object of the image, try to define all attributes for it given its characteristic and generate a json-ld valid string following a schema.org schema. Your json-ld should contain all the fields you can fill out in chosen schema. The schema you choose should be the one that is most appropriate for the single main object you identified in the image. Your response should be solely valid json ld string  which should start with the opening curly braces character '{' and end with closing curly braces character '}'"),
        ),
    ]
