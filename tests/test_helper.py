from src.helper import get_top_words

def test_get_top_words():
    sample_content = "A mitochondrion is an organelle found in the cells of most eukaryotes, such as animals, plants and fungi. Mitochondria have a double membrane structure and use aerobic respiration to generate adenosine triphosphate (ATP), which is used throughout the cell as a source of chemical energy. They were discovered by Albert von Kölliker in 1857 in the voluntary muscles of insects. The term mitochondrion was coined by Carl Benda in 1898. The mitochondrion is popularly nicknamed the \"powerhouse of the cell\", a phrase coined by Philip Siekevitz in a 1957 article of the same name."

    def test_content():
        response = get_top_words(sample_content)
        assert response == ['the', 'a', 'in', 'of', 'mitochondrion', 'is', 'by', 'as', 'and', 'cell']

        response = get_top_words("", 10, [""])
        assert response == []

        response = get_top_words("mitochondrion organelle found organelle")
        assert response == ['organelle', 'mitochondrion', 'found']

    def test_limit():
        response = get_top_words(sample_content)
        assert len(response) == 10

        response = get_top_words(sample_content, 5)
        assert len(response) == 5

        response = get_top_words(sample_content, 0)
        assert len(response) == 0

    def test_stop_words():
        response = get_top_words(sample_content)
        assert response == ['the', 'a', 'in', 'of', 'mitochondrion', 'is', 'by', 'as', 'and', 'cell']

        response = get_top_words(sample_content, stop_words=['the', 'a', 'in', 'of'])
        assert response == ['mitochondrion', 'is', 'by', 'as', 'and', 'cell', 'coined', 'an', 'organelle', 'found']

        response = get_top_words("mitochondrion is an organelle found in the cells", stop_words=['mitochondrion', 'is', 'an', 'organelle', 'found', 'in', 'the', 'cells'])
        assert response == []

    test_content()
    test_limit()
    test_stop_words()
