from models.invoice import Invoice
class InvoiceService:
    def __init__(self):
        
        self.invoice=[]

    def create_invoice(self,invoice_id,vender,amount,tax_rate):
        self.invoice=Invoice
