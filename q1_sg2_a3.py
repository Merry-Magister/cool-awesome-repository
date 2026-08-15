# info = ["Cai-Li Avrencel V. Bragais", "9 - Samat", "19", "code finished at 8/15/2026"]


zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

good_year = False
while good_year == False:
    year = int(input("Please enter your year of birth: "))
    if year >= 1900:
        good_year = True
    else:
        print ("Please try again, your birthyear should not be earlier than 1900.")

if year == 1900 or (year - 1900) % 12 == 0:
    print (f"Your Chinese Zodiac Sign is: {zodiac[0]}")
    quit()
    

for n in range(1, 12):
    if ((year - 1900) - n) % 12 == 0:
        print(f"Your Chinese Zodiac Sign is: The {zodiac[n]}.")
        quit()