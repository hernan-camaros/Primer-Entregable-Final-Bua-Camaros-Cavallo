# Generated by Django 4.0.5 on 2022-06-28 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoFinalApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claseavanzada',
            old_name='apellido3',
            new_name='apellido3_clase',
        ),
        migrations.RenameField(
            model_name='claseavanzada',
            old_name='celular3',
            new_name='celular3_clase',
        ),
        migrations.RenameField(
            model_name='claseavanzada',
            old_name='email3',
            new_name='email3_clase',
        ),
        migrations.RenameField(
            model_name='claseavanzada',
            old_name='nombre3',
            new_name='nombre3_clase',
        ),
        migrations.RenameField(
            model_name='claseinicial',
            old_name='apellido1',
            new_name='apellido1_clase',
        ),
        migrations.RenameField(
            model_name='claseinicial',
            old_name='celular1',
            new_name='celular1_clase',
        ),
        migrations.RenameField(
            model_name='claseinicial',
            old_name='email1',
            new_name='email1_clase',
        ),
        migrations.RenameField(
            model_name='claseinicial',
            old_name='nombre1',
            new_name='nombre1_clase',
        ),
        migrations.RenameField(
            model_name='claseintermedia',
            old_name='apellido2',
            new_name='apellido2_clase',
        ),
        migrations.RenameField(
            model_name='claseintermedia',
            old_name='celular2',
            new_name='celular2_clase',
        ),
        migrations.RenameField(
            model_name='claseintermedia',
            old_name='email2',
            new_name='email2_clase',
        ),
        migrations.RenameField(
            model_name='claseintermedia',
            old_name='nombre2',
            new_name='nombre2_clase',
        ),
    ]
