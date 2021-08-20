"""
 Author: S. Suchek
 August 20, 2021
"""

import pandas as pd

def get_children(df, parent_id):
    """
        Find all children generations in the table given parent ID
        :param df:          an input Dataframe
        :param parent_id:  an input parent company ID

    """

    # Find data related to the children of first generation
    child_mask = (df['parentId'] == parent_id) & (df['id'] != parent_id)
    children = df.loc[child_mask, ['id']]
    
    # Recursively find childern of all generation
    for child_id in children["id"].unique().tolist():
        children = children.append(get_children(df, child_id))
    
    return children

def get_land_parcels_for_company(companies, land_parcels, company_id):
    """
        Find land parcels that belong to a certain company and its affiliated companies
        :param companies:          an input Dataframe with companies
        :param land_parcels:       an input Dataframe with land parcels
        :param company_id:         an input company ID

    """
    children = get_children(companies, company_id)
    
    # Land parcels owned by the parent company
    lp = land_parcels[land_parcels["companyId"] == company_id]
    
    # Land parcels owned by the affiliated companies
    lp_indirect = land_parcels[land_parcels["companyId"].isin(children["id"])]
    
    lp = lp.append(lp_indirect)
    
    return lp["id"].unique().tolist()