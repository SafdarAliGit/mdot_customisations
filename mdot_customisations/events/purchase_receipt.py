
import frappe

def make_purchase_invoice(doc, method=None):
    from erpnext.stock.doctype.purchase_receipt.purchase_receipt import make_purchase_invoice
    if doc.purchase_invoice_on_submit:
        purchase_invoice = make_purchase_invoice(doc.name)
        purchase_invoice.submit()