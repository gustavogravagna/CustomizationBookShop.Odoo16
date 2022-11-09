from odoo import models, fields


# creando un modelo (tabla de la base de datos) a partir de una clase)
class Autor(models.Model):
    _name = 'autor'

    name = fields.Char(string="Nombre")