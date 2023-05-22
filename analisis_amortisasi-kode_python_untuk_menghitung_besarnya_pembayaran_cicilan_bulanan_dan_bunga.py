# harga mobil
car_price = 200000000
# uang muka
down_payment = 60000000
# sisa pembayaran
balance = car_price - down_payment
# bunga per tahun
interest_rate = 0.10
# biaya administrasi
administrative_fee = 1000000
# waktu kredit dalam tahun
loan_period = 5
# jumlah pembayaran
num_payments = loan_period * 12
# pembayaran per bulan
monthly_interest_rate = interest_rate / 12
monthly_payment = (balance * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
monthly_payment += administrative_fee / num_payments
# total biaya bunga
total_interest = (monthly_payment * num_payments) - balance
print("Besarnya pembayaran cicilan bulanan: Rp", round(monthly_payment, 2))
print("Total biaya bunga: Rp", round(total_interest, 2))
