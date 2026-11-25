from odoo import model, fields

class Services(model.Models):
    _name="Services"
    _description="Workshop Services"
    
    name=fields.Char(string="Name", required=True)
    description=fields.Text(strin="Description")
    prince=fields.Float(string="Price")
    vehicle_ids=fields.Many2Many(comodel_name="autofix.vehicle", string="Compatible Vehicles")
    