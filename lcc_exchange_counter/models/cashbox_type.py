from odoo import models, fields
from odoo.tools.translate import _


class cashbox_type(models.Model):
    _name = 'exchangecounter.cashboxtype'
    _description = "MLCC Counter Cashbox Types"
    
    write_date = fields.Datetime(
        string=_("Last Updated on"),
        required=False,
        translate=False,
        readonly=True
    )
    create_date = fields.Datetime(
        string=_("Created on"),
        required=False,
        translate=False,
        readonly=True
    )
    display_name = fields.Char(
        string=_("Display Name"),
        required=False,
        translate=False,
        readonly=True
    )
    id = fields.Integer(
        string=_("ID"),
        required=False,
        translate=False,
        readonly=True
    )
    name = fields.Char(
        string=_("Name"),
        required=False,
        translate=False,
        readonly=False
    )
    write_uid = fields.Many2one(
        string=_("Last Updated by"),
        required=False,
        translate=False,
        readonly=True
    )
    __last_update = fields.Datetime(
        string=_("Last Modified on"),
        required=False,
        translate=False,
        readonly=True
    )
    create_uid = fields.Many2one(
        string=_("Created by"),
        required=False,
        translate=False,
        readonly=True
    )
