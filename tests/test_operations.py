def test_get_av_exchange_rates_no_records(client_setup):
    response = client_setup.get('/api/v1/av_exchange_rates')
    expected_results = {
        'success': True,
        'data': [],
        'number_of_records': 0
    }

    assert response.status_code == 200
    assert response.get_json() == expected_results
