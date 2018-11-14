from dash_package.models import Strain, Flavor, Effect, Country, StrainFlavor, StrainEffects, StrainCountry
from dash_package.queries import races, strain_names_by_race, count_by_race, flavors, strain_names_by_flavor, count_by_flavor, effects, strain_names_by_effect, count_by_effect, countries, strains_by_country, race_count_by_country, effect_count_by_country, flavor_count_by_country, strain_names_by_country, count_by_country, country_race_composition

country_race_composition = country_race_composition()
