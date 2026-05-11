berat = float(input("Masukkan Berat badan (kg) :"))
tinggi = float(input("Masukkan Tinggi badan (m) :"))
bmi = berat / (tinggi**2)
print("BMI kamu adalah", bmi)

if bmi < 18.5:
    category = "Kurus"
elif 18.5 <= bmi < 24.9:
    category = "Normal"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesitas"

print("Kamu termasuk kategory:", category)

