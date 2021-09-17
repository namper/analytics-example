# Generated by Django 3.1.2 on 2021-09-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.PositiveBigIntegerField(db_index=True, verbose_name='Post id')),
                ('user_id', models.PositiveBigIntegerField(db_index=True, verbose_name='User id')),
                ('likes_count', models.PositiveIntegerField(verbose_name='Likes count')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'get_latest_by': ('created',),
            },
        ),
    ]
