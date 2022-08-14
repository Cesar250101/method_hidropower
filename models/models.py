# -*- coding: utf-8 -*-

from odoo import models, fields, api


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
        
    
    
class Otros(models.Model):
    _name = 'method_hidropower.otros'
    _description = 'Selección multiple de otros '

    name = fields.Char(string='Nombre')
    informe_salida_id = fields.Many2one(comodel_name='method_hidropower.informe_salida', string='Informe de Salida')
    

    


class InformeSalida(models.Model):
    _name = 'method_hidropower.informe_salida'
    _description = 'Informe de Salida'

    name = fields.Char(string='Nombre Informe')    
    repair_order_id = fields.Many2one(comodel_name='repair.order', string='Orden de Reparación')    
    partner_id = fields.Many2one(comodel_name='res.partner', string='Cliente')    
    nombre_cilindro = fields.Char(string='Nombre Cilindro')    
    modelo_cilindro = fields.Char(string='Modelo Cilindro')    
    seriecilindro = fields.Char(string='Serie Cilindro')    
    
    mecanico = fields.Char(string='Mecánico')    
    fecha_test = fields.Date(string='Fecha Test')
    presion_max = fields.Char(string='Pesión Máxima')    
    presion_min = fields.Char(string='Pesión Mínima')    
    presion_util = fields.Char(string='Pesión Utilizada')    
    duracion_text = fields.Char(string='Duranción Test')    
    duracion_text_senso = fields.Char(string='Duración test senson node blue parker')    
    hora_text = fields.Char(string='Hora Test')    

    otros = fields.One2many('method_hidropower.otros', 'informe_salida_id', string='Otros Servicios')

    img_1=fields.Binary('Imagen kit sello')
    img_2_1=fields.Binary('Imagen sello tapa prensa 1')
    img_2_2=fields.Binary('Imagen sello tapa prensa 2')
    img_2_3=fields.Binary('Imagen sello tapa prensa 3')
    select_2_1 = fields.Selection(string='sello tapa prensa 1', 
                    selection=[('1', 'Se reaiiza pulido y lavada de Tapa prensa'), 
                    ('2', 'Se realiza instalacion de sellos a tapa prensa'),
                    ('3', 'Se recupera pista de sello vastago a tapa prensa'),
                    ('4', 'Se instala sellos k17 a tapa prensa'),
                    ('5', 'Se recuperan hilos de tapa prensa'),
                    ('6', 'Se fabrica tapa prensa según muestra'),
                    ('7', 'Se fabrica tapa prensa según plano'),
                    ])
    select_2_2 = fields.Selection(string='sello tapa prensa 2', 
                    selection=[('1', 'Se reaiiza pulido y lavada de Tapa prensa'), 
                    ('2', 'Se realiza instalacion de sellos a tapa prensa'),
                    ('3', 'Se recupera pista de sello vastago a tapa prensa'),
                    ('4', 'Se instala sellos k17 a tapa prensa'),
                    ('5', 'Se recuperan hilos de tapa prensa'),
                    ('6', 'Se fabrica tapa prensa según muestra'),
                    ('7', 'Se fabrica tapa prensa según plano'),
                    ])
    select_2_3 = fields.Selection(string='sello tapa prensa 3', 
                    selection=[('1', 'Se reaiiza pulido y lavada de Tapa prensa'), 
                    ('2', 'Se realiza instalacion de sellos a tapa prensa'),
                    ('3', 'Se recupera pista de sello vastago a tapa prensa'),
                    ('4', 'Se instala sellos k17 a tapa prensa'),
                    ('5', 'Se recuperan hilos de tapa prensa'),
                    ('6', 'Se fabrica tapa prensa según muestra'),
                    ('7', 'Se fabrica tapa prensa según plano'),
                    ])
    img_3_1=fields.Binary('Imagen sello pistón 1')
    img_3_2=fields.Binary('Imagen sello pistón 2')
    img_3_3=fields.Binary('Imagen sello pistón 3')
    select_3_1 = fields.Selection(string='Sello pistón 1', 
                    selection=[('1', 'Se reaiiza pulido y lavada de piston'), 
                    ('2', 'Se realiza instalacion de sellos a piston'),
                    ('3', 'Se recupera pista diametro exterior de piston'),
                    ('5', 'Se recuperan hilos diametro interior de piston'),
                    ('5', 'Se recuperan hilos de tapa prensa'),
                    ('6', 'Se fabrica piston según muestra'),
                    ('7', 'Se fabrica piston según plano'),
                    ])
    select_3_2 = fields.Selection(string='Sello pistón 2', 
                    selection=[('1', 'Se reaiiza pulido y lavada de piston'), 
                    ('2', 'Se realiza instalacion de sellos a piston'),
                    ('3', 'Se recupera pista diametro exterior de piston'),
                    ('5', 'Se recuperan hilos diametro interior de piston'),
                    ('5', 'Se recuperan hilos de tapa prensa'),
                    ('6', 'Se fabrica piston según muestra'),
                    ('7', 'Se fabrica piston según plano'),
                    ])
    select_3_3 = fields.Selection(string='Sello pistón 3', 
                    selection=[('1', 'Se reaiiza pulido y lavada de piston'), 
                    ('2', 'Se realiza instalacion de sellos a piston'),
                    ('3', 'Se recupera pista diametro exterior de piston'),
                    ('5', 'Se recuperan hilos diametro interior de piston'),
                    ('5', 'Se recuperan hilos de tapa prensa'),
                    ('6', 'Se fabrica piston según muestra'),
                    ('7', 'Se fabrica piston según plano'),
                    ])
    img_4_1=fields.Binary('Fotografia 1 Instalacion prensa piston')
    img_4_2=fields.Binary('Fotografia 2 Armado de Cilindro')
    img_4_3=fields.Binary('Fotografia 3 Torque de perno')
    
    img_5_1=fields.Binary('Fotografia 1 Instalacion manguera y recorrido de vastago')

    img_6_1=fields.Binary('Fotografia 1 con manemetro indicado presion maxima')
    txt_6_1 = fields.Text(string='Texto Presión interna área base prensa  de cilindro')
    
    img_7_1=fields.Binary('Presión interna área base pistón de cilindro.')
    txt_7_1 = fields.Text(string='Texto Presión interna área base pistón de cilindro.')

    img_8_1=fields.Binary('Imagen presión en cilindro junto a reloj comparador')
    txt_8_1 = fields.Text(string='Texto Imagen presión en cilindro junto a reloj comparador')

    img_9_1=fields.Binary('Cierre de proceso')
    txt_9_1 = fields.Text(string='Texto Cierre de proceso')

    conclusion = fields.Text(string='Conclusión')


    

    


