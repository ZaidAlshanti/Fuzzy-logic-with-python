def get_fuzzy_values(x, y, z):
    def near(val):
        if val <= 0.25:
            return 1
        elif val > 0.25 and val < 0.75:
            return -2 * val + 1.5
        else:
            return 0

    def far(val):
        if val > 0.75:
            return 1
        elif val > 0.25 and val <= 0.75:
            return 2 * val - 0.5
        else:
            return 0

    left = 1 if near(x) >= far(x) else 0
    centre = 1 if near(y) >= far(y) else 0
    right = 1 if near(z) >= far(z) else 0

    print(f"Fuzzy values -> Left: {left}, Centre: {centre}, Right: {right}")

    return left, centre, right


def get_speed_and_rotation(left, centre, right):
        if (left == 1) and (centre == 1) and (right == 1):
            return 'Slow', 'TRB'
        elif (left == 1) and (centre == 1) and (right == 0):
            return 'Medium', 'TRS'
        elif (left == 1) and (centre == 0) and (right == 1):
            return 'Slow', 'TZ'
        elif (left == 1) and (centre == 0) and (right == 0):
            return 'Fast', 'TRS'
        elif (left == 0) and (centre == 1) and (right == 1):
            return 'Medium', 'TLS'
        elif (left == 0) and (centre == 1) and (right == 0):
            return 'Slow', 'TRB'
        elif (left == 0) and (centre == 0) and (right == 1):
            return 'Fast', 'TLS'
        elif (left == 0) and (centre == 0) and (right == 0):
            return 'Fast', 'TZ'
        return "No matching rule"



x=float(input("Enter left distance : "))
y=float(input("Enter centre distance : "))
z=float(input("Enter right distance : "))
left, centre, right = get_fuzzy_values(x,y,z)
result = get_speed_and_rotation(left, centre, right)
print(result)
