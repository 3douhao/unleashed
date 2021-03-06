# Generated by Django 2.0.2 on 2018-03-13 06:06

from django.db import migrations, models

TAGS = (
    # ( tag name, tag slug ),
    ("augmented reality", "augmented-reality"),
    ("big data", "big-data"),
    ("django", "django"),
    ("education", "education"),
    ("ipython", "ipython"),
    ("javascript", "javascript"),
    ("jupyter", "jupyter"),
    ("mobile", "mobile"),
    ("nodejs", "node-js"),
    ("php", "php"),
    ("python", "python"),
    ("ruby on rails", "ruby-on-rails"),
    ("ruby", "ruby"),
    ("video games", "video-games"),
    ("web", "web"),
    ("zend", "zend"),
)


def add_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer', 'Tag')

    for tag_name, tag_slug in TAGS:
        Tag.objects.create(
            name=tag_name, slug=tag_slug
        )

def remove_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer', 'Tag')

    for _, tag_slug in TAGS:
        tag = Tag.objects.get(slug=tag_slug)
        tag.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_tag_data, remove_tag_data)
    ]
