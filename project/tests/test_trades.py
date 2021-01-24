from project.tests.base import BaseTestCase
from project.api.trades.models import Trade, TradeGroup, TradePokemon


class TradeFairnessTest(BaseTestCase):
    def __build_trade_data(self):
        return {
            'isFair': True,
            'tradeGroups': [
                {
                    'wasBenefitted': False,
                    'pokemons': [
                        {
                            'name': 'audino',
                            'spriteUrl': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/531.png'
                        }
                    ]
                },
                {
                    'wasBenefitted': False,
                    'pokemons': [
                        {
                            'name': 'gengar',
                            'spriteUrl': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png'
                        },
                        {
                            'name': 'kirlia',
                            'spriteUrl': 'https://raw.githubuserco…/sprites/pokemon/281.png'
                        },
                        {
                            'name': 'rattata',
                            'spriteUrl': ''
                        }
                    ]
                }
            ]
        }

    def test_post_trade_creates_trade_correctly(self):
        self.create_user()
        token = self.create_token()

        trades = Trade.query.all()
        trade_groups = TradeGroup.query.all()
        trade_pokemons = TradePokemon.query.all()

        self.assertEqual(len(trades), 0)
        self.assertEqual(len(trade_groups), 0)
        self.assertEqual(len(trade_pokemons), 0)

        trade_data = self.__build_trade_data()

        response = self.client.post('/api/trades', json=trade_data, headers=token)

        trades = Trade.query.all()
        trade_groups = TradeGroup.query.all()
        trade_pokemons = TradePokemon.query.all()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(trades), 1)
        self.assertEqual(len(trade_groups), 2)
        self.assertEqual(len(trade_pokemons), 4)
    
    def test_post_trade_fails_without_two_trade_groups(self):
        self.create_user()
        token = self.create_token()

        trades = Trade.query.all()
        trade_groups = TradeGroup.query.all()
        trade_pokemons = TradePokemon.query.all()

        self.assertEqual(len(trades), 0)
        self.assertEqual(len(trade_groups), 0)
        self.assertEqual(len(trade_pokemons), 0)

        trade_data = self.__build_trade_data()
        trade_data['tradeGroups'] = trade_data['tradeGroups'][:1]

        response = self.client.post('/api/trades', json=trade_data, headers=token)

        trades = Trade.query.all()
        trade_groups = TradeGroup.query.all()
        trade_pokemons = TradePokemon.query.all()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(trades), 0)
        self.assertEqual(len(trade_groups), 0)
        self.assertEqual(len(trade_pokemons), 0)

    def test_get_trades_fetchs_all_trades_for_user(self):
        self.create_user()
        token = self.create_token()

        trade_data = self.__build_trade_data()
        response = self.client.post('/api/trades', json=trade_data, headers=token)
        response = self.client.post('/api/trades', json=trade_data, headers=token)

        response = self.client.get('/api/trades', headers=token)
        data = response.json

        self.assert200(response)
        self.assertEqual(len(data['trades']), 2)
    
    def test_get_trades_doesnt_fetch_other_users_trades(self):
        self.create_user()
        self.create_user(username='otheruser')
        token = self.create_token()
        other_token = self.create_token(identity='otheruser')

        trade_data = self.__build_trade_data()
        response = self.client.post('/api/trades', json=trade_data, headers=token)
        response = self.client.post('/api/trades', json=trade_data, headers=other_token)

        response = self.client.get('/api/trades', headers=token)
        data = response.json

        self.assert200(response)
        self.assertEqual(len(data['trades']), 1)
    
    def test_get_trade_fetchs_single_trade_by_id(self):
        self.create_user()
        token = self.create_token()

        trade_data = self.__build_trade_data()
        response = self.client.post('/api/trades', json=trade_data, headers=token)

        data = response.json
        trade_id = data['id']

        response = self.client.get('/api/trades/%s' % trade_id, headers=token)
        data = response.json

        self.assert200(response)
        self.assertEqual(data['trade']['id'], trade_id)
    
    def test_get_trade_doesnt_fetch_other_users_trade(self):
        self.create_user()
        self.create_user(username='otheruser')
        token = self.create_token()
        other_token = self.create_token(identity='otheruser')

        trade_data = self.__build_trade_data()
        response = self.client.post('/api/trades', json=trade_data, headers=other_token)

        data = response.json
        trade_id = data['id']

        response = self.client.get('/api/trades/%s' % trade_id, headers=token)
        data = response.json

        self.assert404(response)
