# Copyright (c) 2026, Employees report issues. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe


class TaskAPI(Document):

	def validate(self):
		if(self.subject):
			length=len(self.subject)
			if(length <1):
				frappe.throw("invalid Subject")
		else:
			frappe.throw("Please Enter the Subject")
