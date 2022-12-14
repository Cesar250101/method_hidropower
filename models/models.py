# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api

class NotaVenta(models.Model):
    _inherit = 'sale.order'

    repair_order_id = fields.Many2one('repair.order', string='Orden de Repración')
    repair_order_state = fields.Selection([
                                            ('draft', 'Quotation'),
                                            ('cancel', 'Cancelled'),
                                            ('confirmed', 'Confirmed'),
                                            ('under_repair', 'Under Repair'),
                                            ('ready', 'Ready to Repair'),
                                            ('2binvoiced', 'To be Invoiced'),
                                            ('invoice_except', 'Invoice Exception'),
                                            ('done', 'Repaired')], string='Estado RMA',
                                            related='repair_order_id.state')


class ReparacionCompras(models.Model):
    _inherit = 'repair.order'

    sale_order_id = fields.Many2one('sale.order', string='Nota de Venta')

    @api.multi
    def action_validate(self):
        if self.operations:
            value={
                'repair_order_id':self.id
            }
            self.sale_order_id.write(value)
        return super(ReparacionCompras, self).action_validate()            


class ModuleName(models.Model):
    _inherit = 'repair.order'

    vastago_diametro = fields.Float(string='Diametro')
    vastago_largo = fields.Float(string='Largo')
    botella_diametro_exterior = fields.Float(string='Diametro Exterior')
    botella_diametro_interior = fields.Float(string='Diametro Interior')
    botella_largo = fields.Float(string='Largo')
    longitud_cromo = fields.Float(string='Longitud Cromo')
    long_int_botella = fields.Float(string='Long.Int. Botella')    
    informe_entrada_ids = fields.One2many(comodel_name='method_hidropower.informe_entrada',inverse_name='repair_order_id', string='Informe de Entrada')
    informe_entrada_count = fields.Char(compute='_compute_informe_entrada_count', string='N° Informes Entradas')
    
    @api.depends('informe_entrada_ids')
    def _compute_informe_entrada_count(self):
        nro_informes=0
        for i in self.informe_entrada_ids:
            nro_informes+=1
        self.informe_entrada_count
        
    
        

    



    
class EstadoVastago(models.Model):
    _name = 'method_hidropower.estado_vastago'
    _description = 'Estado del vastago'

    name = fields.Char('Nombre Estado')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')
    es_otros = fields.Boolean(string='Es Otros', help='Indica si el estado corresponde al concepto de OTROS, si es así se activa una cuadro de texto')

class AccionVastago(models.Model):
    _name = 'method_hidropower.accion_vastago'
    _description = 'Acciones a realizar'

    name = fields.Char('Nombre Acción')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class CondicionAnclaje(models.Model):
    _name = 'method_hidropower.condicion_anclaje'
    _description = 'Condición del anclaje'

    name = fields.Char('Nombre Condicion Anclaje')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')
    
class CondicionAnclaje(models.Model):
    _name = 'method_hidropower.accion_anclaje'
    _description = 'Acción del anclaje'

    name = fields.Char('Nombre Acción Anclaje')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class EstadoBujeRotula(models.Model):
    _name = 'method_hidropower.estado_buje_rotula'
    _description = 'Estado Buje/Rotula'

    name = fields.Char('Nombre Estado Buje/Rotula')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class EstadoBotella(models.Model):
    _name = 'method_hidropower.estado_botella'
    _description = 'Estado Botella'

    name = fields.Char('Estado Botella')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class EstadoEntradaAceite(models.Model):
    _name = 'method_hidropower.estado_entrada_aceite'
    _description = 'Condición de entrada de aceite'

    name = fields.Char('Estado Entrada Aceite')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class AccionBotella(models.Model):
    _name = 'method_hidropower.accion_botella'
    _description = 'Acción a realizar Botella'

    name = fields.Char('Acción Botella')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')


class CondicionesInteriorBotella(models.Model):
    _name = 'method_hidropower.condiciones_interior_botella'
    _description = 'Condiciones interior botella'

    name = fields.Char('Condiciones interior botella')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class AccionInteriorBotella(models.Model):
    _name = 'method_hidropower.accion_interior_botella'
    _description = 'Acción a realizar interior botella'

    name = fields.Char('Acción interior botella')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')


