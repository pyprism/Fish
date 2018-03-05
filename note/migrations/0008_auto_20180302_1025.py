# Generated by Django 2.0.2 on 2018-03-02 10:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0007_auto_20180227_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='encrypted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notebook',
            name='iv',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='notebook',
            name='salt',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='notes',
            name='note_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.NoteBook'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]