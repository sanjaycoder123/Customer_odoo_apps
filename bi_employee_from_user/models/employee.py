from odoo import api,fields, models

class CreateEmployee(models.Model):
    _inherit = 'res.users'

    is_employee = fields.Boolean('Is Employee',copy=False)
    position_id = fields.Many2one('hr.job',string='job Position')

    @api.model_create_multi
    def create(self, vals):
        res = super(CreateEmployee, self).create(vals)
        if res.is_employee == True:
            if len(res.ids) > 0:
                for id in res.ids:
                    load_user = self.env['res.users'].sudo().browse(id)
                    vals_emp = {
                        'company_id': self.env.user.company_id.id or False,
                        'active': True,
                        'job_id' : load_user.position_id.id,
                        'name': load_user.name,
                        'resource_calendar_id': 1,
                        'address_id': False,
                        'category_ids': [[6, False, []]],
                        'work_email': load_user.email,
                        'user_id': id,
                        'image': load_user.image
                    }
                    self.env['hr.employee'].create(vals_emp)

        return res

    @api.multi
    def write(self, vals):
        res = super(CreateEmployee, self).write(vals)
        if self.is_employee == True:
            emp_id = self.env['hr.employee'].search([('name', '=', self.name),('active','=',True)])
            if not emp_id:
                self.env['hr.employee'].create({
                    'active': True,
                    'name': self.name,
                    'image': self.image,
                    'job_id' : self.position_id.id,
                })
            else :

                emp_id.write({
                    'active': True,
                    'name': self.name,
                    'image': self.image,
                    'job_id': self.position_id.id,
                })

        elif self.is_employee == False:
            emp_id = self.env['hr.employee'].search([('name', '=', self.name)])
            if emp_id:
                for res in emp_id:
                    res.resource_id.write({
                        'active': False
                    })

        return res



