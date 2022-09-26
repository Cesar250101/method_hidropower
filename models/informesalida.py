# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Otros(models.Model):
    _name = 'method_hidropower.otros'
    _description = 'Selección multiple de otros '

    name = fields.Char(string='Nombre')
    informe_salida_id = fields.Many2one(comodel_name='method_hidropower.informe_salida', string='Informe de Salida')
    
class InformeSalida(models.Model):
    _name = 'method_hidropower.informe_salida'
    _description = 'Informe de Salida'

    name = fields.Char(string='Nombre Informe')    
    repair_order_id = fields.Many2one(comodel_name='repair.order', string='Orden de Reparación',required=True)    
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

    otros_servicios = fields.One2many('method_hidropower.otros', 'informe_salida_id', string='Otros Servicios')

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


