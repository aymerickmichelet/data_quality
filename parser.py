import pandas as pd
from pandera import Check, Column, DataFrameSchema, errors
import pandera.extensions as ext

if __name__ == '__main__':
    file = pd.read_excel('consolidation.xlsx')

    @ext.register_check_method(statistics=[])
    def is_uppercase(pandas_obj):
        return pandas_obj.str is not None and pandas_obj.str.isupper()

    test_schema = DataFrameSchema({
        "nom_amenageur": Column(str, Check.is_uppercase(), nullable=True),
    })

    error_schema = DataFrameSchema({
        "nom_amenageur": Column(str, Check.is_uppercase(), nullable=True),
        "siren_amenageur": Column(int, Check.in_range(100000000, 999999999)),
        "contact_amenageur": Column(str, Check.str_matches(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')),
        "nom_operateur": Column(str, nullable=True),
        "contact_operateur": Column(str, Check.str_matches(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')),
        "telephone_operateur": Column(str, nullable=True),
        "nom_enseigne": Column(str),
        "id_station_itinerance": Column(str, Check.str_matches(r'(?:(?:^|,)(^FR[A-Z0-9]{4,33}$|Non concerné))+$')),
        "id_station_local": Column(str, nullable=True),
        "nom_station": Column(str),
        "implantation_station": Column(str, Check.str_matches(
            r'(Voirie|Parking public|Parking privé à usage public|Parking privé réservé à la clientèle|Station dédiée à la recharge rapide){1}')),
        "adresse_station": Column(str),
        # "code_insee_commune": Column(str, Check.str_matches(r'^([013-9]\d|2[AB1-9])\d{3}$')),
        # Regex officiel code INSEE ne marche pas
        # coordonneesXY
        # Difficile à valider. consolidated_longitude et latitude sont elles validées.
        "nbre_pdc": Column(int, Check.greater_than(0)),
        "id_pdc_itinerance": Column(str, Check.str_matches(r'(?:(?:^|,)(^FR[A-Z0-9]{4,33}$|Non concerné))+$')),
        "id_pdc_local": Column(str, nullable=True),
        "puissance_nominale": Column(float, Check.greater_than_or_equal_to(0)),
        "prise_type_ef": Column(int, Check.in_range(0, 1)),
        "prise_type_2": Column(int, Check.in_range(0, 1)),
        "prise_type_combo_ccs": Column(int, Check.in_range(0, 1)),
        "prise_type_chademo": Column(int, Check.in_range(0, 1)),
        "prise_type_autre": Column(int, Check.in_range(0, 1)),
        "gratuit": Column(int, Check.in_range(0, 1)),
        "paiement_acte": Column(int, Check.in_range(0, 1)),
        "paiement_cb": Column(int, Check.in_range(0, 1)),
        "tarification": Column(str, nullable=True),
        "condition_acces": Column(str, Check.str_matches(r'(Accès libre|Accès réservé){1}')),
        "reservation": Column(int, Check.in_range(0, 1)),
        # "horaires": Column(str, Check.str_matches(r'(.*?)((\d{1,2}:\d{2})-(\d{1,2}:\d{2})|24/7)')),
        # Regex officielle ne marche pas
        "accessibilite_pmr": Column(str, Check.str_matches(
            r'(Réservé PMR|Accessible mais non réservé PMR|Non accessible|Accessibilité inconnue){1}')),
        "restriction_gabarit": Column(str),
        "station_deux_roues": Column(int, Check.in_range(0, 1)),
        "raccordement": Column(str, Check.str_matches(r'(Direct|Indirect){1}')),
        "num_pdl": Column(str, nullable=True),
        # date_mise_en_service
        # Dates, compliqué à valider
        "observations": Column(str, nullable=True),
        # date_maj
        # last_modified
        "datagouv_dataset_id": Column(str),
        "datagouv_resource_id": Column(str),
        "datagouv_organization_or_owner": Column(str),
        "consolidated_longitude": Column(float, Check.in_range(-180, 180)),
        "consolidated_latitude": Column(float, Check.in_range(-180, 180)),
        "consolidated_code_postal": Column(int, Check.in_range(1000, 99999)),
        "consolidated_commune": Column(str),
        "consolidated_is_lon_lat_correct": Column(int, Check.in_range(0, 1)),
        "consolidated_is_code_insee_verified": Column(int, Check.in_range(0, 1)),
    })

    warning_schema = DataFrameSchema({
        "contact_amenageur": Column(str, Check.str_matches(r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b')),
        "contact_operateur": Column(str, Check.str_matches(r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b')),

    })

    try:
        error_schema.validate(file, lazy=True)
    except errors.SchemaErrors as err:
        pd.set_option("display.max_columns", None, "display.max_rows", None)
        err.failure_cases.to_excel("output.xlsx")
        for error in err.schema_errors:
            print(error["error"])
            pass

