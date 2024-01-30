def convert_gas_price(cad_price):
    # Exchange rate
    cad_to_usd_rate = 0.75
    
    # Conversion from CAD to USD
    usd_price = cad_price * cad_to_usd_rate
    
    # Conversion from liters to gallons (1 liter ≈ 0.264172 gallons)
    liters_to_gallons = 0.264172
    usd_price_per_gallon = usd_price / liters_to_gallons
    
    return usd_price_per_gallon

# Example usage:
canadian_gas_price_cad = 1.65  # Example Canadian gas price in CAD
american_gas_price_usd_per_gallon = convert_gas_price(canadian_gas_price_cad)
print(f"Equivalent American gas price: ${american_gas_price_usd_per_gallon:.2f} USD per gallon")
