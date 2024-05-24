#11.1 11.2
from city_functions import city_country_3
def test_city_population_function():
    """能够正确存储城市名和国家名吗？"""
    formatted_city_country_name=city_country_3('santiago','chile')
    assert formatted_city_country_name=='Santiago,Chile'