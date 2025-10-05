zander_length = float(input("Enter the zander length: "))
limit = 42

if zander_length < limit:
    difference = limit - zander_length
    print(f"Please release the zander")
    print(f"This fish shorter {difference:.1f} to the limit")
else:
    print("You can keep the fish")

cabin_class = input("Enter the cabin class: ")
if cabin_class == "Lux":
    print("the cabin is upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("the cabin is above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("the cabin is windowless cabin above the car deck.")
elif cabin_class == "C":
    print("the cabin is windowless cabin below the car deck")
else:
    print("invalid cabin class")

sex = input("enter your sex:")
hemoglobin_value = float(input("Enter the hemoglobin value: "))
if sex == "Female":
    if hemoglobin_value < 117:
        print("hemoglobin is low")
    if hemoglobin_value > 155:
        print("hemoglobin is high")
    else:
        print("hemoglobin is normal")
if sex == "Male":
    if hemoglobin_value < 134:
        print("hemoglobin is normal")
    if hemoglobin_value > 167:
        print("hemoglobin is high")
    else:
        print("hemoglobin is normal")

year = input("Enter the year: ")
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year.")


