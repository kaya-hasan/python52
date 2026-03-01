from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True)

    # CASCADE kodu eğer kullanıcı silinirse yazılar da silinir
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    status = models.CharField(
        max_length=15,
        choices=[
            ('draft', 'Oluşturulmuş Taslak'),
            ('publish', 'Yayımlanmıştır')
        ],
        default='draft'
    )

    # ManyToMany - Bir yazının birden fazla etiketi olabilir
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-publish']
        verbose_name = 'AdminPanel'
        verbose_name_plural = 'AdminPaneller'
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return self.title


class Profile(models.Model):
    # OneToOne - Her yazarın tek bir profili vardır
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username


# ForeignKey - Bir yazının tek bir yazarı vardır,
# ancak bir yazarın birden fazla yazısı olabilir.

# ManyToMany - Bir yazının birden fazla etiketi olabilir
# ve bir etiket birden fazla yazıya ait olabilir.

# OneToOne - Her yazarın tek bir profili vardır
# ve her profil tek bir yazara aittir.


# migration - veritabanında tablo oluşturma işlemi
# models.py'yi değiştiririz ardından makemigrations ile migration dosyası oluşturur
# sonrasında migrate koduyla db'e bunu uygularız.

# makemigrations ile değişiklikleri otomatik tespit ederek dosya oluşturulur
# db değiştirilmez sadece migrations/ klasöründe yeni python dosyası oluşturulur

# python manage.py makemigrations
# python manage.py makemigrations blog

# migrate de ise oluşturulan dosya direkt db'e yazılır
# python manage.py migrate
# python manage.py migrate blog

# python manage.py migrate blog 001 -> başka versiyonlara da dönülebilir

# python manage.py showmigrations -> migration durumunu check etmek için kullanılır
# python manage.py sqlmigrate -> Migration'ın SQL çıktısını gösterir

# Admin panel ve superuser oluşturma
# python manage.py createsuperuser

# -----------------------------
# TAG (ManyToMany) KULLANIM ÖRNEKLERİ
# -----------------------------

# 1️⃣ Tag oluşturma
# tag1 = Tag.objects.create(name="Django")
# tag2 = Tag.objects.create(name="Python")

# 2️⃣ Post oluşturma
# post = Post.objects.create(
#     title="Django Eğitimi",
#     slug="django-egitimi",
#     author=User.objects.get(id=1),
#     body="İçerik burada..."
# )

# 3️⃣ Post'a etiket ekleme
# post.tags.add(tag1, tag2)

# 4️⃣ Post'tan etiket silme
# post.tags.remove(tag1)

# 5️⃣ Post'un tüm etiketlerini listeleme
# post.tags.all()

# 6️⃣ Belirli bir etiketin bağlı olduğu tüm postları listeleme
# tag = Tag.objects.get(id=1)
# tag.post_set.all()

# Eğer related_name tanımlarsan:
# tags = models.ManyToManyField(Tag, related_name="posts")

# O zaman erişim:
# tag.posts.all()

# 7️⃣ Post'un tüm etiketlerini temizleme
# post.tags.clear()
