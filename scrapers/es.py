# Absorb the data from https://arxiv.org/abs/1703.03864v1

# Copy and paste from Table 3:

table3 = """Game
Alien
Amidar
Assault
Asterix
Asteroids
Atlantis
Bank Heist
Battle Zone
Beam Rider
Berzerk
Bowling
Boxing
Breakout
Centipede
Chopper Command
Crazy Climber
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
Ice Hockey
Kangaroo
Krull
Montezumas Revenge
Name This Game
Phoenix
Pit Fall
Pong
Private Eye
Q Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard of Wor
Yars Revenge
Zaxxon
DQN
570.2
133.4
3332.3
124.5
697.1
76108.0
176.3
17560.0
8672.4
NaN
41.2
25.8
303.9
3773.1
3046.0
50992.0
12835.2
-21.6
475.6
-2.3
25.8
157.4
2731.8
216.5
-3.8
2696.0
3864.0
50.0
5439.9
NaN
NaN
16.2
298.2
4589.8
4065.3
9264.0
58.5
2793.9
NaN
NaN
1449.7
34081.0
-2.3
5640.0
32.4
3311.3
54.0
20228.1
246.0
NaN
831.0
A3C FF, 1 day
182.1
283.9
3746.1
6723.0
3009.4
772392.0
946.0
11340.0
13235.9
1433.4
36.2
33.7
551.6
3306.5
4669.0
101624.0
84997.5
0.1
-82.2
13.6
0.1
180.1
8442.8
269.5
-4.7
106.0
8066.6
53.0
5614.0
28181.8
-123.0
11.4
194.4
13752.3
10001.2
31769.0
2.3
2300.2
-13700.0
1884.8
2214.7
64393.0
-10.2
5825.0
26.1
54525.4
19.0
185852.6
5278.0
7270.8
2659.0
ES FF, 1 hour
994.0
112.0
1673.9
1440.0
1562.0
1267410.0
225.0
16600.0
744.0
686.0
30.0
49.8
9.5
7783.9
3710.0
26430.0
1166.5
0.2
95.0
-49.0
31.0
370.0
582.0
805.0
-4.1
11200.0
8647.2
0.0
4503.0
4041.0
0.0
21.0
100.0
147.5
5009.0
16590.0
11.9
1390.0
-15442.5
2090.0
678.5
1470.0
-4.5
4970.0
130.3
67974.0
760.0
22834.8
3480.0
16401.7
6380.0"""

data = table3.split("\n")
names = data[1:52]
dqn = data[53:104]
a3cs = data[105:156]
ess = data[157:]

print ess
for name, a3c, es in zip(names, a3cs, ess):
    metric_name = name.lower().replace(" ", "_") + "_metric"
    a3c_score = float(a3c)
    es_score = float(es)
    print metric_name + ".measure(None, "+ `es_score` + ', "ES (1 hour)", url="https://arxiv.org/abs/1703.03864v1")'
    print metric_name + ".measure(None, "+ `a3c_score` + ', "A3C FF (1 day)", url="https://arxiv.org/abs/1703.03864v1", algorithm_src_url="https://arxiv.org/pdf/1602.01783.pdf", min_date=date(2016,2,4))'
