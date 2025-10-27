import calendar

if __name__ == "__main__":
    user_in = input("Enter month (1-12 or name, e.g., 'Mar' or 'March'): ").strip()
    month_num = None

    if user_in.isdigit():
        m = int(user_in)
        if 1 <= m <= 12:
            month_num = m
    else:
        low = user_in.lower()
        for i in range(1, 13):
            if low == calendar.month_name[i].lower() or low == calendar.month_abbr[i].lower():
                month_num = i
                break

    if month_num is None:
        print("Invalid month input.")
    else:
        if month_num in (12, 1, 2):
            season = "Winter"
        elif month_num in (3, 4, 5):
            season = "Spring"
        elif month_num in (6, 7, 8):
            season = "Summer"
        else:
            season = "Autumn"
        print(f"Month: {calendar.month_name[month_num]} -> Season: {season}")