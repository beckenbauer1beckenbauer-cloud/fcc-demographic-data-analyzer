import unittest
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(print_data=False)

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertCountEqual(actual, expected)

    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.4
        self.assertAlmostEqual(actual, expected, places=1)

    def test_percentage_bachelors(self):
        actual = self.data['percentage_bachelors']
        expected = 16.4
        self.assertAlmostEqual(actual, expected, places=1)

    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 46.5
        self.assertAlmostEqual(actual, expected, places=1)

    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 17.4
        self.assertAlmostEqual(actual, expected, places=1)

    def test_min_work_hours(self):
        actual = self.data['min_work_hours']
        expected = 1
        self.assertAlmostEqual(actual, expected, places=1)

    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 10.0
        self.assertAlmostEqual(actual, expected, places=1)

    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = 'Iran'
        self.assertEqual(actual, expected)

    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 41.9
        self.assertAlmostEqual(actual, expected, places=1)

    def test_top_IN_occupation(self):
        actual = self.data['top_IN_occupation']
        expected = 'Prof-specialty'
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
