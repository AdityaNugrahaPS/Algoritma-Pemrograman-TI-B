#MATCH CASE : benefits = cleaner n syntax more readable than using elif statement


def day_of_week(day):
    match day:
        case 1:
            return "it is sunday"
        case 2:
            return "it is monday"
        case 3:
            return "it is tuesday"
        case 4:
            return "it wednesday"
        case 5:
            return "it is thursday"
        case 6:
            return "it is friday"
        case 7:
            return "it is saturday"
        case _:
            return "not a valid day"
        
print(day_of_week(3))

        
