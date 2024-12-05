import pandas as pd 
import pytest
from validate_functions import validate_vict_sex, validate_vict_age
from stats_function import calculate_mean, calculate_median

def test_validate_vict_sex():
    df = pd.DataFrame({'Vict sex': ['M', 'F', 'M', 'W']})
    assert not validate_vict_sex(df['Vict sex'])

def test_validate_vict_age():
    df = pd.DataFrame({'Vict age': [25, 35, 150, -5, None]})
    assert not validate_vict_age(df['Vict age'])

def test_calculate_mean():
    df = pd.DataFrame({'Vict age': [25, 35, 45, 55]})
    assert calculate_mean(df['Vict age']) == 40

def test_calculate_median():
    df = pd.DataFrame({'Vict age': [25, 35, 45, 55]})
    assert calculate_median(df['Vict age']) == 40

def test_calculate_mean_edge_case():
    df = pd.DataFrame({'Vict age': ['eight', None]})
    with pytest.raises(TypeError):
        calculate_mean(df['Vict age'])

