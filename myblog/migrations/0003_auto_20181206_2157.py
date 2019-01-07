# Generated by Django 2.1.3 on 2018-12-07 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='blogPosts', to='myblog.Category'),
        ),
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='myblog.Post'),
            preserve_default=False,
        ),
    ]