# Generated by Django 3.2.12 on 2022-02-21 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BienImmobilier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True)),
                ('adresse', models.CharField(max_length=200, null=True)),
                ('etat', models.CharField(choices=[('neuf', 'neuf'), ('tresBonEtat', 'tresBonEtat'), ('bonEtat', 'bonEtat'), ('mauvaisEtat', 'mauvaisEtat')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=20, unique=True)),
                ('telephon', models.CharField(default=None, max_length=18)),
                ('email', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomZone', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('bienimmobilier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='moduleAdministrative.bienimmobilier')),
                ('nbrPiece', models.IntegerField(null=True)),
                ('typePiece', models.CharField(max_length=200)),
                ('jardin', models.BooleanField(default=False)),
            ],
            bases=('moduleAdministrative.bienimmobilier',),
        ),
        migrations.CreateModel(
            name='Immeuble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True)),
                ('nomImmeuble', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('photo', models.CharField(max_length=250)),
                ('adresse', models.CharField(max_length=200)),
                ('etat', models.CharField(choices=[('neuf', 'neuf'), ('tresBonEtat', 'tresBonEtat'), ('bonEtat', 'bonEtat'), ('mauvaisEtat', 'mauvaisEtat')], default='R0', max_length=15)),
                ('categorie', models.CharField(choices=[('R0', 'R0'), ('R1', 'R1'), ('R2', 'R2'), ('R3', 'R3'), ('R4', 'R4'), ('R5', 'R5'), ('R6', 'R6'), ('R7', 'R7'), ('R8', 'R8'), ('R9', 'R9'), ('R10', 'R10')], default='R0', max_length=3)),
                ('proprietaire', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='moduleAdministrative.proprietaire')),
                ('zone', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='moduleAdministrative.zone')),
            ],
        ),
        migrations.AddField(
            model_name='bienimmobilier',
            name='proprietaire',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='moduleAdministrative.proprietaire'),
        ),
        migrations.AddField(
            model_name='bienimmobilier',
            name='zone',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='moduleAdministrative.zone'),
        ),
        migrations.CreateModel(
            name='Appartement',
            fields=[
                ('bienimmobilier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='moduleAdministrative.bienimmobilier')),
                ('typeAppartement', models.CharField(choices=[('studio', 'studio'), ('F2', 'F2'), ('F3', 'F3'), ('F4', 'F4'), ('F5', 'F5'), ('F6', 'F6'), ('F7', 'F7'), ('F8', 'F8'), ('F9', 'F9'), ('F10', 'F10')], max_length=6)),
                ('niveau', models.CharField(choices=[('etage_0', 'etage_0'), ('etage_1', 'etage_1'), ('etage_2', 'etage_2'), ('etage_3', 'etage_3'), ('etage_4', 'etage_4'), ('etage_5', 'etage_5'), ('etage_6', 'etage_6'), ('etage_7', 'etage_7'), ('etage_8', 'etage_8'), ('etage_9', 'etage_9'), ('etage_10', 'etage_10')], max_length=10)),
                ('immeuble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduleAdministrative.immeuble')),
            ],
            bases=('moduleAdministrative.bienimmobilier',),
        ),
    ]
