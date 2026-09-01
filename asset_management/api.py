import frappe

@frappe.whitelist()
def api_practice():
    customer=frappe.qb.DocType("Customer")
    address=frappe.qb.DocType("Customer Address")

    query=frappe.qb.from_(customer).join(address).on(customer.name == address.customer_id).where(customer.status== "InActive").select(customer.name,customer.customer_name)

    result=query.run(as_dict = True)

    for row in result:
        frappe.db.set_value("Customer", row.name, "status", "Active")

    return result




@frappe.whitelist()
def get_recent_todos():

    todos=frappe.get_list("To Do",fields=["name", "user"], order_by="creation desc" , limit_page_length=2)

    for todo in todos:
        todo["email"]=frappe.db.get_value("Customer", todo.user , "email")



    timestamp = frappe.utils.now()

    return {
        "timestamp": timestamp,
        "records": todos
    }


@frappe.whitelist()

def func(subject):
    new_doc=frappe.new_doc("Task-API")
    new_doc.subject=subject
    new_doc.save()
    return new_doc.name


# @frappe.whitelist()
# def practice1():
#     todos=frappe.get_list("To Do",fields=["name", "user"], order_by="creation desc" , limit_page_length=2)

#     for todo in todos:
#         todo["email"]=frappe.db.get_value("Customer", todo.user , "email")

#     return todos