class InformeEntrada(models.Model):
    _name = 'method_hidropower.informe_entrada'
    _description = 'Informe de entrada'

    name = fields.Char(string='Nombre Informe')    
    repair_order_id = fields.Many2one(comodel_name='repair.order', string='Orden de Reparación')    
    partner_id = fields.Many2one(comodel_name='res.partner', string='Cliente')    
    contacto = fields.Char(string='Atención a:')    
    referencia = fields.Char(string='Referencia')
    img_cilindro_completo = fields.Binary('Cilindro Completo')
    img_desarme = fields.Binary('Imagen Desarme')
    txt_desarme = fields.Text(string='Texto Desarme')
    img_vastago = fields.Binary('Imagen Vástago')
    select_2_1 = fields.Selection(string='Vastago', 
                                    selection=[('bueno', 'En buenas condiciones'), 
                                    ('piting', 'Con Piting en su manto de cromo'),
                                    ('golpe', 'Con Golpe en manto de cromo'),
                                    ('flexion', 'con Flexion'),
                                    ('despendimiento', 'Con Des´rendimiento de cromo'),
                                    ('oxido', 'Con Oxido'),
                                    ('quebrado', 'Quebrado'),
                                    ('fisurado', 'Fisurado'),
                                    ('fisura_soldaura', 'Fisura en soldadura'),
                                    ('arrastre', 'Con arrastre de material'),
                                    ('puño', 'Puño cortado'),
                                    ('hilo', 'Daño en hilo de spiga'),
                                    ])
    select_2_2 = fields.Selection(string='Acción', 
                                            selection=[('pilido', 'Pulido de vastago'), 
                                            ('fabricacion', 'Fabricación de vastago'),
                                            ('descromado', 'Descromado y cromado'),
                                            ('recuperacion', 'Recuperación puntual'),
                                            ('hvof', 'Hvof'),
                                            ])
                                                                
    img_vastago_daño = fields.Binary('Daño Vástago')
    txt_vastago_daño = fields.Text(string='Daño de vástago')
    img_anclaje_vastago = fields.Binary('Anclaje Vástago')
    select_3_1 = fields.Selection(string='Condición del Anclaje', 
                                            selection=[('sin_puño', 'Sin puño'), 
                                            ('buena', 'En buenas condiciones'),
                                            ('deformado', 'Con el puño deformado por daño'),
                                            ('quebrado', 'Con el puño quebrado'),
                                            ('fuera_medida', 'Con alojamiento de puño fuera de medida'),
                                            ('fuera_medida', 'Con alojamiento de puño fuera de medida'),
                                            ('arrastre', 'Con alojamiento con arrastre'),
                                            ])
    select_3_3= fields.Selection(string='Buje/Rotula', 
                                            selection=[('buje', 'Buje'), 
                                            ('rotula', 'Rotula'),
                                            ('deformado', 'No trae rotula/buje'),
                                            ('nada', 'N/A'),
                                            ])
    select_3_2 = fields.Selection(string='Acción Realizar', 
                                            selection=[('sin', 'Sin intervención'), 
                                            ('fabricar', 'Fabricar puño'),
                                            ('recuperar', 'Recuperación de puño diametro exterior'),
                                            ('recuperar_interior', 'Recuperación de diametro interior'),
                                            ('cambio', 'Cambio de rotula/buje'),
                                            ('pulido', 'Pulido de alojamiento'),
                                            ])
    select_3_4 = fields.Selection(string='Estado Buje/Rotula', 
                                            selection=[('fuera_medida_interior', 'Buje con diametro interior fuera de medida'), 
                                            ('fuera_medida_exterior', 'Buje con diametro exterior fuera de medida'),
                                            ('buje_arrastre_material', 'Buje presenta arrastre de material'),
                                            ('buje_quebrado', 'Buje Quebrado'),
                                            ('buje_fisura', 'Buje presenta fisura'),
                                            ('juego_axial', 'Rotula con juego axial'),
                                            ('juego_radial', 'Rotula con juego radial'),
                                            ('quebrada', 'Rotula Quebrada'),
                                            ])
    select_3_5 = fields.Selection(string='Acción a realizar Buje/Rotula', 
                                            selection=[('sin', 'Sin intervención'), 
                                            ('fabricar', 'Fabricar buje(+B2)'),
                                            ('pulido', 'Pulido de buje'),
                                            ('cambio', 'Cambio de rotula'),
                                            ])
    select_3_6 = fields.Selection(string='Material Buje', 
                                            selection=[('bronce', 'Bronce'), 
                                            ('acero', 'Acero'),
                                            ('durocoton', 'Durocoton'),
                                            ('technill', 'Technill'),
                                            ])
    img_botella = fields.Binary('Vista general botella')                                            
    select_4_1 = fields.Selection(string='Exterior Botella', 
                                            selection=[('bueno', 'Buenas condiciones'), 
                                            ('flextado', 'Flectado'),
                                            ('daño', 'Con daño/golpes en el exterior de botella'),
                                            ('fisura', 'Fisura en soldadura'),
                                            ('hilo', 'Daños en hilo de prensa'),
                                            ('cañeria', 'Daños en amarre de soporte de cañeria'),
                                            ])
    select_4_2 = fields.Selection(string='Condición de entrada de aceite', 
                                            selection=[('golpe_externo', 'Golpe Externo'), 
                                            ('deformacion', 'Deformación de Niples'),
                                            ('mal_estado', 'Hllos en mal estado'),
                                            ('sin_niples', 'Sin Niples'),
                                            ('fisura', 'Fisura en saldadura'),
                                            ])
    select_4_3 = fields.Selection(string='Acción a realizar Botella', 
                                            selection=[('bruñido', 'Bruñido de botella'), 
                                            ('fabricacion', 'Fabricación de botella'),
                                            ('recuperacion_e', 'Recuperación externa'),
                                            ('recuperacion_sb', 'Recuperación de soldadura de botella'),
                                            ('fabricar_amarres', 'Fabricar amarres de soporte'),
                                            ('cambio_niples', 'Cambio de niples'),
                                            ('recuperar_fisura_soldadura', 'Recuperación fisura de soldadura de niples'),
                                            ])
    img_interior_botella = fields.Binary('Zoom interior de botella')                                            
    select_4_4 = fields.Selection(string='Condiciones interior botella', 
                                            selection=[('buena', 'En buenas condiciones'), 
                                            ('arrastre_material', 'Con arrastre de material en su interior'),
                                            ('golpes_internos', 'Con golpes internos'),
                                            ('fuera_medida', 'Fuera de medida en el diametro interior'),
                                            ('cavitacion', 'cavitación (corroción) en su diametro interior'),
                                            ])
    img_anclaje_botella = fields.Binary('Anclaje de botella')                                            
    select_5_1 = fields.Selection(string='Estado anclaje de botella', 
                                            selection=[('sin_puño', 'Sin puño'), 
                                            ('buena', 'En buenas condiciones'),
                                            ('puño_quebrado', 'Con el puño quebrado'),
                                            ('fuera_medida', 'Con alojamiento de puño fuera de medida'),
                                            ('alojamiento_arrastre', 'Con alojamiento con arrastre'),
                                            ])
    select_5_2 = fields.Selection(string='Acción a realizar anclaje de botella', 
                                            selection=[('sin_intervencion', 'Sin intervención'), 
                                            ('fabricar', 'Fabricar puño'),
                                            ('recuperacion_puño', 'Recuperación de puño diametro exterior'),
                                            ('recuperacion_diametro', 'Recuperación de diametro interior'),
                                            ('cambio_rotula', 'Cambio de rotula/buje'),
                                            ('pulido_alojamento', 'Pulido de Alojamiento'),
                                            ])
    select_5_3 = fields.Selection(string='Buje/Rotula', 
                                            selection=[('buje', 'Buje'), 
                                            ('rotula', 'Rotula'),
                                            ('no_trae', 'No trae rotula/buje'),
                                            ('na', 'N/A'),
                                            ])
    select_5_4 = fields.Selection(string='Estado Buje/Rotula', 
                                            selection=[('buje_fuera_medida', 'Buje con diametro interior fuera de medida'), 
                                            ('buje_diametro_fuera_medida', 'Buje con diametro exterior fuera de medida'),
                                            ('arrastre_metrial', 'Buje presenta arrastre de material'),
                                            ('buje_quebrado', 'Buje quebrado'),
                                            ('fisura', 'Buje presenta fisura'),
                                            ('juego_axial', 'Rotula con juego axial'),
                                            ('juego_radial', 'Rotula con juego radial'),
                                            ('quebrada', 'Rotula quebrada'),
                                            ])
    select_5_5 = fields.Selection(string='Acción a realizar con buje/rotula', 
                                            selection=[('sin_intervencion', 'Sin intervención'), 
                                            ('fabricar', 'Fabricar buje (+B2)'),
                                            ('pulido', 'Pulido de buje'),
                                            ('cambio', 'Cambio de rotula'),
                                            ])
    select_5_6 = fields.Selection(string='Material de buje', 
                                            selection=[('bronce', 'Bronce'), 
                                            ('acero', 'Acero'),
                                            ('durocoton', 'Durocoton'),
                                            ('technill', 'Technill'),
                                            ])
    img_tapa_prensa = fields.Binary('Vista general tapa prensa')                                            
    select_6_1 = fields.Selection(string='Condición de prensa', 
                                            selection=[('buena', 'Buenas condiciones'), 
                                            ('fuera_medida_interior', 'Fuera de medida en el diametro interior'),
                                            ('fuera_medida_exterior', 'Fuera de medida en el diametro exterior'),
                                            ('golpe', 'Presenta Golpe/Arrastre de meterial'),
                                            ('sellos', 'Canal de sellos fuera de medida'),
                                            ('hilo', 'Hilos con daños'),
                                            ('fisura', 'Presenta fisura'),
                                            ])
    select_6_2 = fields.Selection(string='Acción a realizar prensa', 
                                            selection=[('pulido', 'Pulido'), 
                                            ('fabricacion', 'Fabricación'),
                                            ('recuperacion_medida_interior', 'Recuperación de medidas interior'),
                                            ('recuperacion_medida_exterior', 'Recuperación de medidas exterior'),
                                            ('recuperacion_sellos', 'Recueración de canal de sellos'),
                                            ('recuperacion_hilo', 'Recuperación de hilo'),
                                            ])
    img_piston = fields.Binary('Vista general pistón') 
    select_7_1 = fields.Selection(string='Condición de pistón', 
                                            selection=[('buena', 'Buenas condiciones'), 
                                            ('fuera_medida_di', 'Fuera de medida en el diametro interior'),
                                            ('fuera_medida_de', 'Fuera de medida en el diametro exterior'),
                                            ('recuperacion_medida_exterior', 'Presenta golpes/arrastre de material'),
                                            ('sello_fuera_medida', 'Canal de sellos fuera de medida'),
                                            ('hilo_daño', 'Hilo con daños'),
                                            ('fisura', 'Presenta fisura'),
                                            ])    
    select_7_2 = fields.Selection(string='Acción a realizar pistón', 
                                            selection=[('pulido', 'Pulido'), 
                                            ('fabricacion', 'Fabricación'),
                                            ('recuperacion_interior', 'Recuperación de medidas interior'),
                                            ('recuperacion_exterior', 'Recuperación de medidas exterior'),
                                            ('recuperacion_sellos', 'Recuperación de canal de sellos'),
                                            ('recuperacion_hilo', 'Recuperación de hilo'),
                                            ])    
    observaciones = fields.Text(string='Observaciones')
                                                

                                        

    
    



