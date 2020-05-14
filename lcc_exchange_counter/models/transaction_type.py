from odoo import models, fields, api
from odoo.tools.translate import _

class transaction_type(models.Model):
    _name = 'exchangecounter.transactiontype'
    _description = "MLCC Transaction Type"

    name = fields.Char(
        string=_("Name"),
        required=False,
        translate=False,
        readonly=False
    )