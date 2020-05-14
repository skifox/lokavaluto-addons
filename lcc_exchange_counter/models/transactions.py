from odoo import models, fields, api
from odoo.tools.translate import _

class Transaction(models.Model):
    _name = 'exchangecounter.transaction'
    _description = "MLCC Transaction"

    id = fields.Integer(
        string=_("ID"),
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
    create_uid = fields.Many2one(
        string=_("Created by"),
        required=False,
        translate=False,
        readonly=True
    )
    write_date = fields.Datetime(
        string=_("Last Updated on"),
        required=False,
        translate=False,
        readonly=True
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



    transaction_date = fields.Datetime(
        string="Transaction Date",
        required= True,

    )
    transaction_amount = fields.Float( 
        string='Amount',
        required=True
    )
    
    STATES = [
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('received', 'Received')
    ]    
    status = fields.Selection(
        STATES,
        default=STATES[0][0]
    )


class Coupons(models.Model):
    _name = 'exchangecounter.coupons'
    _description = "MLCC Coupons"
    _inherit = 'exchangecounter.transaction'

    location_orig_id=fields.Many2one(
        'stock.location',
        string='Origine stock',
        required=True,
        ondelete='set null',
        readonly=True
    )
    location_dest_id=fields.Many2one(
        'stock.location',
        string='Destination stock',
        required=True,
        ondelete='set null',
        readonly=True
    )
    quantity_coupons=fields.Integer(
        string="Quantity of coupons",
        required=True
    )
    coupons_list=fields.Many2one(
        'product.product',
        string='List of coupons',
        ondelete='set null',
    )




class Money(models.Model):
    _name = 'exchangecounter.money'
    _description = "MLCC Coupon"
    _inherit = 'exchangecounter.transaction'





class Deposit(models.Model):
    _name = 'exchangecounter.deposit'
    _description = "MLCC Coupon"
    _inherit = 'exchangecounter.transaction'