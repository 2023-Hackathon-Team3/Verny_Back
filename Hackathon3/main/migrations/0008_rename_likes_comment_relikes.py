# Generated by Django 4.2 on 2023-08-06 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment_likes_recomment_likes_delete_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='likes',
            new_name='relikes',
        ),
    ]
