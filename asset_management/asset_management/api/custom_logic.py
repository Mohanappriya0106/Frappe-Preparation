import frappe

def custom_logic(doc, method=None):
    frappe.msgprint("Hook executed!")