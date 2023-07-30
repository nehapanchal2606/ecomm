# Generated by Django 4.1.4 on 2023-07-08 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_userprofile_contact_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_oreder', models.DateField()),
                ('complete', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('color', models.CharField(choices=[('w', 'White'), ('b', 'black'), ('p', 'pink'), ('bl', 'blue'), ('y', 'yellow'), ('r', 'red'), ('o', 'orange'), ('pu', 'purple'), ('br', 'brown'), ('g', 'gray'), ('gr', 'green')], default='w', max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('size', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.product')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.product')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.sub_category'),
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('timestamp', models.TimeField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField()),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.order_details')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.product')),
            ],
        ),
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry', models.TextField()),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(max_length=13)),
                ('total_amount', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=8)),
                ('date_added', models.DateField()),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.order_details')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.product')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
        ),
    ]