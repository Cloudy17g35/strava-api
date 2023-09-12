from src.data_preprocessing import main as dp


def test1_convert_m_per_s_to_km_per_h():
    expected = 36.0
    result = dp.convert_m_per_s_to_km_per_h(10.0)
    assert result == expected


def test2_convert_m_per_s_to_km_per_h():
    expected = 11.99
    result = dp.convert_m_per_s_to_km_per_h(3.33)
    assert result == expected