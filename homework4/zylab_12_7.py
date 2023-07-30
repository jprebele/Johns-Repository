# John Rebeles
# PSID: 2039426

def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    # TODO: Raise exception for invalid ages
    return age


# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = .7 * (220 - age)
    return heart_rate


if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        u_age = get_age()
        h_rate = fat_burning_heart_rate(u_age)
        print(f"Fat burning heart rate for a {u_age} year-old: {h_rate:.1f} bpm")
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate heart rate info.\n")
