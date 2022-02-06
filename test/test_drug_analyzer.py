import unittest

from app.drug_analyzer import DrugAnalyzer


class TestDrugAnalyzer(unittest.TestCase):
    def test_initialization(self):
        analyzer = DrugAnalyzer(
            [["L01-10", 1007.67, 102.88, 1.00100], ["L01-06", 996.42, 99.68, 2.00087]]
        )
        self.assertEqual(
            analyzer.data,
            [["L01-10", 1007.67, 102.88, 1.00100], ["L01-06", 996.42, 99.68, 2.00087]],
        )

    def test_addition(self):
        analyzer = DrugAnalyzer(
            [["L01-10", 1007.67, 102.88, 1.00100], ["L01-06", 996.42, 99.68, 2.00087]]
        )
        new_analyzer = analyzer + ["L01-13", 987.63, 101.88, 1.34100]
        self.assertEqual(
            new_analyzer.data,
            [
                ["L01-10", 1007.67, 102.88, 1.00100],
                ["L01-06", 996.42, 99.68, 2.00087],
                ["L01-13", 987.63, 101.88, 1.34100],
            ],
        )

    def test_multiple_additions(self):
        analyzer = DrugAnalyzer(
            [["L01-10", 1007.67, 102.88, 1.00100], ["L01-06", 996.42, 99.68, 2.00087]]
        )
        new_analyzer = (
            analyzer
            + ["L01-13", 987.63, 101.88, 1.34100]
            + ["L01-14", 981.63, 105.88, 1.04100]
        )
        self.assertEqual(
            new_analyzer.data,
            [
                ["L01-10", 1007.67, 102.88, 1.00100],
                ["L01-06", 996.42, 99.68, 2.00087],
                ["L01-13", 987.63, 101.88, 1.34100],
                ["L01-14", 981.63, 105.88, 1.04100],
            ],
        )
