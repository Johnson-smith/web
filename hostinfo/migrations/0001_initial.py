# Generated by Django 2.1.1 on 2018-10-15 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50, verbose_name='环境')),
                ('hostname', models.CharField(max_length=50, verbose_name='机器名')),
                ('publicip', models.CharField(default='-', max_length=50, verbose_name='入口公网ip')),
                ('publicip1', models.CharField(default='-', max_length=50, verbose_name='对外公网ip')),
                ('privateip', models.GenericIPAddressField(blank=True, null=True, verbose_name='私网ip')),
                ('cpu_num', models.CharField(default='-', max_length=50)),
                ('gateway', models.CharField(blank=True, max_length=50)),
                ('mac', models.CharField(blank=True, max_length=50)),
                ('distribution', models.CharField(blank=True, max_length=50)),
                ('distribution_version', models.CharField(blank=True, max_length=50)),
                ('architecture', models.CharField(blank=True, max_length=50)),
                ('kernel', models.CharField(blank=True, max_length=50)),
                ('processor', models.CharField(blank=True, max_length=50)),
                ('processor_count', models.CharField(blank=True, max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('app_name', models.CharField(max_length=100, verbose_name='应用名')),
                ('account', models.CharField(default='-', max_length=50, verbose_name='云账号')),
            ],
            options={
                'verbose_name': '机器',
                'verbose_name_plural': '机器',
            },
        ),
    ]
