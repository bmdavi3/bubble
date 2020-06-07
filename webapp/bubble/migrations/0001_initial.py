# Generated by Django 3.0.7 on 2020-06-06 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'jug',
            },
        ),
        migrations.CreateModel(
            name='Bubble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('jug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bubble.Jug')),
            ],
            options={
                'db_table': 'bubble',
            },
        ),
    ]