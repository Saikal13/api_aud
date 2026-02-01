from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)  # краткая биография
    photo = models.ImageField(upload_to='teachers/', null=True, blank=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)  # название класса/темы
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='classes'
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    description = models.TextField(blank=True)
    book_class = models.ForeignKey(
        Class, on_delete=models.SET_NULL, null=True, blank=True, related_name='books'
    )

    def __str__(self):
        return self.title


class Audio(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='audios'
    )  # обязательно, чтобы избежать IntegrityError
    title = models.CharField(max_length=200, blank=True)  # название главы или аудиофайла
    audio_file = models.FileField(upload_to='audiobooks/')
    duration = models.DurationField(null=True, blank=True)  # длина аудио
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title:
            return f"{self.book.title} - {self.title}"
        return f"{self.book.title} - Audio"
