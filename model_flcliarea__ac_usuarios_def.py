# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration area_clientes_yeboyebo #
from YBLEGACY.constantes import *


class area_clientes_yeboyebo(interna):

    def area_clientes_yeboyebo_getDesc(self):
        return None

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.area_clientes_yeboyebo_getDesc()


# @class_declaration head #
class head(area_clientes_yeboyebo):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
