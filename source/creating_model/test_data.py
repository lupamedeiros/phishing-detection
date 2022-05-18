import pytest
import wandb
import pandas as pd

# This is global so all tests are collected under the same run

run = wandb.init(project="phishing-detection", job_type="data_checks")

@pytest.fixture(scope="session")
def data():

    local_path = run.use_artifact("phishing-detection/preprocessed_data.csv:latest")
    print(local_path)
    df = pd.read_csv(local_path)

    return df

def test_data_length(data):
    """We test if we have enouth samples to proceed

    :param data: DataFrame of the data set
    :type data: pandas.DataFrame
    """

    assert len(data) > 10000

def test_number_of_columns(data):
    """We test the number of features

    :param data: DataFrame of the dataset
    :type data: pandas.DataFrame
    """

    assert data.shape[1] == 89

def test_column_presence_and_type(data):
    """
    Here we test if each column has the expected data type in all samples

    :param data: DataFrame of the dataset
    :type data: pandas.DataFrame
    """

    required_columns = {
        "length_url": pd.api.types.is_int64_dtype,
        "length_hostname": pd.api.types.is_int64_dtype,
        "ip": pd.api.types.is_int64_dtype,
        "nb_dots": pd.api.types.is_int64_dtype,
        "nb_hyphens": pd.api.types.is_int64_dtype,
        "nb_at": pd.api.types.is_int64_dtype,
        "nb_qm": pd.api.types.is_int64_dtype,
        "nb_and": pd.api.types.is_int64_dtype,
        "nb_or": pd.api.types.is_int64_dtype,
        "nb_eq": pd.api.types.is_int64_dtype,
        "nb_underscore": pd.api.types.is_int64_dtype,
        "nb_tilde": pd.api.types.is_int64_dtype,
        "nb_percent": pd.api.types.is_int64_dtype,
        "nb_slash": pd.api.types.is_int64_dtype,
        "nb_star": pd.api.types.is_int64_dtype,
        "nb_colon": pd.api.types.is_int64_dtype,
        "nb_comma": pd.api.types.is_int64_dtype,
        "nb_semicolumn": pd.api.types.is_int64_dtype,
        "nb_dollar": pd.api.types.is_int64_dtype,
        "nb_space": pd.api.types.is_int64_dtype,
        "nb_www": pd.api.types.is_int64_dtype,
        "nb_com": pd.api.types.is_int64_dtype,
        "nb_dslash": pd.api.types.is_int64_dtype,
        "http_in_path": pd.api.types.is_int64_dtype,
        "https_token": pd.api.types.is_int64_dtype,
        "ratio_digits_url": pd.api.types.is_float64_dtype,
        "ratio_digits_host": pd.api.types.is_float64_dtype,
        "punycode": pd.api.types.is_int64_dtype,
        "port": pd.api.types.is_int64_dtype,
        "tld_in_path": pd.api.types.is_int64_dtype,
        "tld_in_subdomain": pd.api.types.is_int64_dtype,
        "abnormal_subdomain": pd.api.types.is_int64_dtype,
        "nb_subdomains": pd.api.types.is_int64_dtype,
        "prefix_suffix": pd.api.types.is_int64_dtype,
        "random_domain": pd.api.types.is_int64_dtype,
        "shortening_service": pd.api.types.is_int64_dtype,
        "path_extension": pd.api.types.is_int64_dtype,
        "nb_redirection": pd.api.types.is_int64_dtype,
        "nb_external_redirection": pd.api.types.is_int64_dtype,
        "length_words_raw": pd.api.types.is_int64_dtype,
        "char_repeat": pd.api.types.is_int64_dtype,
        "shortest_words_raw": pd.api.types.is_int64_dtype,
        "shortest_words_host": pd.api.types.is_int64_dtype,
        "shortest_words_path": pd.api.types.is_int64_dtype,
        "longest_words_raw": pd.api.types.is_int64_dtype,
        "longest_words_host": pd.api.types.is_int64_dtype,
        "longest_words_path": pd.api.types.is_int64_dtype,
        "avg_words_raw": pd.api.types.is_float64_dtype,
        "avg_word_host": pd.api.types.is_float64_dtype,
        "avg_word_path": pd.api.types.is_float64_dtype,
        "phish_hints": pd.api.types.is_int64_dtype,
        "domain_in_brand": pd.api.types.is_int64_dtype,
        "brand_in_subdomain": pd.api.types.is_int64_dtype,
        "brand_in_path": pd.api.types.is_int64_dtype,
        "suspecious_tld": pd.api.types.is_int64_dtype,
        "statistical_report": pd.api.types.is_int64_dtype,
        "nb_hyperlinks": pd.api.types.is_int64_dtype,
        "ratio_intHyperlinks": pd.api.types.is_float64_dtype,
        "ratio_extHyperlinks": pd.api.types.is_float64_dtype,
        "ratio_nullHyperlinks": pd.api.types.is_int64_dtype,
        "nb_extCSS": pd.api.types.is_int64_dtype,
        "ratio_intRedirection": pd.api.types.is_int64_dtype,
        "ratio_extRedirection": pd.api.types.is_float64_dtype,
        "ratio_intErrors": pd.api.types.is_int64_dtype,
        "ratio_extErrors": pd.api.types.is_float64_dtype,
        "login_form": pd.api.types.is_int64_dtype,
        "external_favicon": pd.api.types.is_int64_dtype,
        "link_in_tags": pd.api.types.is_float64_dtype,
        "submit_email": pd.api.types.is_int64_dtype,
        "ratio_intMedia": pd.api.types.is_float64_dtype,
        "ratio_extMedia": pd.api.types.is_float64_dtype,
        "sfh": pd.api.types.is_int64_dtype,
        "iframe": pd.api.types.is_int64_dtype,
        "popup_window": pd.api.types.is_int64_dtype,
        "safe_anchor": pd.api.types.is_float64_dtype,
        "onmouseover": pd.api.types.is_int64_dtype,
        "right_clic": pd.api.types.is_int64_dtype,
        "empty_title": pd.api.types.is_int64_dtype,
        "domain_in_title": pd.api.types.is_int64_dtype,
        "domain_with_copyright": pd.api.types.is_int64_dtype,
        "whois_registered_domain": pd.api.types.is_int64_dtype,
        "domain_registration_length": pd.api.types.is_int64_dtype,
        "domain_age": pd.api.types.is_int64_dtype,
        "web_traffic": pd.api.types.is_int64_dtype,
        "dns_record": pd.api.types.is_int64_dtype,
        "google_index": pd.api.types.is_int64_dtype,
        "page_rank": pd.api.types.is_int64_dtype,
        "status": pd.api.types.is_object_dtype
    }

    # Check column presence
    assert set(data.columns.values).issuperset(required_columns.keys())

    # Check data type
    for col_name, format_verification_funct in required_columns.items():
        assert format_verification_funct(data[col_name]), f"Column {col_name} failed test {format_verification_funct}"

run.finish()