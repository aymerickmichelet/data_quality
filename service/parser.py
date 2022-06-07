import os.path
import pandas as pd
from pandera import Check, Column, DataFrameSchema, errors
import pandera.extensions as ext


@ext.register_check_method(statistics=[])
def is_uppercase(pandas_obj):
    return pandas_obj.str is not None and pandas_obj.str.isupper()


def parser(file_path):
    if not os.path.exists(file_path):
        print("File not found. Trying with default.")
        file_path = "bnls.xlsx"
        if not os.path.exists(file_path):
            return {"ErrorMessage": "File path is invalid"}

    file = pd.read_excel(file_path)

    error_schema = DataFrameSchema({
        "nom": Column(str),
        "insee": Column(int, Check.in_range(1000,99999)),
        "adresse": Column(str),
        "url": Column(str, Check.str_matches(r'^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+$')),
        "type_usagers": Column(str, Check.str_matches(
            r'(tous|abonnés){1}')),
        "gratuit": Column(int, Check.in_range(0, 1)),
        "nb_places": Column(int, Check.greater_than(0)),
        "nb_pr": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "nb_pmr": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "nb_voitures_electriques": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "nb_autopartage": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "nb_covoit": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "hauteur_max": Column(str, Check.str_matches(r'^(\d+|N/A)$')),
        "num_siret": Column(int, Check.in_range(10000000000000, 99999999999999)),
        "Xlong": Column(float, Check.in_range(-180, 180)),
        "Ylat": Column(float, Check.in_range(-90, 90)),
        "tarif_pmr": Column(str, Check.str_matches(
            r'(gratuit|normal_payant|tarif_special){1}')),
        "tarif_1h": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "tarif_2h": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "tarif_3h": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "tarif_4h": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "tarif_24h": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "abo_resident": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "abo_non_resident": Column(int, Check.greater_than_or_equal_to(0), nullable=True),
        "type_ouvrage": Column(str, Check.str_matches(
            r'(ouvrage|enclos_en_surface){1}')),
        "info": Column(str, nullable=True)
    })

    error_percent = 0
    error_df = pd.DataFrame()

    try:
        error_schema.validate(file, lazy=True)
    except errors.SchemaErrors as err:
        pd.set_option("display.max_columns", None, "display.max_rows", None)
        error_df = err.failure_cases
        error_percent = len(pd.unique(error_df['index']))/len(file)*100


    if error_df is not None:
        with pd.ExcelWriter(
            path=file_path,
            engine="openpyxl",
            mode="a",
            if_sheet_exists="replace"
        )as writer:
            error_df.to_excel(excel_writer=writer, sheet_name="Error")

    correct_percent = 100 - error_percent
    results = {
        "correct": correct_percent,
        "error": error_percent,
        "total_lines": len(file),
        "error_lines": len(pd.unique(error_df['index'])),
        "correct_lines": len(file) - len(pd.unique(error_df['index']))
    }
    print(results)
    return results


if __name__ == "__main__":
    parser("bnls.xlsx")