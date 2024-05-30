# Generated by Django 4.2 on 2024-05-30 07:38

import bands.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('year', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ('band__name', 'year'),
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('still_active', models.BooleanField(blank=True, default=False)),
                ('genre', models.IntegerField(blank=True, choices=[(0, 'Neznamy'), (1, 'Classic'), (2, 'Dechovka'), (3, 'Pop'), (4, 'Rock'), (5, 'Heavy metal')], default=0)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model, bands.models.GetDataEngine),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bands.band'),
        ),
    ]
