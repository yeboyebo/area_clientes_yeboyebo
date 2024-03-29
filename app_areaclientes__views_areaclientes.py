# @class_declaration interna #
from YBLEGACY import qsatype
from django.shortcuts import render
from YBUTILS.viewREST import helpers


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def areaclientes_cargadoc(self, request):
        return self.iface.cargadocparam(request, "index.html")

    def areaclientes_cargadocparam(self, request, match):
        usuario = qsatype.FLUtil.nameUser()
        codfuncional = qsatype.FLUtil.sqlSelect("ac_usuarios", "codfuncional", "nombre = '{}'".format(usuario))
        if not codfuncional:
            codfuncional = usuario

        if match.endswith("/"):
            match = match[:len(match) - 1]

        return render(request, "areaclientes/page.html", {"usuario": usuario, "doc_cliente": codfuncional, "nuevaUrl": match})

    def __init__(self, context=None):
        self.ctx = context

    @helpers.decoradores.check_authentication_iface
    def cargadoc(self, request):
        return self.ctx.areaclientes_cargadoc(request)

    @helpers.decoradores.check_authentication_iface
    def cargadocparam(self, request, match):
        return self.ctx.areaclientes_cargadocparam(request, match)


# @class_declaration head #
class head(interna):

    def __init__(self, context=None):
        super(head, self).__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super(ifaceCtx, self).__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
