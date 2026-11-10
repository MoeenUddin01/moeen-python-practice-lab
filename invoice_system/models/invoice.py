
class Invoice:
    def __init__(self,invoic_id,vender,amount,tax_rate):
        self.invoice_id=invoic_id
        self.vender=vender
        self.amount=amount
        self.tax_rate=tax_rate
        self.status="Unpaid"

    def calculate_tax(self):
        tax=self.amount*self.tax_rate
        return tax

    def calculate_total(self):
        tax=self.calculate_tax()
        total=tax+self.amount
        return total

    

    def make_as_paid(self):
        self.status ="Paid"
        return self.status

        

    def get_invoice_details(self):
        tax_cal=self.calculate_tax()
        total=self.calculate_total()
        paid=self.status
        details={
            "TAX":tax_cal,
            "TOTAL":total,
            "PAID_STATUS":paid
        }
        return details

if __name__=="__main__":
    ivo=Invoice("INV-001","Acme CORP",1000,0.05)
    print("Initial Invoice Details ")
    print(ivo.get_invoice_details())

    print(f"calculating text {ivo.calculate_tax()}")

    print(f"Calculating total {ivo.calculate_total()}")
    print(f"status {ivo.make_as_paid()}")
