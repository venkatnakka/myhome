# Generated by Django 3.1 on 2020-08-22 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saleDeedCertificate', models.BooleanField(default=True)),
                ('propertytax', models.BooleanField(default=True)),
                ('occupancyCertificate', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='flatDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartmenttype', models.CharField(max_length=20)),
                ('apertmentname', models.CharField(max_length=40)),
                ('bhktype', models.CharField(max_length=20)),
                ('floor', models.IntegerField()),
                ('totalfloor', models.IntegerField()),
                ('propertyage', models.CharField(max_length=50)),
                ('facing', models.CharField(blank=True, max_length=20)),
                ('propertysize', models.IntegerField()),
                ('tenant_type', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=20)),
                ('flatrentexpected', models.IntegerField()),
                ('flatrentDeposit', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hosteldetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabiltyfor', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Anyone', 'ANYONE')], max_length=20)),
                ('preferedguests', models.CharField(max_length=30)),
                ('Availablefrom', models.DateTimeField()),
                ('foodincluded', models.BooleanField()),
                ('image', models.ImageField(upload_to='')),
                ('parking', models.CharField(choices=[('TWO WHEELER', 'Two wheeler'), ('FOUR WHEELER', 'Four wheeler')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HostelRoomDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomsavailable', models.CharField(choices=[('SINGLE', 'Single'), ('DOUBLE', 'Double'), ('THREE', 'Three'), ('FOUR', 'Four')], max_length=20)),
                ('rentexpected', models.IntegerField()),
                ('rentDeposit', models.IntegerField()),
                ('cupboards', models.BooleanField(default=False)),
                ('Tv', models.BooleanField(default=False)),
                ('bedding', models.BooleanField(default=False)),
                ('geyser', models.BooleanField(default=False)),
                ('Ac', models.BooleanField(default=False)),
                ('attachedbathroom', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RentalDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availablelease', models.BooleanField(default=True)),
                ('expectedrent', models.IntegerField()),
                ('expecteddeposit', models.IntegerField()),
                ('maintenance', models.CharField(max_length=30)),
                ('availablefrom', models.DateTimeField()),
                ('preferedtenants', models.CharField(max_length=50)),
                ('furnishing', models.CharField(max_length=20)),
                ('parking', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RentPropertyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartmenttype', models.CharField(max_length=20)),
                ('apertmentname', models.CharField(max_length=40)),
                ('bhktype', models.CharField(max_length=20)),
                ('floor', models.IntegerField()),
                ('totalfloor', models.IntegerField()),
                ('propertysize', models.IntegerField()),
                ('facing', models.CharField(blank=True, max_length=20)),
                ('datecreated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resaledetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expectedprice', models.CharField(max_length=20)),
                ('maintenancecost', models.CharField(max_length=20)),
                ('possessiondate', models.DateTimeField()),
                ('kitchen_type', models.CharField(max_length=50)),
                ('furnishing', models.CharField(max_length=20)),
                ('parking', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ResalePropertyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartmenttype', models.CharField(max_length=20)),
                ('apertmentname', models.CharField(max_length=40)),
                ('bhktype', models.CharField(max_length=20)),
                ('floor', models.IntegerField()),
                ('totalfloor', models.IntegerField()),
                ('propertysize', models.IntegerField()),
                ('ownershiptype', models.CharField(max_length=20)),
                ('propertyage', models.CharField(max_length=50)),
                ('floortype', models.CharField(max_length=30)),
                ('no_of_units', models.IntegerField()),
                ('facing', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResaleSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilty', models.CharField(max_length=30)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('availabiltyAllDay', models.BooleanField(default=False)),
                ('resaledetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.resaledetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResaleLocationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, null=True)),
                ('locality', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('Resalepropertydetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.resalepropertydetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResaleAmenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilty', models.CharField(max_length=30)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('availabiltyAllDay', models.BooleanField(default=False)),
                ('resaledetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.resaledetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RentSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilty', models.CharField(max_length=30)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('availabiltyAllDay', models.BooleanField(default=False)),
                ('Rentdetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.rentaldetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RentLocationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, null=True)),
                ('locality', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('propertydetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='residential.rentpropertydetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RentAmenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathroom', models.IntegerField()),
                ('balcony', models.IntegerField()),
                ('watersupply', models.CharField(max_length=20)),
                ('gym', models.BooleanField(default=False)),
                ('nonvegallowed', models.BooleanField(default=True)),
                ('showinghouse', models.CharField(max_length=20)),
                ('secondarynumber', models.IntegerField()),
                ('amenitiesavailable', models.CharField(max_length=400)),
                ('rentdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.rentaldetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='rentaldetail',
            name='rentallocation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='residential.rentlocationdetail'),
        ),
        migrations.CreateModel(
            name='hostelSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availabilty', models.CharField(max_length=30)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('availabiltyAllDay', models.BooleanField(default=False)),
                ('hostelschedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.hosteldetails')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hostellocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, null=True)),
                ('locality', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('roomavailibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.hostelroomdetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='hosteldetails',
            name='hostellocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.hostellocation'),
        ),
    ]
