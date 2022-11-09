from odoo import models, fields


# creando un modelo (tabla de la base de datos) a partir de una clase)
class Libros(models.Model):
    _name = 'libros'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Nombre del Libro', required=True, tracking=True)
    editorial = fields.Char(string='Editorial', required=True, tracking=True)
    isbn = fields.Char(string='ISBN', required=True, tracking=True)
    autor_id = fields.Many2one(comodel_name='autor', string='autor', required=True, tracking=True)
    image = fields.Binary(string='Image')

    _sql_constraints = [("name_uniq","unique (name)", "El nombre del libro ya existe.")]
