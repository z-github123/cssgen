

class Rule(object):  # pragma pylint: disable=too-few-public-methods

    def __init__(self, prop_id):
        self._prop_id = prop_id


class BetweenRule(Rule):  # pragma pylint: disable=too-few-public-methods

    def __init__(self, prop_id, pv, min_val, max_val):
        super(BetweenRule, self).__init__(prop_id)
        self._pv = pv
        self._min = min_val
        self._max = max_val


class GreaterThanRule(Rule):  # pragma pylint: disable=too-few-public-methods

    def __init__(self, prop_id, pv, threshold):
        super(GreaterThanRule, self).__init__(prop_id)
        self._pv = pv
        self._threshold = threshold
