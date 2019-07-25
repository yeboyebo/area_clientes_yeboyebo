from django.db import models

from YBLEGACY.FLUtil import FLUtil
from YBLEGACY.clasesBase import BaseModel


def _miextend(self, **kwargs):
    self._legacy_mtd = kwargs
    return self


models.Field._miextend = _miextend


class mtd_ac_usuarios(models.Model, BaseModel):
    idusuario = models.AutoField(db_column="idusuario", verbose_name=FLUtil.translate("MetaData", "Identificador"), primary_key=True)._miextend(visiblegrid=False, OLDTIPO="SERIAL")
    nombre = models.CharField(blank=False, null=True, max_length=100)._miextend(OLDTIPO="STRING")
    password = models.TextField(blank=False, null=True)._miextend(OLDTIPO="STRING")
    esadmin = models.NullBooleanField(db_column="esadmin", verbose_name=FLUtil.translate("MetaData", "Admin"), default=False, null=True)._miextend(OLDTIPO="BOOL")
    codfuncional = models.CharField(blank=True, null=True, max_length=15)._miextend(OLDTIPO="STRING")

    class Meta:
        managed = True
        verbose_name = FLUtil.translate("MetaData", "Usuarios area clientes")
        db_table = 'ac_usuarios'
