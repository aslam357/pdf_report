from odoo import api, models, fields


class Studentupdatewizard(models.TransientModel):
    _name="student.fees.update.wizard"
    total_fees=fields.Float(string="fees")


    def student_fees_update(self):
        print("succes.....")
        return True