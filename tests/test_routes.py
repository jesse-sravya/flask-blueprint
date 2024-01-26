def test_health_check(client):
    response = client.get('/health')
    assert b"OK!" in response.data

def test_fetch(client, mocker):
    def test_valid_response():
        mocked_call_api_value = "A mitochondrion is an organelle found in the cells of most eukaryotes, such as animals, plants and fungi. Mitochondria have a double membrane structure and use aerobic respiration to generate adenosine triphosphate (ATP), which is used throughout the cell as a source of chemical energy. They were discovered by Albert von Kölliker in 1857 in the voluntary muscles of insects. The term mitochondrion was coined by Carl Benda in 1898. The mitochondrion is popularly nicknamed the \"powerhouse of the cell\", a phrase coined by Philip Siekevitz in a 1957 article of the same name."
        mocker.patch("src.routes.get_article", return_value=[True, mocked_call_api_value])
        response = client.get('/fetch/mitochondrion')
        assert response.status_code == 200
        assert response.json['success'] == True
        assert len(response.json['data']) is not None

    def test_empty_response():
        mocker.patch("src.routes.get_article", return_value=[True, ""])

        response = client.get('/fetch/mitochondrion')
        assert response.status_code == 200
        assert response.json['success'] == True
        assert len(response.json['data']) == 0

    def test_crash_response():
        mocker.patch("src.routes.get_article", return_value=[False, None])

        response = client.get('/fetch/mitochondrion')
        assert response.status_code == 200
        assert response.json['success'] == False
        assert 'data' not in response.json
        assert response.json['message'] == "wikipedia hasn't returned a valid response"


    test_valid_response()
    test_empty_response()
    test_crash_response()
