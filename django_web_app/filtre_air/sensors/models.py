from django.db import models
import random
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    air_quality = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_fake_data():
        return SensorData.objects.create(
            temperature=round(random.uniform(18, 30), 2),
            humidity=round(random.uniform(30, 70), 2),
            air_quality=random.randint(1, 100)
        )


class ExempleModele(models.Model):
    """
    Exemple de modèle Django qui contient la plupart des types de champs
    et les attributs les plus utilisés.
    """

    # --- Champs numériques ---
    identifiant = models.BigAutoField(
        primary_key=True,
        help_text="Clé primaire auto-incrémentée"
    )
    entier_long = models.BigIntegerField(
        null=True,
        blank=True,
        db_index=True,
        help_text="Nombre entier de grande taille"
    )
    entier = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Entier compris entre 0 et 100"
    )
    petit_entier = models.SmallIntegerField(null=True, blank=True)
    entier_positif_long = models.PositiveBigIntegerField(null=True, blank=True)
    entier_positif = models.PositiveIntegerField(null=True, blank=True)
    petit_entier_positif = models.PositiveSmallIntegerField(null=True, blank=True)
    reel = models.FloatField(null=True, blank=True)
    decimal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text="Nombre décimal avec 2 chiffres après la virgule"
    )

    # --- Champs texte ---
    nom_unique = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nom unique",
        help_text="Texte court et unique",
        error_messages={"unique": "Ce nom existe déjà !"}
    )
    texte_long = models.TextField(null=True, blank=True)
    identifiant_url = models.SlugField(unique=True, help_text="Slug (identifiant lisible dans l’URL)")
    courriel = models.EmailField(blank=True, help_text="Adresse de courrier électronique")
    site_web = models.URLField(null=True, blank=True)
    identifiant_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # --- Champs fichiers et binaires ---
    # donnees_binaires = models.BinaryField(null=True, blank=True)
    # fichier = models.FileField(upload_to="uploads/fichiers/", null=True, blank=True)
    # image = models.ImageField(upload_to="uploads/images/", null=True, blank=True)
    # chemin_fichier = models.FilePathField(path="/tmp", null=True, blank=True)

    # --- Champs date et temps ---
    date_simple = models.DateField(
        null=True,
        blank=True,
        unique_for_date="date_simple",
        help_text="Date simple"
    )
    date_et_heure = models.DateTimeField(
        auto_now_add=True,
        help_text="Date et heure d’ajout (non modifiable)"
    )
    heure = models.TimeField(null=True, blank=True)
    duree = models.DurationField(null=True, blank=True)

    # --- Champs spéciaux ---
    est_actif = models.BooleanField(default=False, help_text="Valeur booléenne (vrai/faux)")
    donnees_json = models.JSONField(default=dict, help_text="Stockage de données JSON")
    adresse_ip = models.GenericIPAddressField(null=True, blank=True)
    valeur_calculee = models.GeneratedField(
        expression=models.F("entier") * 2,
        output_field=models.IntegerField(),
        db_persist=True,
        help_text="Champ généré automatiquement (entier * 2)"
    )

    

    # --- Exemple avec des choix ---
    choix = models.CharField(
        max_length=10,
        choices=[("A", "Option A"), ("B", "Option B")],
        default="A",
        help_text="Champ avec des choix prédéfinis"
    )