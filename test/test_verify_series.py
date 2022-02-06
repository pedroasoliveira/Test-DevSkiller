import unittest

from app.drug_analyzer import DrugAnalyzer


class TestVerifySeries(unittest.TestCase):
    def test_passing_case(self):
        analyzer = DrugAnalyzer(
            [
                ["L01-10", 1000.02, 102.88, 1.00100],
                ["L01-06", 999.90, 96.00, 0.00087],
                ["G02-03", 1000, 96.50, 3.00100],
                ["G03-06", 989.01, 119.00, 4.00004],
            ]
        )

        self.assertTrue(
            analyzer.verify_series(
                series_id="L01",
                act_subst_wgt=100,
                act_subst_rate=0.05,
                allowed_imp=0.001,
            )
        )

    def test_small_pills(self):
        analyzer = DrugAnalyzer(
            [
                ["L01-10", 400.02, 102.88, 1.00100],
                ["L01-06", 300.90, 96.00, 0.00087],
                ["G02-03", 1000, 96.50, 3.00100],
                ["G03-06", 989.01, 119.00, 4.00004],
            ]
        )

        self.assertFalse(
            analyzer.verify_series(
                series_id="L01",
                act_subst_wgt=100,
                act_subst_rate=0.05,
                allowed_imp=0.001,
            )
        )

    def test_high_impurities(self):
        analyzer = DrugAnalyzer(
            [
                ["L01-10", 1000.02, 102.88, 1.00100],
                ["L01-06", 999.90, 96.00, 3.00087],
                ["G02-03", 1000, 96.50, 3.00100],
                ["G03-06", 989.01, 119.00, 4.00004],
            ]
        )

        self.assertFalse(
            analyzer.verify_series(
                series_id="L01",
                act_subst_wgt=100,
                act_subst_rate=0.05,
                allowed_imp=0.001,
            )
        )

    def test_low_active_substance(self):
        analyzer = DrugAnalyzer(
            [
                ["L01-10", 1000.02, 94.88, 0.00100],
                ["L01-06", 999.90, 96.00, 0.00087],
                ["L01-06", 999.90, 94.00, 0.00087],
                ["G02-03", 1000, 96.50, 3.00100],
                ["G03-06", 989.01, 119.00, 4.00004],
            ]
        )

        self.assertFalse(
            analyzer.verify_series(
                series_id="L01",
                act_subst_wgt=100,
                act_subst_rate=0.05,
                allowed_imp=0.001,
            )
        )

    def test_high_active_substance(self):
        analyzer = DrugAnalyzer(
            [
                ["L01-10", 1000.02, 105.88, 0.00100],
                ["L01-06", 999.90, 104.00, 0.00087],
                ["L01-06", 999.90, 106.00, 0.00087],
                ["G02-03", 1000, 96.50, 3.00100],
                ["G03-06", 989.01, 119.00, 4.00004],
            ]
        )

        self.assertFalse(
            analyzer.verify_series(
                series_id="L01",
                act_subst_wgt=100,
                act_subst_rate=0.05,
                allowed_imp=0.001,
            )
        )

    def test_one_wrong_pill(self):
        analyzer = DrugAnalyzer(
            [
                ["L01-10", 1000.02, 100.00, 0.00100],
                ["L01-06", 999.90, 100.00, 0.00087],
                ["L01-06", 999.90, 43.26, 0.00087],
                ["G02-03", 1000, 96.50, 3.00100],
                ["G03-06", 989.01, 119.00, 4.00004],
            ]
        )

        self.assertFalse(
            analyzer.verify_series(
                series_id="L01",
                act_subst_wgt=100,
                act_subst_rate=0.05,
                allowed_imp=0.001,
            )
        )
