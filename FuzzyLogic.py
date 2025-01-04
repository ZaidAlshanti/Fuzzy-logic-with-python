

# Membership functions
def near(dist):
    if dist <= 0.25:
        return 1.0
    elif dist >= 0.75:
        return 0.0
    else:
        return (-2.0 * dist + 1.5)

def far(dist):
    if dist <= 0.25:
        return 0.0
    elif dist >= 0.75:
        return 1.0
    else:
        return (2.0 * dist - 0.5)

# Defuzzify translational speed
def defuzzify_speed(slow, medium, fast):
    return slow * 0.0 + medium * 25.0 + fast * 50.0

# Defuzzify rotational speed
def defuzzify_rotation(tlb, tls, tz, trs, trb):
    return tlb * -50.0 + tls * -25.0 + tz * 0.0 + trs * 25.0 + trb * 50.0

# Min function for fuzzy rule evaluation
def fuzzy_min(values):
    return min(values)


# Example fuzzy logic rules
def fuzzy_logic_single_rule(left_dist, center_dist, right_dist):
    left_near = near(left_dist)
    center_near = near(center_dist)
    right_near = near(right_dist)

    left_far = far(left_dist)
    center_far = far(center_dist)
    right_far = far(right_dist)

    # Initialize rule firings with their strengths
    rules = [
        {"rule": ("TRB", "Slow"), "strength": fuzzy_min([left_near, center_near, right_near])},
        {"rule": ("TRS", "Medium"), "strength": fuzzy_min([left_near, center_near, right_far])},
        {"rule": ("TZ", "Slow"), "strength": fuzzy_min([left_near, center_far, right_near])},
        {"rule": ("TRS", "Fast"), "strength": fuzzy_min([left_near, center_far, right_far])},
        {"rule": ("TLS", "Medium"), "strength": fuzzy_min([left_far, center_near, right_near])},
        {"rule": ("TRB", "Slow"), "strength": fuzzy_min([left_far, center_near, right_far])},
        {"rule": ("TLS", "Fast"), "strength": fuzzy_min([left_far, center_far, right_near])},
        {"rule": ("TZ", "Fast"), "strength": fuzzy_min([left_far, center_far, right_far])},
    ]

    # Find the rule with the highest strength (union operation)
    best_rule = max(rules, key=lambda r: r["strength"])

    # Translational and rotational speeds are derived from the best rule
    translational_speed, rotational_speed = best_rule["rule"]
    return translational_speed, rotational_speed, best_rule
if __name__ == "__main__":
    # Example distances from sensors (in meters)
    left_dist = float(input("Left distance "))
    center_dist = float(input("Center distance "))
    right_dist = float(input("Right distance "))
    print(fuzzy_logic_single_rule(left_dist, center_dist, right_dist))