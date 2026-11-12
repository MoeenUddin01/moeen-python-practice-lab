
from models.invoice import Invoice
class InvoiceService:
    def __init__(self):
        
        self.invoice=[]
        print (self.invoice)

    def create_invoice(invoice2,invoice_id,vender,amount,tax_rate):
       invoice1= Invoice(invoice_id,vender,amount,tax_rate)
       invoice2.append(invoice1)
       return invoice2.append(invoice1)



if __name__=="__main__":
    print("Testing the invoice")
    inv1=InvoiceService()
    inv1.create_invoice(1123,"HBK",2000,0.05)
    print(inv1)