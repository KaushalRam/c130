import pandas as pd
import csv

df = pd.read_csv('final.csv')

df['hyperlink']
df['temp_planet_data']
df['temp_planet_mass']
df['pl_letter']
df['pl_name']
df['pl_controflag']
df['pl_pnum']
df['pl_orbper']
df['pl_orbpererr1']
df['pl_orbpererr2']
df['pl_orbperlim']
df['pl_orbsmax']
df['pl_orbsmaxerr1']
df['pl_orbsmaxerr2']
df['pl_orbsmaxlim']
df['pl_orbeccen']
df['pl_orbeccenerr1']
df['pl_orbeccenerr2']
df['pl_orbeccenlim']
df['pl_orbinclerr1']
df['pl_orbinclerr2']
df['pl_bmassj']
df['pl_bmassjerr1']
df['pl_bmassjerr2']
df['pl_bmassjlim']
df['pl_bmassprov']
df['pl_radj']
df['pl_radjerr1']
df['pl_radjerr2']
df['pl_radjlim']
df['pl_denserr1']
df['pl_denserr2']
df['pl_denslim']
df['pl_ttvflag']
df['pl_kepflag']
df['pl_k2flag']
df['pl_nnotes']
df['ra']
df['des']
df['st_dist']
df['st_disterr1']
df['st_disterr2']
df['st_distlim']
df['gaia_dist']
df['gaia_disterr1']
df['gaia_disterr2']
df['gaia_distlim']
df['st_optmag']
df['st_optmagerr']
df['st_optmaglim']
df['st_optband']
df['gaia_gmag']
df['gaia_gmagerr']
df['gaia_gmaglim']
df['st_tefferr1']
df['st_tefferr2']
df['st_tefflim']
df['st_masserr1']
df['st_masserr2']
df['st_masslim']
df['st_raderr1']
df['st_raderr2']
df['st_radlim']
df['rowupdate']
df['pl_facility']

df = df.rename({ 'pl_hostname': "solar_system_name", 
                'pl_discmethod': "planet_discovery_method", 
                'pl_orbincl': "planet_orbital_inclination", 
                'pl_dens': "planet_density", 
                'ra_str': "right_ascension", 
                'dec_str': "declination", 
                "st_teff": "host_temperature", 
                'st_mass': "host_mass", 
                'st_rad': "host_radius" 
                }, axis='columns')

df.to_csv('main.csv')
