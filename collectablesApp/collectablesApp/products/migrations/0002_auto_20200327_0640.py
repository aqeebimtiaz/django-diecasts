# Generated by Django 2.2.10 on 2020-03-27 06:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('barcode', models.CharField(max_length=100, unique=True)),
                ('manufacturer', models.CharField(max_length=200, unique=True)),
                ('style', models.CharField(max_length=200, unique=True)),
                ('year', models.PositiveIntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1984), products.models.max_value_current_year])),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]