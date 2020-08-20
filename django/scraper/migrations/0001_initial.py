# Generated by Django 3.1 on 2020-08-20 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('company', models.CharField(max_length=300)),
                ('posted_date', models.DateField()),
                ('work_type', models.CharField(max_length=300)),
                ('location', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Job_to_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.job')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.tag')),
            ],
        ),
    ]
