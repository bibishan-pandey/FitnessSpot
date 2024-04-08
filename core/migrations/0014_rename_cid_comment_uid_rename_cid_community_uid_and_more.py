# Generated by Django 5.0.3 on 2024-04-08 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_alter_communitypost_active_alter_post_active"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="cid",
            new_name="uid",
        ),
        migrations.RenameField(
            model_name="community",
            old_name="cid",
            new_name="uid",
        ),
        migrations.RenameField(
            model_name="communitypost",
            old_name="cid",
            new_name="uid",
        ),
        migrations.RenameField(
            model_name="friend",
            old_name="fid",
            new_name="uid",
        ),
        migrations.RenameField(
            model_name="friendrequest",
            old_name="fid",
            new_name="uid",
        ),
        migrations.RenameField(
            model_name="notification",
            old_name="nid",
            new_name="uid",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="pid",
            new_name="uid",
        ),
        migrations.RenameField(
            model_name="replycomment",
            old_name="rcid",
            new_name="uid",
        ),
        migrations.RenameField(
            model_name="workout",
            old_name="pid",
            new_name="uid",
        ),
    ]
