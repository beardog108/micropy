# Generated by Django 2.2 on 2019-06-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_rules', models.TextField(null=True)),
                ('site_terms', models.TextField(null=True)),
                ('site_privacy', models.TextField(null=True)),
                ('site_motd', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='boards',
            name='rules',
            field=models.TextField(default='Obey site-wide rules'),
        ),
    ]
