# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api

class Otros(models.Model):
    _name = 'method_hidropower.otros'
    _description = 'Selección multiple de otros '

    name = fields.Char(string='Nombre')
    informe_salida_id = fields.Many2one(comodel_name='method_hidropower.informe_salida', string='Informe de Salida')
    
class SelloTapaPrensa1(models.Model):
    _name = 'method_hidropower.sello_tapa_prensa_1'
    _description = 'Sello tapa prensa 1'

    name = fields.Char(string='Nombre')
    informe_salida_id = fields.Many2one(comodel_name='method_hidropower.informe_salida', string='Informe de Salida')

class SelloPiston(models.Model):
    _name = 'method_hidropower.sello_piston'
    _description = 'Sello Pistón'

    name = fields.Char(string='Nombre')
    informe_salida_id = fields.Many2one(comodel_name='method_hidropower.informe_salida', string='Informe de Salida')

class ReemplazoRotula(models.Model):
    _name = 'method_hidropower.reemplazo_rotula'
    _description = 'Reemplazo de rótulas'

    name = fields.Char(string='Nombre')
    informe_salida_id = fields.Many2one(comodel_name='method_hidropower.informe_salida', string='Informe de Salida')

class FabricacionPiezas(models.Model):
    _name = 'method_hidropower.fabricacion_piezas'
    _description = 'Fabricación Piezas'

    name = fields.Char(string='Nombre')
    informe_salida_id = fields.Many2one(comodel_name='method_hidropower.informe_salida', string='Informe de Salida')


class SelloPiston(models.Model):
    _name = 'method_hidropower.concluciones'
    _description = 'Informe de Salida - Concluciones'

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
    sello_tapa_prensa_ids = fields.One2many('method_hidropower.sello_tapa_prensa_1', 'informe_salida_id', string='Sello Tapa Prensa 1')

    img_3_1=fields.Binary('Imagen sello pistón 1')
    img_3_2=fields.Binary('Imagen sello pistón 2')
    img_3_3=fields.Binary('Imagen sello pistón 3')    
    sello_piston_ids = fields.One2many('method_hidropower.sello_piston', 'informe_salida_id', string='Sello Pistón')

    img_reemplazo_rotula_1 = fields.Binary('Imagen reemplazo rótula 1')
    img_reemplazo_rotula_2 = fields.Binary('Imagen reemplazo rótula 2')
    img_reemplazo_rotula_3 = fields.Binary('Imagen reemplazo rótula 3')
    reemplazo_rotula_ids = fields.One2many('method_hidropower.reemplazo_rotula', 'informe_salida_id', string='Reemplazo Rótula')

    img_fabricacion_piezas_1 = fields.Binary('Imagen reemplazo rótula 1')
    img_fabricacion_piezas_2 = fields.Binary('Imagen reemplazo rótula 2')
    img_fabricacion_piezas_3 = fields.Binary('Imagen reemplazo rótula 3')
    img_fabricacion_piezas_4 = fields.Binary('Imagen reemplazo rótula 4')
    img_fabricacion_piezas_5 = fields.Binary('Imagen reemplazo rótula 5')
    img_fabricacion_piezas_6 = fields.Binary('Imagen reemplazo rótula 6')
    fabricacion_piezas_ids = fields.One2many('method_hidropower.fabricacion_piezas', 'informe_salida_id', string='Fabricación Piezas')


    img_4_1=fields.Binary('Fotografia 1 Instalacion prensa piston')
    img_4_2=fields.Binary('Fotografia 2 Armado de Cilindro')
    img_4_3=fields.Binary('Fotografia 3 Torque de perno')
    
    img_5_1=fields.Binary('Fotografia 1 Instalacion manguera y recorrido de vastago')

    img_6_1=fields.Binary('Fotografia 1 con manemetro indicado presion maxima')
    txt_6_1 = fields.Text(string='Texto Presión interna área base prensa  de cilindro')
    
    img_7_1=fields.Binary('Presión interna área base pistón de cilindro.')
    txt_7_1 = fields.Text(string='Texto Presión interna área base pistón de cilindro.')

    img_presion_cilindro = fields.Binary('Presión en Cilindro')
    txt_presion_cilindro = fields.Text(string='Texto Presión interna área base pistón de cilindro.',
                                        default='Cilindro NO presenta fuga de aceite')

    img_8_1=fields.Binary('Imagen presión en cilindro junto a reloj comparador')
    txt_8_1 = fields.Text(string='Texto Imagen presión en cilindro junto a reloj comparador',
                                defaul='Cilindro no presenta fuga de aceite - No presenta by pass - No presenta diferencia en medidas de en reloj comparador * Dejar Opcion de texto abierto')

    img_9_1=fields.Binary('Cierre de proceso')
    txt_9_1 = fields.Text(string='Texto Cierre de proceso',default='Texto Fijo: Equipo cumple las prueba hidraulica.')

    img_10_1=fields.Binary('Gráfico test senso node parker')
    txt_10_1 = fields.Text(string='Test senso node parker',default='Se agregan graficos del test de senso node parker con registro de las presiones por segundo.')


    conclucion_ids = fields.One2many('method_hidropower.concluciones', 'informe_salida_id', string='Sello Pistón')


