# Generated by Django 4.0.4 on 2022-06-17 18:27

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tipo_user', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='userimg/')),
                ('numero_contac', models.IntegerField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Perona/Pyme',
                'verbose_name_plural': 'Peronas/Pymes',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Municipalidad',
            fields=[
                ('id_munic', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Municipalidad',
                'verbose_name_plural': 'Municipalidades',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('nr_visita', models.IntegerField(blank=True, default='0', null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Oferta_empleo',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.post')),
                ('id_oferta', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre_ofer', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('pago', models.IntegerField()),
                ('extra', models.FileField(upload_to='Archivos_ofertas_Emp/')),
            ],
            bases=('core.post',),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.post')),
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('descripcion', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('tipo_producto', models.CharField(max_length=20)),
            ],
            bases=('core.post',),
        ),
        migrations.CreateModel(
            name='tienda_fisica',
            fields=[
                ('id_tienda', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='')),
                ('direccion', models.CharField(max_length=40)),
                ('numero_contac', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReporteStrike',
            fields=[
                ('id_strike', models.AutoField(primary_key=True, serialize=False)),
                ('num_strike', models.IntegerField()),
                ('anotacion', models.CharField(max_length=100)),
                ('id_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
                ('id_user_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='usuarioTrabaj',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cargo', models.CharField(max_length=20)),
                ('tienda_fisica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tienda_trabaj', to='core.tienda_fisica')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
            bases=('core.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='usuarioEncarga',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cargo', models.CharField(max_length=20)),
                ('Municipalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.municipalidad')),
            ],
            options={
                'verbose_name': 'Encargado',
                'verbose_name_plural': 'Encargados',
            },
            bases=('core.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudOferta',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('extra', models.FileField(upload_to='Archivos_Postulaciones/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.oferta_empleo')),
            ],
        ),
    ]
