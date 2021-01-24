from ..params import ExpMargins, ExpThresholds


def __set_margin(group_exp):
    margin = None

    if group_exp < ExpThresholds.Minimum.value:
        margin = ExpMargins.Minimum.value
    elif group_exp < ExpThresholds.Low.value:
        margin = ExpMargins.Low.value
    elif group_exp < ExpThresholds.Medium.value:
        margin = ExpMargins.Medium.value
    elif group_exp < ExpThresholds.High.value:
        margin = ExpMargins.High.value
    else:
        margin = ExpMargins.Max.value

    return margin

def calculate_fairness(trade_params):
    group_one_exp = trade_params['group_one_exp']
    group_two_exp = trade_params['group_two_exp']

    if group_one_exp == group_two_exp:
        return {
            'fair': True
        }

    exp_difference = abs(group_one_exp - group_two_exp)
    smaller_group = min(group_one_exp, group_two_exp)

    margin = __set_margin(smaller_group)

    if exp_difference <= margin:
        return {
            'fair': True
        }

    benefitted_trainer = None
    if smaller_group == group_one_exp:
        benefitted_trainer = "group_one"
    else:
        benefitted_trainer = "group_two"

    return {
        'fair': False,
        'benefittedTrainer': benefitted_trainer
    }

