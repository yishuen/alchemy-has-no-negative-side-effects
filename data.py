import requests
from models import Strain, Flavor, StrainFlavor, Effect, StrainEffects

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

def pos_effects():
    pos_effects = []
    for strain in data:
        pos_effects += strain[1]['effects']['positive']
    return list(set(pos_effects))

def neg_effects():
    neg_effects = []
    for strain in data:
        neg_effects += strain[1]['effects']['negative']
    return list(set(neg_effects))

def med_effects():
    med_effects = []
    for strain in data:
        med_effects += strain[1]['effects']['medical']
    return list(set(med_effects))

def instantiate_effects():
    effect_instances = []
    for effect in pos_effects():
        eff = Effect(name=effect, type='Positive', strains=[])
        effect_instances.append(eff)
    for effect in neg_effects():
        eff = Effect(name=effect, type='Negative', strains=[])
        effect_instances.append(eff)
    for effect in med_effects():
        eff = Effect(name=effect, type='Medical', strains=[])
        effect_instances.append(eff)
    return effect_instances

effect_instances = instantiate_effects()

def instantiate_strains():
    strain_instances = []
    for strain in data:
        s = Strain(name=strain[0], \
            race=strain[1]['race'], \
            flavors=list(filter(lambda f: f.name in strain[1]['flavors'], \
                flavor_instances)), \
            effects = list(filter(lambda e: e.name in strain[1]['effects']['positive'] or \
                                            e.name in strain[1]['effects']['negative'] or \
                                            e.name in strain[1]['effects']['medical'], effect_instances)))
        strain_instances.append(s)
    return strain_instances

strain_instances = instantiate_strains()

session.add_all(strain_instances)
session.add_all(flavor_instances)
session.commit()





# "Afpak":    {"id":1 ,
#             "race":"hybrid",
#             "flavors":["Earthy","Chemical","Pine"],
#             "effects":  {"positive":["Relaxed","Hungry","Happy","Sleepy"],
#                         "negative":["Dizzy"],
#                         "medical":["Depression","Insomnia","Pain","Stress","Lack of Appetite"]}}
