# Generated by Django 3.2.12 on 2022-02-26 18:09

from django.db import migrations, models
import django.db.models.deletion
import moduleAdministrative.models.bienImmobilier
import moduleAdministrative.models.immeuble


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
                ('nomBien', models.CharField(max_length=100)),
                ('statut', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=moduleAdministrative.models.bienImmobilier.upload_path)),
                ('adresse', models.CharField(max_length=200)),
                ('etat', models.CharField(choices=[('neuf', 'neuf'), ('tresBonEtat', 'tresBonEtat'), ('bonEtat', 'bonEtat'), ('mauvaisEtat', 'mauvaisEtat')], default='neuf', max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
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
                ('nbrPiece', models.IntegerField()),
                ('typePiece', models.CharField(max_length=250)),
                ('jardin', models.BooleanField(default=False)),
            ],
            bases=('moduleAdministrative.bienimmobilier',),
        ),
        migrations.CreateModel(
            name='Immeuble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True)),
                ('nomImmeuble', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=moduleAdministrative.models.immeuble.upload_path)),
                ('adresse', models.CharField(max_length=200)),
                ('etat', models.CharField(choices=[('neuf', 'neuf'), ('tresBonEtat', 'tresBonEtat'), ('bonEtat', 'bonEtat'), ('mauvaisEtat', 'mauvaisEtat')], default='neuf', max_length=15)),
                ('categorie', models.CharField(choices=[('R0', 'R0'), ('R1', 'R1'), ('R2', 'R2'), ('R3', 'R3'), ('R4', 'R4'), ('R5', 'R5'), ('R6', 'R6'), ('R7', 'R7'), ('R8', 'R8'), ('R9', 'R9'), ('R10', 'R10')], default='R0', max_length=3)),
                ('proprietaire', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='moduleAdministrative.proprietaire')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='moduleAdministrative.zone')),
            ],
        ),
        migrations.AddField(
            model_name='bienimmobilier',
            name='proprietaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='moduleAdministrative.proprietaire'),
        ),
        migrations.AddField(
            model_name='bienimmobilier',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='moduleAdministrative.zone'),
        ),
        migrations.CreateModel(
            name='Appartement',
            fields=[
                ('bienimmobilier_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='moduleAdministrative.bienimmobilier')),
                ('typeAppartement', models.CharField(choices=[('studio', 'studio'), ('F2', 'F2'), ('F3', 'F3'), ('F4', 'F4'), ('F5', 'F5'), ('F6', 'F6'), ('F7', 'F7'), ('F8', 'F8'), ('F9', 'F9'), ('F10', 'F10')], max_length=6)),
                ('niveau', models.CharField(choices=[('etage_0_gauche', 'etage_0_gauche'), ('etage_0_droit', 'etage_0_droit'), ('etage_1_gauche', 'etage_1_gauche'), ('etage_1_droit', 'etage_1_droit'), ('etage_2_gauche', 'etage_2_gauche'), ('etage_2_droit', 'etage_2_droit'), ('etage_3_gauche', 'etage_3_gauche'), ('etage_3_droit', 'etage_3_droit'), ('etage_4_gauche', 'etage_4_gauche'), ('etage_4_droit', 'etage_4_droit'), ('etage_5_gauche', 'etage_5_gauche'), ('etage_5_droit', 'etage_5_droit'), ('etage_6_gauche', 'etage_6_gauche'), ('etage_6_droit', 'etage_6_droit'), ('etage_7_gauche', 'etage_7_gauche'), ('etage_7_droit', 'etage_7_droit'), ('etage_8_gauche', 'etage_8_gauche'), ('etage_8_droit', 'etage_8_droit'), ('etage_9_gauche', 'etage_9_gauche'), ('etage_9_droit', 'etage_9_droit'), ('etage_10_gauche', 'etage_10_gauche'), ('etage_10_droit', 'etage_10_droit')], max_length=20)),
                ('immeuble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduleAdministrative.immeuble')),
            ],
            bases=('moduleAdministrative.bienimmobilier',),
        ),
    ]
