from odoo import models, fields, api

class Vehicle(models.Model):
    _name="autofix.vehicle"
    _description="Vehicle information"
    
    brand = fields.Char(string="Brand")
    color = fields.Char(string="Color")
    mileage = fields.Integer(string="Kilometer")
    model = fields.Char(string="Model")
    plate = fields.Char(string="Plate")
    state = fields.Boolean(string="State", default=True)
    year = fields.Integer(string="Year")
    fuel_type = fields.Selection(string="Fuel type",  selection=[
    ('gasoline', 'Gasoline'),
    ('diesel','Diesel'),
    ('hybrid','Hybrid'),
    ('electric','Electric')
    ])
    vin = fields.Char(string="Vin") 
    doors = fields.Integer(string="Doors")
    notes = fields.Text(string="Notes")
    customer_id = fields.Many2one(comodel_name="autofix.customer", string="Customer")