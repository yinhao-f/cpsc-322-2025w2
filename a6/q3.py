$ python -i probDo.py

>>> bn_sprinklerv.queryDo(Sprinkler, obs={Season: "dry_season"})
{'on': 0.4, 'off': 0.6}
>>> bn_sprinklerv.queryDo(Sprinkler)
{'on': 0.20500000000000002, 'off': 0.7949999999999999}
>>> bn_sprinklerv.queryDo(Grass_wet, obs={Rained: True})
{False: 0.2845333333333333, True: 0.7154666666666667}
>>> bn_sprinklerv.queryDo(Grass_wet)
{False: 0.51145, True: 0.48855000000000004}