from project.tests.base import BaseTestCase


class TradeFairnessTest(BaseTestCase):
    def test_close_exp_groups_are_considered_fair(self):
        token = self.create_token()

        exp_groups = [(50, 55), (120, 150), (660, 600), (1200, 1300), (2149, 2000)]

        for group in exp_groups:
            query = {
                'group_one': group[0],
                'group_two': group[1],
            }
            response = self.client.get('/api/trades/fairness', query_string=query, headers=token)
            data = response.json

            self.assert200(response)
            self.assertTrue(data['fair'])

    def test_far_exp_groups_are_considered_unfair(self):
        token = self.create_token()

        exp_groups = [(50, 70), (120, 180), (700, 600), (1200, 1301), (2200, 2000)]

        for group in exp_groups:
            query = {
                'group_one': group[0],
                'group_two': group[1],
            }
            response = self.client.get('/api/trades/fairness', query_string=query, headers=token)
            data = response.json

            self.assert200(response)
            self.assertFalse(data['fair'])
    
    def test_unfair_trades_show_the_benefitted_trainer(self):
        token = self.create_token()

        trainer_one_benefits = [(50, 70), (120, 180), (600, 700), (1200, 1301), (2000, 2200)]
        trainer_two_benefits = [(70, 50), (180, 120), (700, 600), (1301, 1200), (2200, 2000)]

        for group in trainer_one_benefits:
            query = {
                'group_one': group[0],
                'group_two': group[1],
            }
            response = self.client.get('/api/trades/fairness', query_string=query, headers=token)
            data = response.json

            self.assert200(response)
            self.assertFalse(data['fair'])
            self.assertEqual(data['benefittedTrainer'], 'group_one')
        
        for group in trainer_two_benefits:
            query = {
                'group_one': group[0],
                'group_two': group[1],
            }
            response = self.client.get('/api/trades/fairness', query_string=query, headers=token)
            data = response.json

            self.assert200(response)
            self.assertFalse(data['fair'])
            self.assertEqual(data['benefittedTrainer'], 'group_two')
    
    def test_fairness_fails_if_exp_less_than_one(self):
        token = self.create_token()
        
        exp_groups = [(0, 0), (0, 150), (660, 0), (-20, 1300), (2149, -100), (-10, -15)]

        for group in exp_groups:
            query = {
                'group_one': group[0],
                'group_two': group[1],
            }
            response = self.client.get('/api/trades/fairness', query_string=query, headers=token)
            data = response.json

            self.assertEqual(response.status_code, 400)

