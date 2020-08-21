# Generated by Django 2.2.2 on 2020-08-21 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartmenttype', models.CharField(max_length=20)),
                ('apertmentname', models.CharField(max_length=40)),
                ('bhktype', models.CharField(max_length=20)),
                ('floor', models.IntegerField()),
                ('totalfloor', models.IntegerField()),
                ('propertysize', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RentPropertyDetail',
            fields=[
                ('propertydetail_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='residential.PropertyDetail')),
                ('facing', models.CharField(blank=True, max_length=20)),
            ],
            bases=('residential.propertydetail',),
        ),
        migrations.CreateModel(
            name='RentLocationDetail',
            fields=[
                ('locationdetail_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='residential.LocationDetail')),
                ('street', models.CharField(max_length=150)),
                ('propertydetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.RentPropertyDetail')),
            ],
            bases=('residential.locationdetail',),
        ),
    ]
