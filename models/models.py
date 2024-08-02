from odoo import models, fields, api

class AcademyStudent(models.Model):
    _name = 'academy.student'
    _description = 'Academy Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    teacher_id = fields.Many2one('academy.teacher', string='Teacher')

    def print_report(self):
        return self.env.ref('academy.action_print_student').report_action(self)

    def action_save_student(self):
        self.ensure_one()
        self.write({'name': self.name}) 
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }


class AcademyTeacher(models.Model):
    _name = 'academy.teacher'
    _description = 'Academy Teacher'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    department = fields.Char(string='Department')
    student_ids = fields.One2many('academy.student', 'teacher_id', string='Students')
