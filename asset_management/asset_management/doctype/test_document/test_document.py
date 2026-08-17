# Copyright (c) 2026, Employees report issues. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TestDocument(Document):
    def before_save(self):
        print("1111111111111111111111111111111111111111111111111111111111111111111")
        if not self.description:
            self.description = "Default description"
            print("000000000000000000000000000000000000000000000000000000000000000000000")
