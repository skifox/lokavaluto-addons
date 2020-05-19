from odoo import models, fields, api
from odoo.tools.translate import _

class counter_transaction(models.Model):
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
        readonly=True,
    )

    TRANSACTIONTYPE = [
        ('coupons', 'Coupons'),
        ('national_money', 'National Money'),
        ('deposit', 'Deposit')
    ]
    transaction_type = fields.Selection(
        TRANSACTIONTYPE,
        required= True,
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

    ################################################
    # fields for the coupons
    ################################################
    coupons_location_orig_id=fields.Many2one(
        'stock.location',
        string='Origine stock',
        required=False,
        ondelete='set null',
        readonly=True
    )
    coupons_location_dest_id=fields.Many2one(
        'stock.location',
        string='Destination stock',
        required=False,
        ondelete='set null',
        readonly=True
    )
    coupons_quantity=fields.Integer(
        string="Quantity of coupons",
        required=False
    )
    coupons_list=fields.Many2one(
        'product.product',
        string='List of coupons',
        ondelete='set null',
    )

    ################################################
    # fields for the national currency transactions
    ################################################
    national_currency_journal_orig_id=fields.Many2one(
        'account.journal',
        string='Origine stock',
        required=False,
        ondelete='set null',
        readonly=True
    )
    national_currency_journal_dest_id=fields.Many2one(
        'account.journal',
        string='Destination stock',
        required=False,
        ondelete='set null',
        readonly=True
    )

    ################################################
    # fields for the deposits
    ################################################
    deposit_journal_orig_id=fields.Many2one(
        'account.journal',
        string='Origine stock',
        required=False,
        ondelete='set null',
        readonly=True
    )
    deposit_journal_dest_id=fields.Many2one(
        'account.journal',
        string='Destination stock',
        required=False,
        ondelete='set null',
        readonly=True
    )