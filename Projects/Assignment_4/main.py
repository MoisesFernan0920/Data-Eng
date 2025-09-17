def calculate_bulking_macros(weight_lbs=205, activity_level=16, surplus_percent=0.08):
    """
    Calculate calories and macros for a bulking phase.
    
    Parameters:
    - weight_lbs (float): Body weight in pounds
    - activity_level (int): 14 (low), 16 (moderate), 18 (very active)
    - surplus_percent (float): Caloric surplus (e.g., 0.08 for 8%)

    Returns:
    - dict with TDEE, surplus calories, total calories, and macro breakdown
    """
    
    # Calculate TDEE (Total Daily Energy Expenditure)
    tdee = weight_lbs * activity_level
    surplus = tdee * surplus_percent
    total_calories = tdee + surplus

    # Protein: 0.75 to 1.0g per lb
    protein_per_lb = 0.9  # middle ground
    protein_grams = weight_lbs * protein_per_lb
    protein_cals = protein_grams * 4

    # Fats: 20% to 30% of total calories
    fat_ratio = 0.25  # middle ground
    fat_cals = total_calories * fat_ratio
    fat_grams = fat_cals / 9

    # Carbs: Remaining calories
    carb_cals = total_calories - (protein_cals + fat_cals)
    carb_grams = carb_cals / 4

    return {
        'Weight (lbs)': weight_lbs,
        'TDEE': round(tdee),
        'Surplus Calories': round(surplus),
        'Total Calories (Bulking)': round(total_calories),
        'Protein (g)': round(protein_grams),
        'Fats (g)': round(fat_grams),
        'Carbs (g)': round(carb_grams)
    }


# Example usage
macros = calculate_bulking_macros()
for k, v in macros.items():
    print(f"{k}: {v}")
