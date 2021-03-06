# Generated by Django 2.2.12 on 2020-04-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0013_auto_20200423_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pdf', models.FileField(upload_to='college/syllabus')),
            ],
        ),
        migrations.AlterField(
            model_name='fyform',
            name='year',
            field=models.CharField(default='FY', max_length=20),
        ),
        migrations.AlterField(
            model_name='syform',
            name='hsc_result',
            field=models.ImageField(upload_to='college/form/result'),
        ),
        migrations.AlterField(
            model_name='syform',
            name='sem1_result',
            field=models.ImageField(upload_to='college/form/result'),
        ),
        migrations.AlterField(
            model_name='syform',
            name='sem2_result',
            field=models.ImageField(upload_to='college/form/result'),
        ),
        migrations.AlterField(
            model_name='syform',
            name='ssc_result',
            field=models.ImageField(upload_to='college/form/result'),
        ),
        migrations.AlterField(
            model_name='syform',
            name='year',
            field=models.CharField(default='SY', max_length=20),
        ),
        migrations.AlterField(
            model_name='tyform',
            name='year',
            field=models.CharField(default='TY', max_length=20),
        ),
    ]
