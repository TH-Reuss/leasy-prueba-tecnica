import uuid
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return super().update(deleted_at=timezone.now())

    def hard_delete(self):
        return super().delete()

    def restore(self):
        return super().update(deleted_at=None)

    def alive(self):
        return self.filter(deleted_at__isnull=True)

    def dead(self):
        return self.exclude(deleted_at__isnull=True)


class AllObjectsManager(models.Manager.from_queryset(SoftDeleteQuerySet)):
    pass

class SoftDeleteManager(AllObjectsManager):
    def get_queryset(self):
        return super().get_queryset().alive()

class BaseModel(models.Model):
    id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects      = SoftDeleteManager()
    all_objects  = AllObjectsManager()

    protected_relations = []
    cascade_delete_relations = []

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        # 1. Protección: ¿tiene relaciones que impiden eliminar?
        for rel in self.protected_relations:
            related_qs = getattr(self, rel).all()
            if related_qs.exists():
                raise ValidationError(f"No se puede eliminar porque tiene {rel} asociados.")

        # 2. Eliminación en cascada (soft delete en objetos relacionados)
        for rel in self.cascade_delete_relations:
            related_qs = getattr(self, rel).all()
            for obj in related_qs:
                obj.delete()

        # 3. Soft delete de este objeto
        self.deleted_at = timezone.now()
        self.save()


    def hard_delete(self, using=None, keep_parents=False):
        type(self).all_objects.filter(pk=self.pk).hard_delete()

    def restore(self):
        type(self).all_objects.filter(pk=self.pk).restore()