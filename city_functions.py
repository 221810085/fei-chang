#11.1
#11.2
def city_country(city,country):
    """城市名和国家名"""
    formatted_city_country=f"{city},{country}"
    return formatted_city_country.title()

def city_country_2(city,country,population):
    """城市名国家名人口"""
    info=f"{city}.title(),{country}.title() -population{population}"
    return info

def city_country_3(city,country,population=''):
    """城市名国家名人口"""
    if population:
        info=f"{city}.title(),{country}.title() -population{population}"
        return info
    else:
        info=f"{city},{country}"
        return info.title()


