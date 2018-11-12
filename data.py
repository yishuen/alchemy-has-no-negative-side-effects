import requests
from models import Strain, Flavor, StrainFlavor #, Effect, StrainEffects

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///weed.db')

Session = sessionmaker(bind=engine)
session = Session()

url = 'http://strainapi.evanbusse.com/80Bxz5h/strains/search/all'

data = list(dict(requests.get(url).json()).items())

strain_names = list(requests.get(url).json())

def flavors():
    flavors = []
    for strain in data:
        flavors += strain[1]['flavors']
    return(list(set(flavors)))

def instantiate_flavors():
    flavor_instances = []
    for flavor in flavors():
        flav = Flavor(name=flavor, strains=[])
        flavor_instances.append(flav)
    return flavor_instances

flavor_instances = instantiate_flavors()

def instantiate_strains():
    strain_instances = []
    for strain in data:
        s = Strain(name=strain[0], \
            race=strain[1]['race'], \
            flavors=list(filter(lambda f: f.name in strain[1]['flavors'], \
                flavor_instances)))
        strain_instances.append(s)
    return strain_instances

# def add_flavors():
#     for strain in data:
#         flav_objs = instantiate_flavors()
#         flavors = list(filter(lambda f: f.name in strain[1]['flavors'], flav_objs))
#         pick = list(filter(lambda n: n.name == strain[0], instantiate_strains()))[0]
#         pick.flavors.append(flavors)
#
# add_flavors()



x = instantiate_strains()

session.add_all(x)
session.add_all(flavor_instances)
session.commit()
#
# def print_strains():
#     for i in session.query(Strain).all():
#         print(i.name)
#
# def print_flavors():
#     for i in session.query(Flavor).all():
#         print(i.name)
#
# def pos_effects():
#     pos_effects = []
#     for name in strain_names:
#         pos_effects += data[name]['effects']['positive']
#     return list(set(pos_effects))
#
# def neg_effects():
#     neg_effects = []
#     for name in strain_names:
#         neg_effects += data[name]['effects']['negative']
#     return list(set(neg_effects))
#
# def med_effects():
#     med_effects = []
#     for name in strain_names:
#         med_effects += data[name]['effects']['medical']
#     return list(set(med_effects))


# "Afpak":    {"id":1 ,
#             "race":"hybrid",
#             "flavors":["Earthy","Chemical","Pine"],
#             "effects":  {"positive":["Relaxed","Hungry","Happy","Sleepy"],
#                         "negative":["Dizzy"],
#                         "medical":["Depression","Insomnia","Pain","Stress","Lack of Appetite"]}}
