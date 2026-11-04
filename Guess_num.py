import random
while True:
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    win = False
    print("\nبازی حدس اعداد")
    print("من یک عدد بین 1 تا 100 انتخاب کردم.")
    print("شما 5 فرصت برای حدس زدن دارید.")
    while attempts < max_attempts:
        print("\nتلاش", attempts + 1, "از 5")
        print("جان باقی مانده:", max_attempts - attempts)
        try:
            guess = int(input("عدد مورد نظر را وارد کنید: "))
            if guess < 1 or guess > 100:
                print("خطا! عدد باید بین 1 تا 100 باشد.")
                continue
        except ValueError:
            print("خطا! لطفاً فقط عدد وارد کنید.")
            continue
        attempts += 1
        if guess == number:
            print("\nآفرین! شما برنده شدید.")
            win = True
            if attempts == 1:
                print("رتبه شما: نمونه ای")
            elif attempts == 2:
                print("رتبه شما: بسیار خوب")
            elif attempts == 3:
                print("رتبه شما: خوب")
            elif attempts == 4:
                print("رتبه شما: قبول")
            elif attempts == 5:
                print("رتبه شما: با شانس بردی!")
            break
        elif guess > number:
            print("عدد کوچک تری وارد کن.")
        else:
            print("عدد بزرگ تری وارد کن.")
        difference = abs(guess - number)
        if difference <= 5:
            print("خیلی نزدیکی!")
        elif difference <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")
    if win == False:
        print("\nمتأسفانه فرصت های شما تمام شد!")
        print("شما باختید.")
        print("عدد مخفی برابر بود با:", number)
    again = input("\nآیا می خواهید دوباره بازی کنید؟ (بله/خیر): ")
    if again == "بله" or again == "آره" or again == "اره" or again == "yes":
        print("بازی جدید شروع می شود!")
    else:
        print("ممنون از بازی شما! خداحافظ.")
        break
