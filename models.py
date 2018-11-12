from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
Base = declarative_base()

class Strain(Base):
    __tablename__ = 'strains'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    race = Column(Text)
    flavors = relationship('Flavor', secondary='strainflavors', back_populates='strains')
    # effect_ids = Column(Integer, ForeignKey('effects.id'))
    # effects = relationship('Effect', secondary = 'straineffects', back_populates = 'strain')

class Flavor(Base):
    __tablename__ = 'flavors'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    strains = relationship('Strain', secondary='strainflavors', back_populates = 'flavors')

class StrainFlavor(Base):
    __tablename__ = 'strainflavors'
    strain_id = Column(Integer, ForeignKey('strains.id'), primary_key=True)
    flavor_id = Column(Integer, ForeignKey('flavors.id'), primary_key=True)

# class Effect(Base):
#     __tablename__ = 'effects'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     type = Column(Text)
#     strain_ids = Column(Integer, ForeignKey('strains.id'))
#     strains = relationship('Strain', secondary = 'straineffects', back_populates = 'effects')




# class StrainEffects(Base):
#     __tablename__ = 'straineffects'
#     id = Column(Integer, primary_key=True)
#     strain_id = Column(Integer, ForeignKey('strains.id'))
#     effect_id = Column(Integer, ForeignKey('effects.id'))


engine = create_engine('sqlite:///weed.db')
Base.metadata.create_all(engine)
