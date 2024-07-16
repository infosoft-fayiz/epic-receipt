from odoo import models, fields

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        result = super(PosSession, self)._loader_params_res_partner()
        result['search_params']['fields'].append('credit_limit')
        result['search_params']['fields'].append('credit')
        return result 
