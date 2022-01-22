# Generated by Django 4.0 on 2022-01-16 23:24

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipCode', models.CharField(blank=True, max_length=100)),
                ('contacto', models.CharField(blank=True, max_length=100)),
                ('notes', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone', models.CharField(blank=True, max_length=250)),
                ('url_corp', models.CharField(blank=True, max_length=250)),
                ('feeds', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('grocery', 'Grocery'), ('protein', 'Protein'), ('fruVer', 'FruVer')], default='grocery', max_length=50)),
                ('presentation', models.CharField(choices=[('gram', 'Gram'), ('unit', 'Unit'), ('milliliter', 'Milliliter'), ('kilogram', 'Kilogram')], default='gram', max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=999)),
                ('price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('qty', models.DecimalField(decimal_places=10, max_digits=20)),
                ('merma', models.DecimalField(decimal_places=6, default=0.1, max_digits=10)),
                ('chef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipcode', models.CharField(blank=True, max_length=100)),
                ('contacto', models.CharField(blank=True, max_length=100)),
                ('notes', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('phone', models.CharField(blank=True, max_length=250)),
                ('url_corp', models.CharField(blank=True, max_length=250)),
                ('feeds', models.CharField(blank=True, max_length=250)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costos.company')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('isComplete', models.BooleanField(default=False)),
                ('cost', models.DecimalField(decimal_places=10, max_digits=20)),
                ('portions', models.DecimalField(decimal_places=10, default=1.0, max_digits=20)),
                ('mpcost', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('prepacost', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('portioncost', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('mpestablish', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('errormargin', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('realratemp', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('saleprice', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('menuprice', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('realsaleprice', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('taxportion', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.DecimalField(decimal_places=10, max_digits=20)),
                ('preparacion', models.CharField(max_length=250)),
                ('merma', models.DecimalField(decimal_places=6, max_digits=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costos.ingredient')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costos.receta')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipCode', models.CharField(blank=True, max_length=100)),
                ('contacto', models.CharField(blank=True, max_length=100)),
                ('notes', models.CharField(blank=True, max_length=250)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone', models.CharField(blank=True, max_length=250)),
                ('url_corp', models.CharField(blank=True, max_length=250)),
                ('feeds', models.CharField(blank=True, max_length=250)),
                ('chefs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costos.company')),
                ('providers', models.ManyToManyField(to='costos.Provider')),
            ],
        ),
        migrations.AddField(
            model_name='receta',
            name='items',
            field=models.ManyToManyField(through='costos.Steps', to='costos.Ingredient'),
        ),
        migrations.AddField(
            model_name='receta',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costos.restaurant'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='costos.provider'),
        ),
        migrations.CreateModel(
            name='HistoricalReceta',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('isComplete', models.BooleanField(default=False)),
                ('cost', models.DecimalField(decimal_places=10, max_digits=20)),
                ('portions', models.DecimalField(decimal_places=10, default=1.0, max_digits=20)),
                ('mpcost', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('prepacost', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('portioncost', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('mpestablish', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('errormargin', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('realratemp', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('saleprice', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('menuprice', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('realsaleprice', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('taxportion', models.DecimalField(blank=True, decimal_places=10, max_digits=20)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('chef', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.user')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='auth.user')),
                ('restaurant', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='costos.restaurant')),
            ],
            options={
                'verbose_name': 'historical receta',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIngredient',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('grocery', 'Grocery'), ('protein', 'Protein'), ('fruVer', 'FruVer')], default='grocery', max_length=50)),
                ('presentation', models.CharField(choices=[('gram', 'Gram'), ('unit', 'Unit'), ('milliliter', 'Milliliter'), ('kilogram', 'Kilogram')], default='gram', max_length=50)),
                ('created_on', models.DateTimeField(blank=True, editable=False)),
                ('description', models.TextField(max_length=999)),
                ('price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('qty', models.DecimalField(decimal_places=10, max_digits=20)),
                ('merma', models.DecimalField(decimal_places=6, default=0.1, max_digits=10)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('chef', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.user')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='auth.user')),
                ('provider', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='costos.provider')),
            ],
            options={
                'verbose_name': 'historical ingredient',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]