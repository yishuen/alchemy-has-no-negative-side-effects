from models import Strain, Flavor, Effect, Country, StrainFlavor, StrainEffects, StrainCountry
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, relationship
from collections import Counter
engine = create_engine('sqlite:///weed.db')
Session = sessionmaker(bind=engine)
session = Session()

# CHANGE QUERIES from session.query(Listing).all() to Listing.query.all()/filter_by()

def races():
    objs = session.query(Strain).all()
    races = list(map(lambda o: o.race, objs))
    return list(set(races))

def strain_names_by_race(race):
    objs = session.query(Strain).filter(Strain.race == race).all()
    names = list(map(lambda o: o.name, objs))
    return names

def count_by_race():
    race_counts = list(map(lambda r: (r, len(strain_names_by_race(r))), races()))
    return {'x': list(map(lambda c: c[0], race_counts)), 'y': list(map(lambda c: c[1], race_counts))}

def flavors():
    objs = session.query(Strain).all()
    flavors = []
    for o in objs:
        for flavor in o.flavors:
            flavors.append(flavor.name)
    return list(set(flavors))

def strain_names_by_flavor(flavor):
    objs = session.query(Flavor).filter(Flavor.name == flavor).first().strains
    names = list(map(lambda o: o.name, objs))
    return names

def count_by_flavor():
    flavor_counts = list(map(lambda f: (f, len(strain_names_by_flavor(f))), flavors()))
    return {'x': list(map(lambda f: f[0], flavor_counts)), 'y': list(map(lambda f: f[1], flavor_counts))}

def effects():
    objs = session.query(Strain).all()
    effects = []
    for o in objs:
        for effect in o.effects:
            effects.append(effect.name)
    return list(set(effects))

def strain_names_by_effect(effect):
    objs = session.query(Effect).filter(Effect.name == effect).first().strains
    names = list(map(lambda o: o.name, objs))
    return names

def count_by_effect():
    effect_counts = list(map(lambda e: (e, len(strain_names_by_effect(e))), effects()))
    return {'x': list(map(lambda f: f[0], effect_counts)), 'y': list(map(lambda f: f[1], effect_counts))}

def countries():
    objs = session.query(Strain).all()
    countries = []
    for o in objs:
        for country in o.countries:
            countries.append(country.name)
    return list(set(countries))

def strains_by_country(country):
    return session.query(Country).filter(Country.name == country).first().strains

def race_count_by_country(country):
    strains = strains_by_country(country)
    race_counts = list(Counter(list(map(lambda s: s.race, strains))).items())
    return {'x': list(map(lambda f: f[0], race_counts)), 'y': list(map(lambda f: f[1], race_counts))}

def country_race_composition():
    country_list = []
    sativas = []
    indicas = []
    hybrids = []
    for country in countries():
        country_list.append(country)
        race = race_count_by_country(country)['x']
        count = race_count_by_country(country)['y']
        race_dict = dict(zip(race, count))
        if 'sativa' in race_dict.keys():
            sativas.append(race_dict['sativa'])
        if 'indica' in race_dict.keys():
            indicas.append(race_dict['indica'])
        if 'hybrid' in race_dict.keys():
            hybrids.append(race_dict['hybrid'])
    return {'countries': country_list, 'sativas': sativas, 'indicas': indicas, 'hybrids': hybrids}



def effect_count_by_country(country):
    strains = strains_by_country(country)
    effects = []
    for strain in strains:
        straineffects = strain.effects
        for effect in straineffects:
            effects.append(effect.name)
    effect_counts = list(dict(Counter(effects)).items())
    return {'x': list(map(lambda f: f[0], effect_counts)), 'y': list(map(lambda f: f[1], effect_counts))}


def flavor_count_by_country(country):
    strains = strains_by_country(country)
    flavors = []
    for strain in strains:
        strainflavors = strain.flavors
        for flavor in strainflavors:
            flavors.append(flavor.name)
    flavor_counts = list(dict(Counter(flavors)).items())
    return {'x': list(map(lambda f: f[0], flavor_counts)), 'y': list(map(lambda f: f[1], flavor_counts))}


def strain_names_by_country(country):
    objs = session.query(Country).filter(Country.name == country).first().strains
    names = list(map(lambda o: o.name, objs))
    return names

def count_by_country():
    return list(map(lambda c: (c, len(strain_names_by_country(c))), countries()))
