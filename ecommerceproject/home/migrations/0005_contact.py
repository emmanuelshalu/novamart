# Generated by Django 5.1.2 on 2024-11-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(choices=[('Sales', 'Sales'), ('Customer Support', 'Customer Support'), ('Technical Support', 'Technical Support')], max_length=20)),
                ('message', models.TextField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('is_resolved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date_submitted'],
            },
        ),
    ]
