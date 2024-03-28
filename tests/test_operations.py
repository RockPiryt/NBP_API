def test_get_av_exchange_rates_no_records(client_setup):
    response = client_setup.get('/api/v1/av_exchange_rates')
    expected_results = {
        'success': True,
        'data': [],
        'number_of_records': 0
    }

    assert response.status_code == 200
    assert response.get_json() == expected_results


def test_get_av_exchange_rates_all(client_setup):
    response = client_setup.get('/api/v1/av_exchange_rates')
    response_data = response.get_json()


    assert response.status_code == 200
    assert response_data['success'] is True
    assert response_data['number_of_records'] == 9
