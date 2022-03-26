from src.preprocessing.build_validation_dataset import extract_sentences_list


def test_validation_data_extraction(sample_sentence_level_data_path):
    """
    This is a test that's probably not necessary because the function being tested is so simple
    but I want to show how the tests should be written.

    :return:
    """
    expected_sentences = ["$1.4 mnamo mwaka 2008.",
                          "` 17 Basi, akawaacha, akatoka nje ya mji na kwenda Bethania, akalala huko.",
                          '"1982 na ina milio sawa na maujanja yaliwemo kwenye Off The Wall.',
                          "%2012/Act%20555.pdf sheria ya 1996 iliyoruhusu kuanzishwa kwa taasisi za elimu ya juu za kibinafsi.",
                          '“2019-n-CoV: Kile ambacho umma inafaa kufanywa” Kituo cha kuzuia magonjwa Marekani.',
                          '%201/Act%2030.pdf sheria ya mwaka 1971 kuhusu vyuo vikuu na sehemu ya vyuo hivyo.',
                          '`) 20 Basi, imeandikwa katika kitabu cha Zaburi: `Nyumba yake ibaki mahame; mtu yeyote asiishi ndani yake.',
                          '`21 Kwa hiyo, ni lazima mtu mwingine ajiunge nasi kama shahidi wa ufufuo wake Bwana Yesu.',
                          '` 24 Manabii wote, kuanzia Samweli na wale waliomfuata, walitangaza habari za mambo haya ambayo yamekuwa yakitendeka siku hizi.',
                          '` 26 Basi, ilikuwa kwa ajili yenu kwanza kwamba Mungu alimfufua mtumishi wake, alimtuma awabariki kwa kumfanya kila mmoja wenu aachane kabisa na maovu yake."'
                          ]
    assert extract_sentences_list(sample_sentence_level_data_path) == expected_sentences