class EstadoAnclajeBotella(models.Model):
    _name = 'method_hidropower.estado_anclaje_botella'
    _description = 'Estado anclaje de botella'

    name = fields.Char('Estado Anclaje botella')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class AcciónRealizarAnclajeBotella(models.Model):
    _name = 'method_hidropower.accion_anclaje_botella'
    _description = 'Acción a realizar anclaje de botella'

    name = fields.Char('Acción Realizar Anclaje botella')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class EstadoBujeRotula(models.Model):
    _name = 'method_hidropower.estado_buje_rotula'
    _description = 'Estado Buje/Rotula'

    name = fields.Char('Estado Buje/Rotula')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class CondicionPrensa(models.Model):
    _name = 'method_hidropower.condicion_prensa'
    _description = 'Condición de prensa'

    name = fields.Char('Condición Prensa')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class CondicionPrensa(models.Model):
    _name = 'method_hidropower.accion_prensa'
    _description = 'Acción a realizar prensa'

    name = fields.Char('Acción Realizar Prensa')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class CondicionPiston(models.Model):
    _name = 'method_hidropower.condicion_piston'
    _description = 'Condición de pistón'

    name = fields.Char('Condición pistón')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')

class AccionPiston(models.Model):
    _name = 'method_hidropower.accion_piston'
    _description = 'Acción a realizar pistón'

    name = fields.Char('Acción pistón')
    informe_entrada_id = fields.Many2one('method_hidropower.informe_entrada', string='Informe de Entrada')


class AccionRotulaBuje(models.Model):
    _name = 'method_hidropower.accion_rotula_buje'
    _description = 'Acción a realizar Rotulo/Buje'

    name = fields.Char('Nombre Acción Realizar Rotulo/Buje')

class AccionZoomInteriorBotella(models.Model):
    _name = 'method_hidropower.accion_zoom_botella'
    _description = 'Acción a realizar Rotulo/Buje'

    name = fields.Char('Nombre Acción Realizar Rotulo/Buje')

class AccionRealizarBujeRotula(models.Model):
    _name = 'method_hidropower.accion_realizar_buje_rotula'
    _description = 'Acción a realizar con buje/rotula'

    name = fields.Char('Nombre Acción Realizar Buje/Rotula')

    # select_5_5 = fields.Selection(string='Acción a realizar con buje/rotula', 
    #                                         selection=[('sin_intervencion', 'Sin intervención'), 
    #                                         ('fabricar', 'Fabricar buje (+B2)'),
    #                                         ('pulido', 'Pulido de buje'),
    #                                         ('cambio', 'Cambio de rotula'),
    #                                         ])

