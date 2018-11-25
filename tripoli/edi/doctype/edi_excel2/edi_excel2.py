# -*- coding: utf-8 -*-
# Copyright (c) 2018, Zaqout and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class EDIExcel2(Document):
	pass

def on_submit():
	if (self.shipper_cus == " ") and (self.consignee_cus == " ") and (self.notify_cus == " "):
		frappe.msgprint("select value shipper , consignee , notify")


