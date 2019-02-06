# @class_declaration interna_ac_usuarios #
import importlib

from YBUTILS.viewREST import helpers

from models.flcliarea import models as modelos


class interna_ac_usuarios(modelos.mtd_ac_usuarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration area_clientes_yeboyebo_ac_usuarios #
class area_clientes_yeboyebo_ac_usuarios(interna_ac_usuarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration ac_usuarios #
class ac_usuarios(area_clientes_yeboyebo_ac_usuarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flcliarea.ac_usuarios_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
