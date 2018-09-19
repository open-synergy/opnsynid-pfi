# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class RecruitmentCandidate(models.Model):
    _inherit = ["hr_service.recruitment_candidate"]

    objective = fields.Text(
        string="Objective",
    )
    cover_letter = fields.Text(
        string="Cover Letter",
    )
    last_work = fields.Text(
        string="Last Work",
    )
    last_education = fields.Text(
        string="Last Education",
    )
    years_of_experience = fields.Float(
        string="Years of Experiences"
    )
    expected_job_position_string = fields.Char(
        string="Expected Job Position",
    )
