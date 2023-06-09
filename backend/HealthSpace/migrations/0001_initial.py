# Generated by Django 4.1.5 on 2023-06-06 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbUser',
            fields=[
                ('username', models.CharField(max_length=24, primary_key=True, serialize=False, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='tbQRcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HealthSpace.tbuser')),
            ],
        ),
        migrations.CreateModel(
            name='tbPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=25)),
                ('sex', models.CharField(max_length=1)),
                ('bloodType', models.CharField(max_length=3)),
                ('maritalStatus', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=15)),
                ('nationality', models.CharField(max_length=25)),
                ('occupation', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=11)),
                ('primaryLanguague', models.CharField(max_length=25)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HealthSpace.tbuser')),
            ],
        ),
        migrations.CreateModel(
            name='tbMedicalConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicalCondition', models.CharField(max_length=50)),
                ('note', models.TextField(max_length=1000)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HealthSpace.tbuser')),
            ],
        ),
        migrations.CreateModel(
            name='tbEmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HealthSpace.tbuser')),
            ],
        ),
        migrations.CreateModel(
            name='tbAllergiesReactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergiesReactions', models.CharField(max_length=50)),
                ('notes', models.TextField(max_length=1000)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HealthSpace.tbuser')),
            ],
        ),
    ]
