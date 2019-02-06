from django.db import models

from YBLEGACY.FLUtil import FLUtil
from YBLEGACY.clasesBase import BaseModel


def _miextend(self, **kwargs):
    self._legacy_mtd = kwargs
    return self


models.Field._miextend = _miextend


class mtd_ac_usuarios(models.Model, BaseModel):
    idusuario = models.AutoField(db_column="idusuario", verbose_name=FLUtil.translate(u"Identificador", u"MetaData"), primary_key=True)._miextend(visiblegrid=False, OLDTIPO="SERIAL")
    nombre = models.CharField(blank=False, null=True, max_length=100)._miextend(OLDTIPO="STRING")
    password = models.TextField(blank=False, null=True)._miextend(OLDTIPO="STRING")
    esadmin = models.NullBooleanField(db_column="esadmin", verbose_name=FLUtil.translate(u"Admin", u"MetaData"), default=False, null=True)._miextend(OLDTIPO="BOOL")
    codfuncional = models.CharField(blank=True, null=True, max_length=15)._miextend(OLDTIPO="STRING")

    class Meta:
        managed = True
        verbose_name = FLUtil.translate(u"Usuarios area clientes", u"MetaData")
        db_table = 'ac_usuarios'
