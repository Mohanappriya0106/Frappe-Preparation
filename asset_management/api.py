import frappe

@frappe.whitelist()
def api_practice():
    customer=frappe.qb.DocType("Customer")
    address=frappe.qb.DocType("Customer Address")

    query=frappe.qb.from_(customer).join(address).on(customer.name == address.customer_id).where(customer.status== "InActive").select(customer.customer_name)

    result=query.run(as_dict = True)

    for row in result:
        frappe.db.set_value("Customer", row.name, "status", "Active")

    return result
