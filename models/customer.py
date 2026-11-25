from odoo import fields,models

class Customer(models.Model):
    _name = "autofix.customer"
    _description = "Autofix  Customer"
    
    name=fields.Char(string="Name", required=True)
    birthdate = fields.date(string="Birthdate")
    id_card = fields.Integer(string="ID card")
    phone = fields.Char(string="Numbre Phone")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address")
    vehicle_ids = fields.One2Many(comodel_name="autofix.vehicle", inverse_name="customer_id", string="Vehicles")