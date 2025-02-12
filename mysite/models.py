# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    publication_date = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)
    post = models.ForeignKey('MainPost', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_comment'


class MainKategorija(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'main_kategorija'


class MainPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    pavadinimas = models.CharField(max_length=255)
    turinys = models.TextField()
    publication_date = models.DateTimeField()
    foto = models.CharField(max_length=100)
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_post'


class MainPostKategorija(models.Model):
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(MainPost, models.DO_NOTHING)
    kategorija = models.ForeignKey(MainKategorija, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_post_kategorija'
        unique_together = (('post', 'kategorija'),)


class MainPostTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    post = models.ForeignKey(MainPost, models.DO_NOTHING)
    tag = models.ForeignKey('MainTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'main_post_tags'
        unique_together = (('post', 'tag'),)


class MainProduktai(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    url_to_product = models.CharField(max_length=255)
    category_path = models.CharField(max_length=255)
    url_to_image = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    sales = models.IntegerField()
    review_rate = models.FloatField()
    estimated_commission_rate = models.FloatField()
    estimated_earnings = models.DecimalField(max_digits=10, decimal_places=2)
    

    class Meta:
        managed = False
        db_table = 'main_produktai'


class MainTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'main_tag'


class Produktai(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    url_to_product = models.TextField(db_column='URL to product', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    categorypath = models.TextField(db_column='categoryPath', blank=True, null=True)  # Field name made lowercase.
    url_to_image = models.TextField(db_column='URL to image', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency = models.TextField(db_column='Currency', blank=True, null=True)  # Field name made lowercase.
    sales = models.FloatField(db_column='Sales', blank=True, null=True)  # Field name made lowercase.
    review_rate = models.FloatField(db_column='Review Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    estimated_commission_rate = models.TextField(db_column='Estimated Commission Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    estimated_earnings = models.FloatField(db_column='Estimated Earnings', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'produktai'


class ProduktaiLt(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    salis = models.TextField(blank=True, null=True)
    pavadinimas = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    kategirija = models.TextField(blank=True, null=True)
    foto = models.TextField(blank=True, null=True)
    valiuta = models.TextField(db_column='Valiuta', blank=True, null=True)  # Field name made lowercase.
    pardavimai = models.TextField(db_column='Pardavimai', blank=True, null=True)  # Field name made lowercase.
    vertinimas = models.TextField(blank=True, null=True)
    numatomas_komisinis_dydis = models.TextField(db_column='Numatomas komisinis dydis', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uzdarbis = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produktai_lt'
