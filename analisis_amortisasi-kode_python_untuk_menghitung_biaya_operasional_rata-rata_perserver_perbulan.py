# jumlah server
n = 10
# biaya operasional per server per tahun
maintenance_cost = 2000000
software_update_cost = 1500000
system_upgrade_cost = 3000000
# waktu operasi server dalam tahun
t = 5
# biaya amortisasi per server per bulan
amortization_cost = ((maintenance_cost + software_update_cost + system_upgrade_cost) / t) / 12
# biaya operasional rata-rata per server per bulan
average_monthly_cost = amortization_cost / n
print("Biaya operasional rata-rata per server per bulan: Rp", round(average_monthly_cost, 2))
