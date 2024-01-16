def greet
  puts "Hello Rachel. You are very pretty today."
end

class GasStation
  def initialize(name = "Station")
    @name = name
  end

  def input_price(price = 000)
    @price = price
  end


#app will get price, ask for currency, and then display the price in both currencies and per-units
#app will specify and convert gallons to liters and visa-versa, assuming liters for CAN and gallons for USD
