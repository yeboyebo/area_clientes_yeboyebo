# @class_declaration interna #
from YBLEGACY import qsatype
from django.shortcuts import render


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration head #
class head(interna):

    def areaclientes_cargadoc(self, request):
        # usuario = qsatype.FLUtil.nameUser()
        return render(request, 'areaclientes/index.html', {})

    def __init__(self, context=None):
        super(head, self).__init__(context)

    def cargadoc(self, request):
        return self.ctx.areaclientes_cargadoc(request)

# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super(ifaceCtx, self).__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
