def get_input():
    value = float(input("Enter the value to convert: "))
    unit = input("Enter the unit (e.g., km, mi, kg, lb): ").lower()
    return value, unit

def check_unit_type(unit):
    length_units = ['km', 'm', 'cm', 'mm', 'mi', 'yd', 'ft', 'in']
    mass_units = ['kg', 'g', 'mg', 'lb', 'oz']
    
    if unit in length_units:
        return "length"
    elif unit in mass_units:
        return "mass"
    else:
        return "unknown"

def convert_value(value, from_unit, to_unit):
    # Conversion factors
    length_factors = {
        'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001,
        'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254
    }
    mass_factors = {
        'kg': 1000, 'g': 1, 'mg': 0.001,
        'lb': 453.592, 'oz': 28.3495
    }
    
    if from_unit in length_factors and to_unit in length_factors:
        return value * length_factors[from_unit] / length_factors[to_unit]
    elif from_unit in mass_factors and to_unit in mass_factors:
        return value * mass_factors[from_unit] / mass_factors[to_unit]
    else:
        return None

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        value, from_unit = get_input()
        unit_type = check_unit_type(from_unit)
        
        if unit_type == "unknown":
            print("Unknown unit type. Please try again.")
            continue
        
        print(f"Converting {unit_type}...")
        
        to_unit = input(f"Enter the unit to convert to ({unit_type}): ").lower()
        if check_unit_type(to_unit) != unit_type:
            print("Incompatible unit types. Please try again.")
            continue
        
        result = convert_value(value, from_unit, to_unit)
        
        if result is not None:
            print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
        else:
            print("Conversion failed. Please check your units and try again.")
        
        if input("Do you want to perform another conversion? (y/n): ").lower() != 'y':
            break
    
    print("Thank you for using the Unit Converter!")

if __name__ == "__main__":
    main()
