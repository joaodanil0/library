# Generated by Django 4.1.7 on 2023-02-25 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_borrow_borrow_date_alter_borrow_borrow_return'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='borrow_time',
        ),
    ]
