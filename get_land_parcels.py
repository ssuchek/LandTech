
"""
 Author: S. Suchek
 August 20, 2021
"""

import argparse
import pandas as pd

from data import companies, land_parcels
from helpers import get_land_parcels_for_company

ap = argparse.ArgumentParser(description="Getting land parcels")
ap.add_argument("--id", required=True, help="Company id")
args = ap.parse_args()


def main():

    companies_df = pd.DataFrame(companies)
    land_parcels_df = pd.DataFrame(land_parcels)
    
    print("Input company ID: {}".format(args.id))

    land_parcels_list = get_land_parcels_for_company(companies=companies_df,
                                                    land_parcels=land_parcels_df,
                                                    company_id = args.id
                                                    )

    print("Company {} owns land parcels: {}".format(args.id, land_parcels_list))

if __name__ == '__main__':
    main()