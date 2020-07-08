from odoo import models, fields, api
from odoo.tools.translate import _

class counter_cashbox(models.Model):
    _name = 'exchangecounter.cashbox'
    _description = "MLCC Counter Cashbox"

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



    name = fields.Char(
        string=_("Name"),
        required=True,
        translate=False,
        readonly=False
    )
    #salesteams_id = fields.Many2one(
    #     string=_("Groupe local"),
    #     required=False,
    #     translate=False,
    #     readonly=False
    # )
    company_id = fields.Many2one(
        string=_("Organisation"),
        required=False,
        translate=False,
        readonly=False
    )
    cashbox_type_id = fields.Many2one(
        'exchangecounter.cashboxtype.name',
        string=_("Type de caisse"),
        required=False,
        translate=False,
        readonly=False
    )    
    cashbox_referent_id = fields.Many2one(
        'partner.name',
        string=_("Cashbox référent"),
        required=False,
        translate=False,
        readonly=False
    )
    cashbox_contact_id = fields.Many2one(
        string=_("Responsable de caisse"),
        required=False,
        translate=False,
        readonly=False
    )
    cashbox_code = fields.Char(
        string=_("Code caisse"),
        required=False,
        translate=False,
        readonly=False
    )
    


    #Currencies
    national_currency_id = fields.Many2one(
        string=_("Devise nationale"),
        required=False,
        translate=False,
        readonly=False
    )
    local_currency_id = fields.Many2one(
        string=_("Devise locale"),
        required=False,
        translate=False,
        readonly=False
    )
    
    display_name = fields.Char(
        string=_("Display Name"),
        required=False,
        translate=False,
        readonly=True
    )
    

    # Coupons
    local_currency_cash_journal_id = fields.Many2one(
        string=_("Compte caisse en monnaie locale"),
        required=False,
        translate=False,
        readonly=False
    )
    local_currency_cash_out_journal_id = fields.Many2one(
        string=_("Compte caisse destinataire en monnaie locale"),
        required=False,
        translate=False,
        readonly=False
    )
    
    # National money
    national_currency_cash_journal_id = fields.Many2one(
        string=_("Compte caisse monnaie nationale"),
        required=False,
        translate=False,
        readonly=False
    )
    national_currency_cash_out_journal_id = fields.Many2one(
        string=_("Compte caisse destination monnaie nationale"),
        required=False,
        translate=False,
        readonly=False
    )

    #Checkout
    national_currency_check_journal_id = fields.Many2one(
        string=_("Compte chèque en monnaie nationale"),
        required=False,
        translate=False,
        readonly=False
    )
    national_currency_check_out_journal_id = fields.Many2one(
        string=_("Compte chèque destinataire en monnaie nationale"),
        required=False,
        translate=False,
        readonly=False
    )

    