class InformeEntrada(models.Model):
    _name = 'method_hidropower.informe_entrada'
    _description = 'Informe de entrada'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Nombre Informe')    
    repair_order_id = fields.Many2one(comodel_name='repair.order', string='Orden de Reparación')    
    partner_id = fields.Many2one(comodel_name='res.partner', string='Cliente')    
    contacto = fields.Char(string='Atención a:')    
    referencia = fields.Char(string='Referencia')
    img_cilindro_completo = fields.Binary('Cilindro Completo')

    desarme_mostrar = fields.Boolean('Mostrar en Informe?',default=True)
    img_desarme_1 = fields.Binary('Imagen Desarme 1')
    img_desarme_2 = fields.Binary('Imagen Desarme 2')
    img_desarme_3 = fields.Binary('Imagen Desarme 3')
    txt_desarme = fields.Text(string='Texto Desarme')
    
    vastago_mostrar = fields.Boolean('Mostrar en Informe?',default=True)
    img_vastago_1 = fields.Binary('Imagen Vástago 1')
    img_vastago_2 = fields.Binary('Imagen Vástago 2')
    img_vastago_3 = fields.Binary('Imagen Vástago 3')
    select_2_1 = fields.One2many('method_hidropower.estado_vastago', 'informe_entrada_id', string='Estado Vastago')
    select_2_1_es_otro = fields.Boolean(string='Otro?')
    select_2_1_otros = fields.Char('Especificar')
    select_2_2 = fields.One2many('method_hidropower.accion_vastago','informe_entrada_id' ,string='Acciones Vastago')

    vastago_daño_mostrar = fields.Boolean('Mostrar en Informe?',default=True)                                                                
    img_vastago_daño = fields.Binary('Daño Vástago 1')
    img_vastago_daño_2 = fields.Binary('Daño Vástago 2')
    img_vastago_daño_3 = fields.Binary('Daño Vástago 3')
    img_vastago_daño_4 = fields.Binary('Daño Vástago 4')
    img_vastago_daño_5 = fields.Binary('Daño Vástago 5')
    txt_vastago_daño = fields.Text(string='Daño de vástago')

    anclaje_vastago_mostrar = fields.Boolean('Mostrar en Informe?',default=True)                                                                    
    img_anclaje_vastago = fields.Binary('Anclaje Vástago 1')
    img_anclaje_vastago_2 = fields.Binary('Anclaje Vástago 2')
    img_anclaje_vastago_3 = fields.Binary('Anclaje Vástago 3')
    select_3_1 = fields.One2many('method_hidropower.condicion_anclaje', 'informe_entrada_id', string='Estado Anclaje')
    select_3_2 = fields.One2many('method_hidropower.accion_anclaje', 'informe_entrada_id', string='Acción Anclaje')    
    select_3_3= fields.Selection(string='Buje/Rotula', 
                                            selection=[('buje', 'El Anclaje del vástago viene con buje'), 
                                            ('rotula', 'El Anclaje del vástago viene con rotula'),
                                            ('buje_rotula', 'El Anclaje del vástago viene sin buje/rotula'),
                                            ('nada', 'N/A'),
                                            ])
    select_3_5 = fields.Many2one('method_hidropower.accion_rotula_buje', string='Acción Realizar Rotulo/Buje')
    select_3_4 = fields.One2many('method_hidropower.estado_buje_rotula', 'informe_entrada_id', string='Estado Buje/Rotula')
                                            
    # select_3_5 = fields.Selection(string='Acción a realizar Buje/Rotula', 
    #                                         selection=[('sin', 'Sin intervención'), 
    #                                         ('fabricar', 'Fabricar buje(+B2)'),
    #                                         ('pulido', 'Pulido de buje'),
    #                                         ('cambio', 'Cambio de rotula'),
    #                                         ])
    select_3_6 = fields.Selection(string='Material Buje', 
                                            selection=[('bronce', 'Bronce'), 
                                            ('acero', 'Acero'),
                                            ('durocoton', 'Durocoton'),
                                            ('technill', 'Technill'),
                                            ])
    botella_mostrar = fields.Boolean('Mostrar en Informe?',default=True)                                                                                                                    
    img_botella = fields.Binary('Vista general botella') 
    img_botella_2 = fields.Binary('Vista general botella 2')
    img_botella_3 = fields.Binary('Vista general botella 3')  
    select_4_1 = fields.One2many('method_hidropower.estado_botella', 'informe_entrada_id', string='Estado Botella')
    select_4_2 = fields.One2many('method_hidropower.estado_entrada_aceite', 'informe_entrada_id', string='Estado Entrada Aceite')

    interior_botella_mostrar = fields.Boolean('Mostrar en Informe?',default=True)                                            
    select_4_3 = fields.One2many('method_hidropower.accion_botella', 'informe_entrada_id', string='Acción Realizar Botella')
    img_interior_botella = fields.Binary('Zoom interior de botella 1')                                            
    img_interior_botella_2 = fields.Binary('Zoom interior de botella 2')                                            
    img_interior_botella_3 = fields.Binary('Zoom interior de botella 3')                                            
    select_4_4 = fields.One2many('method_hidropower.condiciones_interior_botella', 'informe_entrada_id', string='Condición Interior Botella')
    select_4_4_1 = fields.One2many('method_hidropower.accion_interior_botella', 'informe_entrada_id', string='Acciones realizar interior botella')
    select_4_4_B = fields.Selection(string='Consecuencias estado botella', 
                                            selection=[('no_afecta', 'no afectan su optimo funcionamiento'), 
                                            ('afecta', ' afectan su optimo funcionamiento'),
                                            ])
    select_4_4_C = fields.Many2one('method_hidropower.accion_zoom_botella', string='Acción Realizar Zoom Botella')                                            

    anclaje_botella_mostrar = fields.Boolean('Mostrar en Informe?',default=True)
    img_anclaje_botella = fields.Binary('Anclaje de botella')
    img_anclaje_botella_2 = fields.Binary('Anclaje de botella 2')
    img_anclaje_botella_3 = fields.Binary('Anclaje de botella 3')
    select_5_1 = fields.One2many('method_hidropower.estado_anclaje_botella', 'informe_entrada_id', string='Estado Anclaje Botella')
    select_5_2 = fields.One2many('method_hidropower.accion_anclaje_botella', 'informe_entrada_id', string='Acción realizar Anclaje Botella')
    select_5_3 = fields.Selection(string='Buje/Rotula', 
                                            selection=[('buje', 'El Anclaje del vástago viene con buje'), 
                                            ('rotula', 'El Anclaje del vástago viene con rotula'),
                                            ('no_trae', 'El Anclaje del vástago viene sin buje/rotula'),
                                            ('na', 'N/A'),
                                            ])                                            
    select_5_4 = fields.One2many('method_hidropower.estado_buje_rotula', 'informe_entrada_id', string='Estado Buje/Rótula')
    # select_5_5 = fields.Selection(string='Acción a realizar con buje/rotula', 
    #                                         selection=[('sin_intervencion', 'Sin intervención'), 
    #                                         ('fabricar', 'Fabricar buje (+B2)'),
    #                                         ('pulido', 'Pulido de buje'),
    #                                         ('cambio', 'Cambio de rotula'),
    #                                         ])
    select_5_5 = fields.Many2one('method_hidropower.accion_realizar_buje_rotula', string='Acción Realizar Buje/Rotula')
    select_5_6 = fields.Selection(string='Material de buje', 
                                            selection=[('bronce', 'Bronce'), 
                                            ('acero', 'Acero'),
                                            ('durocoton', 'Durocoton'),
                                            ('technill', 'Technill'),
                                            ])
    tapa_prensa_mostrar = fields.Boolean('Mostrar en Informe?',default=True)                                            
    img_tapa_prensa = fields.Binary('Vista general tapa prensa')
    img_tapa_prensa_2 = fields.Binary('Vista general tapa prensa 2')
    img_tapa_prensa_3 = fields.Binary('Vista general tapa prensa 3')
    select_6_1 = fields.One2many('method_hidropower.condicion_prensa', 'informe_entrada_id', string='Condición Prensa')
    select_6_2 = fields.One2many('method_hidropower.accion_prensa', 'informe_entrada_id', string='Acción Prensa')
    select_6_3 = fields.Text('6.3 Texto fijo')

    piston_mostrar = fields.Boolean('Mostrar en Informe?',default=True)                                            
    img_piston = fields.Binary('Vista general pistón') 
    img_piston_2 = fields.Binary('Vista general pistón 2')
    img_piston_3 = fields.Binary('Vista general pistón 3')
    select_7_1 = fields.One2many('method_hidropower.condicion_piston', 'informe_entrada_id', string='Condición Pistón')    
    select_7_2 = fields.One2many('method_hidropower.accion_piston', 'informe_entrada_id', string='Acción realizar pistón')
    select_7_3 = fields.Text('7.3 Texto fijo')

    otros_mostrar = fields.Boolean('Mostrar en Informe?',default=True)                                            
    img_otros_1 = fields.Binary('Imagen 1')
    img_otros_2 = fields.Binary('Imagen 2')
    img_otros_3 = fields.Binary('Imagen 3')
    img_otros_4 = fields.Binary('Imagen 4')
    img_otros_5 = fields.Binary('Imagen 5') 
    txt_otros = fields.Text('Texto')

    observaciones = fields.Text(string='Observaciones')

    vastago_exterior = fields.Char('Ø Exterior')
    vastago_longitud_cromo = fields.Char('Longitud de cromo')
    vastago_longitud_centro = fields.Char('Longitud de centro')
    vastago_longitud_total = fields.Char('Longitud total')
    vastago_flexion = fields.Char('Flexión')
    vastago_tipo_cromo = fields.Char('Tipo de cromo')
                                                
    botella_exterior = fields.Char('Ø Exterior')
    botella_interior = fields.Char('Ø Interior')   
    botella_longitud_interior = fields.Char('Longitud interior')
    botella_longitud_centro = fields.Char('Longitud de centro')
    botella_longitud_total = fields.Char('Longitud total')
    botella_ovalación = fields.Char('Ovalación')

    piston_exterior= fields.Char('Ø Exterior')
    piston_interior= fields.Char('Ø Interior')
    piston_ancho= fields.Char('Ancho')
    piston_material= fields.Char('Material')

    prensa_exterior= fields.Char('Ø Exterior')
    prensa_interior= fields.Char('Ø Interior')
    prensa_ancho= fields.Char('Ancho')
    prensa_material= fields.Char('Material')

    anclaje_vastago_exterior= fields.Char('Ø Exterior (buje/rotula')
    anclaje_vastago_interior= fields.Char('Ø Interior (buje/rotula')
    anclaje_vastago_ancho= fields.Char('Ancho')
    anclaje_vastago_material= fields.Char('Material')

    anclaje_botella_exterior= fields.Char('Ø Exterior (buje/rotula')
    anclaje_botella_interior= fields.Char('Ø Interior (buje/rotula')
    anclaje_botella_ancho= fields.Char('Ancho')
    anclaje_botella_material= fields.Char('Material')

    




                                        

    
    



