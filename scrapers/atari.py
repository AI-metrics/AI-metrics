#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

from data.video_games import *
import re

# Machinery for importing both copy-and-pasted and (where necessary) OCR'd tables from various Atari research papers
# Copying and pasting tables from PDFs produces very weird results sometimes, so we make no promises that there aren't
# anyforms of weirdness here.

# The common case is that PDF tables paste column-wise; but some are row-wise so we have machinery for both.

# COLUMN-WISE RESULT TABLES:

wang_table_2 = """GAMES
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
Defender
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
H.E.R.O.
Ice Hockey
James Bond
Kangaroo
Krull
Kung-Fu Master
Montezuma’s Revenge
Ms. Pac-Man
Name This Game
Phoenix
Pitfall!
Pong
Private Eye
Q*Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Surround
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard Of Wor
Yars Revenge
Zaxxon
NO. ACTIONS
18
10
7
9
14
4
18
18
9
18
6
18
4
18
18
9
18
6
18
9
18
3
18
8
18
18
18
18
18
18
14
18
9
6
8
18
3
18
6
18
18
18
18
3
18
6
18
5
18
10
8
6
18
9
10
18
18
R ANDOM
227.8
5.8
222.4
210.0
719.1
12,850.0
14.2
2,360.0
363.9
123.7
23.1
0.1
1.7
2,090.9
811.0
10,780.5
2,874.5
152.1
-18.6
0.0
-91.7
0.0
65.2
257.6
173.0
1,027.0
-11.2
29.0
52.0
1,598.0
258.5
0.0
307.3
2,292.3
761.4
-229.4
-20.7
24.9
163.9
1,338.5
11.5
2.2
68.4
-17,098.1
1,236.3
148.0
664.0
-10.0
-23.8
3,568.0
11.4
533.4
0.0
16,256.9
563.5
3,092.9
32.5
HUMAN
7,127.7
1,719.5
742.0
8,503.3
47,388.7
29,028.1
753.1
37,187.5
16,926.5
2,630.4
160.7
12.1
30.5
12,017.0
7,387.8
35,829.4
18,688.9
1,971.0
-16.4
860.5
-38.7
29.6
4,334.7
2,412.5
3,351.4
30,826.4
0.9
302.8
3,035.0
2,665.5
22,736.3
4,753.3
6,951.6
8,049.0
7,242.6
6,463.7
14.6
69,571.3
13,455.0
17,118.0
7,845.0
11.9
42,054.7
-4,336.9
12,326.7
1,668.7
10,250.0
6.5
-8.3
5,229.2
167.6
11,693.2
1,187.5
17,667.9
4,756.5
54,576.9
9,173.3
DQN
1,620.0
978.0
4,280.4
4,359.0
1,364.5
279,987.0
455.0
29,900.0
8,627.5
585.6
50.4
88.0
385.5
4,657.7
6,126.0
110,763.0
23,633.0
12,149.4
-6.6
729.0
-4.9
30.8
797.4
8,777.4
473.0
20,437.8
-1.9
768.5
7,259.0
8,422.3
26,059.0
0.0
3,085.6
8,207.8
8,485.2
-286.1
19.5
146.7
13,117.3
7,377.6
39,544.0
63.9
5,860.6
-13,062.3
3,482.8
1,692.3
54,282.0
-5.6
12.2
4,870.0
68.1
9,989.9
163.0
196,760.4
2,704.0
18,098.9
5,363.0
DDQN
3,747.7
1,793.3
5,393.2
17,356.5
734.7
106,056.0
1,030.6
31,700.0
13,772.8
1,225.4
68.1
91.6
418.5
5,409.4
5,809.0
117,282.0
35,338.5
58,044.2
-5.5
1,211.8
15.5
33.3
1,683.3
14,840.8
412.0
20,130.2
-2.7
1,358.0
12,992.0
7,920.5
29,710.0
0.0
2,711.4
10,616.0
12,252.5
-29.9
20.9
129.7
15,088.5
14,884.5
44,127.0
65.1
16,452.7
-9,021.8
3,067.8
2,525.5
60,142.0
-2.9
-22.8
8,339.0
218.4
22,972.2
98.0
309,941.9
7,492.0
11,712.6
10,163.0
DUEL
4,461.4
2,354.5
4,621.0
28,188.0
2,837.7
382,572.0
1,611.9
37,150.0
12,164.0
1,472.6
65.5
99.4
345.3
7,561.4
11,215.0
143,570.0
42,214.0
60,813.3
0.1
2,258.2
46.4
0.0
4,672.8
15,718.4
588.0
20,818.2
0.5
1,312.5
14,854.0
11,451.9
34,294.0
0.0
6,283.5
11,971.1
23,092.2
0.0
21.0
103.0
19,220.3
21,162.6
69,524.0
65.3
50,254.2
-8,857.4
2,250.8
6,427.3
89,238.0
4.4
5.1
11,666.0
211.4
44,939.6
497.0
98,209.5
7,855.0
49,622.1
12,944.0
P RIOR .
4,203.8
1,838.9
7,672.1
31,527.0
2,654.3
357,324.0
1,054.6
31,530.0
23,384.2
1,305.6
47.9
95.6
373.9
4,463.2
8,600.0
141,161.0
31,286.5
71,846.4
18.5
2,093.0
39.5
33.7
4,380.1
32,487.2
548.5
23,037.7
1.3
5,148.0
16,200.0
9,728.0
39,581.0
0.0
6,518.7
12,270.5
18,992.7
-356.5
20.6
200.0
16,256.5
14,522.3
57,608.0
62.6
26,357.8
-9,996.9
4,309.0
2,865.8
63,302.0
8.9
0.0
9,197.0
204.6
16,154.1
54.0
282,007.3
4,802.0
11,357.0
10,469.0
PRIOR. DUEL.
3,941.0
2,296.8
11,477.0
375,080.0
1,192.7
395,762.0
1,503.1
35,520.0
30,276.5
3,409.0
46.7
98.9
366.0
7,687.5
13,185.0
162,224.0
41,324.5
72,878.6
-12.5
2,306.4
41.3
33.0
7,413.0
104,368.2
238.0
21,036.5
-0.4
812.0
1,792.0
10,374.4
48,375.0
0.0
3,327.3
15,572.5
70,324.3
0.0
20.9
206.0
18,760.3
20,607.6
62,151.0
27.5
931.6
-19,949.9
133.4
15,311.5
125,117.0
1.2
0.0
7,553.0
245.9
33,879.1
48.0
479,197.0
12,352.0
69,618.1
13,886.0"""

wang_table_3 = """GAMES
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
Defender
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
H.E.R.O.
Ice Hockey
James Bond
Kangaroo
Krull
Kung-Fu Master
Montezuma’s Revenge
Ms. Pac-Man
Name This Game
Phoenix
Pitfall!
Pong
Private Eye
Q*Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Surround
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard Of Wor
Yars Revenge
Zaxxon
N O . A CTIONS
18
10
7
9
14
4
18
18
9
18
6
18
4
18
18
9
18
6
18
9
18
3
18
8
18
18
18
18
18
18
14
18
9
6
8
18
3
18
6
18
18
18
18
3
18
6
18
5
18
10
8
6
18
9
10
18
18
R ANDOM
128.3
11.8
166.9
164.5
871.3
13,463.0
21.7
3,560.0
254.6
196.1
35.2
-1.5
1.6
1,925.5
644.0
9,337.0
1,965.5
208.3
-16.0
-81.8
-77.1
0.1
66.4
250.0
245.5
1,580.3
-9.7
33.5
100.0
1,151.9
304.0
25.0
197.8
1,747.8
1,134.4
-348.8
-18.0
662.8
183.0
588.3
200.0
2.4
215.5
-15,287.4
2,047.2
182.6
697.0
-9.7
-21.4
3,273.0
12.7
707.2
18.0
20,452.0
804.0
1,476.9
475.0
HUMAN
6,371.3
1,540.4
628.9
7,536.0
36,517.3
26,575.0
644.5
33,030.0
14,961.0
2,237.5
146.5
9.6
27.9
10,321.9
8,930.0
32,667.0
14,296.0
3,442.8
-14.4
740.2
5.1
25.6
4,202.8
2,311.0
3,116.0
25,839.4
0.5
368.5
2,739.0
2,109.1
20,786.8
4,182.0
15,375.0
6,796.0
6,686.2
5,998.9
15.5
64,169.1
12,085.0
14,382.2
6,878.0
8.9
40,425.8
-3,686.6
11,032.6
1,464.9
9,528.0
5.4
-6.7
5,650.0
138.3
9,896.1
1,039.0
15,641.1
4,556.0
47,135.2
8,443.0
DQN
634.0
178.4
3,489.3
3,170.5
1,458.7
292,491.0
312.7
23,750.0
9,743.2
493.4
56.5
70.3
354.5
3,973.9
5,017.0
98,128.0
15,917.5
12,550.7
-6.0
626.7
-1.6
26.9
496.1
8,190.4
298.0
14,992.9
-1.6
697.5
4,496.0
6,206.0
20,882.0
47.0
1,092.3
6,738.8
7,484.8
-113.2
18.0
207.9
9,271.5
4,748.5
35,215.0
58.7
4,216.7
-12,142.1
1,295.4
1,293.8
52,970.0
-6.0
11.1
4,786.0
45.6
8,038.5
136.0
154,414.1
1,609.0
4,577.5
4,412.0
DDQN
1,033.4
169.1
6,060.8
16,837.0
1,193.2
319,688.0
886.0
24,740.0
17,417.2
1,011.1
69.6
73.5
368.9
3,853.5
3,495.0
113,782.0
27,510.0
69,803.4
-0.3
1,216.6
3.2
28.8
1,448.1
15,253.0
200.5
14,892.5
-2.5
573.0
11,204.0
6,796.1
30,207.0
42.0
1,241.3
8,960.3
12,366.5
-186.7
19.1
-575.5
11,020.8
10,838.4
43,156.0
59.1
14,498.0
-11,490.4
810.0
2,628.7
58,365.0
1.9
-7.8
6,608.0
92.2
19,086.9
21.0
367,823.7
6,201.0
6,270.6
8,593.0
D UEL
1,486.5
172.7
3,994.8
15,840.0
2,035.4
445,360.0
1,129.3
31,320.0
14,591.3
910.6
65.7
77.3
411.6
4,881.0
3,784.0
124,566.0
33,996.0
56,322.8
-0.8
2,077.4
-4.1
0.2
2,332.4
20,051.4
297.0
15,207.9
-1.3
835.5
10,334.0
8,051.6
24,288.0
22.0
2,250.6
11,185.1
20,410.5
-46.9
18.8
292.6
14,175.8
16,569.4
58,549.0
62.0
37,361.6
-11,928.0
1,768.4
5,993.1
90,804.0
4.0
4.4
6,601.0
48.0
24,759.2
200.0
110,976.2
7,054.0
25,976.5
10,164.0
P RIOR .
1,334.7
129.1
6,548.9
22,484.5
1,745.1
330,647.0
876.6
25,520.0
31,181.3
865.9
52.0
72.3
343.0
3,489.1
4,635.0
127,512.0
23,666.5
61,277.5
16.0
1,831.0
9.8
28.9
3,510.0
34,858.8
269.5
20,889.9
-0.2
3,961.0
12,185.0
6,872.8
31,676.0
51.0
1,865.9
10,497.6
16,903.6
-427.0
18.9
670.7
9,944.0
11,807.2
52,264.0
56.2
25,463.7
-10,169.1
2,272.8
3,912.1
61,582.0
5.9
-5.3
5,963.0
56.9
12,157.4
94.0
295,972.8
5,727.0
4,687.4
9,474.0
P RIOR . D UEL .
823.7
238.4
10,950.6
364,200.0
1,021.9
423,252.0
1,004.6
30,650.0
37,412.2
2,178.6
50.4
79.2
354.6
5,570.2
8,058.0
127,853.0
34,415.0
73,371.3
-10.7
2,223.9
17.0
28.2
4,038.4
105,148.4
167.0
15,459.2
0.5
585.0
861.0
7,658.6
37,484.0
24.0
1,007.8
13,637.9
63,597.0
-243.6
18.4
1,277.6
14,063.0
16,496.8
54,630.0
24.7
1,431.2
-18,955.8
280.6
8,978.0
127,073.0
-0.2
-13.2
4,871.0
108.6
22,681.3
29.0
447,408.6
10,471.0
58,145.9
11,320.0"""

# Absorb the data from https://arxiv.org/abs/1703.03864v1

# Copy and paste from Table 3:

es_table3 = """Game
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

bellemare_figure_14 = """GAMES
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
Defender
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
H.E.R.O.
Ice Hockey
James Bond
Kangaroo
Krull
Kung-Fu Master
Montezuma’s Revenge
Ms. Pac-Man
Name This Game
Phoenix
Pitfall!
Pong
Private Eye
Q*Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Surround
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard Of Wor
Yars’ Revenge
Zaxxon
RANDOM
227.8
5.8
222.4
210.0
719.1
12,850.0
14.2
2,360.0
363.9
123.7
23.1
0.1
1.7
2,090.9
811.0
10,780.5
2,874.5
152.1
-18.6
0.0
-91.7
0.0
65.2
257.6
173.0
1,027.0
-11.2
29.0
52.0
1,598.0
258.5
0.0
307.3
2,292.3
761.4
-229.4
-20.7
24.9
163.9
1,338.5
11.5
2.2
68.4
-17,098.1
1,236.3
148.0
664.0
-10.0
-23.8
3,568.0
11.4
533.4
0.0
16,256.9
563.5
3,092.9
32.5 
HUMAN
7,127.7
1,719.5
742.0
8,503.3
47,388.7
29,028.1
753.1
37,187.5
16,926.5
2,630.4
160.7
12.1
30.5
12,017.0
7,387.8
35,829.4
18,688.9
1,971.0
-16.4
860.5
-38.7
29.6
4,334.7
2,412.5
3,351.4
30,826.4
0.9
302.8
3,035.0
2,665.5
22,736.3
4,753.3
6,951.6
8,049.0
7,242.6
6,463.7
14.6
69,571.3
13,455.0
17,118.0
7,845.0
11.9
42,054.7
-4,336.9
12,326.7
1,668.7
10,250.0
6.5
-8.3
5,229.2
167.6
11,693.2
1,187.5
17,667.9
4,756.5
54,576.9
9,173.3
DQN
1,620.0
978.0
4,280.4
4,359.0
1,364.5
279,987.0
455.0
29,900.0
8,627.5
585.6
50.4
88.0
385.5
4,657.7
6,126.0
110,763.0
23,633.0
12,149.4
-6.6
729.0
-4.9
30.8
797.4
8,777.4
473.0
20,437.8
-1.9
768.5
7,259.0
8,422.3
26,059.0
0.0
3,085.6
8,207.8
8,485.2
-286.1
19.5
146.7
13,117.3
7,377.6
39,544.0
63.9
5,860.6
-13,062.3
3,482.8
1,692.3
54,282.0
-5.6
12.2
4,870.0
68.1
9,989.9
163.0
196,760.4
2,704.0
18,098.9
5,363.0
DDQN
3,747.7
1,793.3
5,393.2
17,356.5
734.7
106,056.0
1,030.6
31,700.0
13,772.8
1,225.4
68.1
91.6
418.5
5,409.4
5,809.0
117,282.0
35,338.5
58,044.2
-5.5
1,211.8
15.5
33.3
1,683.3
14,840.8
412.0
20,130.2
-2.7
1,358.0
12,992.0
7,920.5
29,710.0
0.0
2,711.4
10,616.0
12,252.5
-29.9
20.9
129.7
15,088.5
14,884.5
44,127.0
65.1
16,452.7
-9,021.8
3,067.8
2,525.5
60,142.0
-2.9
-22.8
8,339.0
218.4
22,972.2
98.0
309,941.9
7,492.0
11,712.6
10,163.0
DUEL
4,461.4
2,354.5
4,621.0
28,188.0
2,837.7
382,572.0
1,611.9
37,150.0
12,164.0
1,472.6
65.5
99.4
345.3
7,561.4
11,215.0
143,570.0
42,214.0
60,813.3
0.1
2,258.2
46.4
0.0
4,672.8
15,718.4
588.0
20,818.2
0.5
1,312.5
14,854.0
11,451.9
34,294.0
0.0
6,283.5
11,971.1
23,092.2
0.0
21.0
103.0
19,220.3
21,162.6
69,524.0
65.3
50,254.2
-8,857.4
2,250.8
6,427.3
89,238.0
4.4
5.1
11,666.0
211.4
44,939.6
497.0
98,209.5
7,855.0
49,622.1
12,944.0
PRIOR. DUEL.
3,941.0
2,296.8
11,477.0
375,080.0
1,192.7
395,762.0
1,503.1
35,520.0
30,276.5
3,409.0
46.7
98.9
366.0
7,687.5
13,185.0
162,224.0
41,324.5
72,878.6
-12.5
2,306.4
41.3
33.0
7,413.0
104,368.2
238.0
21,036.5
-0.4
812.0
1,792.0
10,374.4
48,375.0
0.0
3,327.3
15,572.5
70,324.3
0.0
20.9
206.0
18,760.3
20,607.6
62,151.0
27.5
931.6
-19,949.9
133.4
15,311.5
125,117.0
1.2
0.0
7,553.0
245.9
33,879.1
48.0
479,197.0
12,352.0
69,618.1
13,886.0
C51
3,166
1,735
7,203
406,211
1,516
841,075
976
28,742
14,074
1,645
81.8
97.8
748
9,646
15,600
179,877
47,092
130,955
2.5
3,454
8.9
33.9
3,965
33,641
440
38,874
-3.5
1,909
12,853
9,735
48,192
0.0
3,415
12,542
17,490
0.0
20.9
15,095
23,784
17,322
55,839
52.3
266,434
-13,901
8,342
5,747
49,095
6.8
23.1
8,329
280
15,612
1,520
949,604
9,300
35,050
10,513"""

mnih_2013_table_1 = """Random
Sarsa [3]
Contingency [4]
DQN
Human
HNeat Best [8]
HNeat Pixel [8]
DQN Best
B. Rider Breakout Enduro Pong Q*bert Seaquest S. Invaders
354
996
1743
4092
7456
3616
1332
5184
1.2
5.2
6
168
31
52
4
225
0
129
159
470
368
106
91
661
−20.4
−19
−17
20
−3
19
−16
21
157
614
960
1952
18900
1800
1325
4500
110
665
723
1705
28010
920
800
1740
179
271
268
581
3690
1720
1145
1075"""

van_hasselt_2016_table1 = """Game
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
Defender
Demon Attack
Double Dunk
Enduro
Fishing Derby
Freeway
Frostbite
Gopher
Gravitar
H.E.R.O.
Ice Hockey
James Bond
Kangaroo
Krull
Kung-Fu Master
Montezuma’s Revenge
Ms. Pacman
Name This Game
Phoenix
Pitfall
Pong
Private Eye
Q*Bert
River Raid
Road Runner
Robotank
Seaquest
Skiing
Solaris
Space Invaders
Star Gunner
Surround
Tennis
Time Pilot
Tutankham
Up and Down
Venture
Video Pinball
Wizard of Wor
Yars Revenge
Zaxxon
Random
227.80
5.80
222.40
210.00
719.10
12850.00
14.20
2360.00
363.90
123.70
23.10
0.10
1.70
2090.90
811.00
10780.50
2874.50
152.10
−18.60
0.00
−91.70
0.00
65.20
257.60
173.00
1027.00
−11.20
29.00
52.00
1598.00
258.50
0.00
307.30
2292.30
761.40
−229.40
−20.70
24.90
163.90
1338.50
11.50
2.20
68.40
−17098.10
1236.30
148.00
664.00
−10.00
−23.80
3568.00
11.40
533.40
0.00
16256.90
563.50
3092.90
32.50
Human
7127.70
1719.50
742.00
8503.30
47388.70
29028.10
753.10
37187.50
16926.50
2630.40
160.70
12.10
30.50
12017.00
7387.80
35829.40
18688.90
1971.00
−16.40
860.50
−38.70
29.60
4334.70
2412.50
3351.40
30826.40
0.90
302.80
3035.00
2665.50
22736.30
4753.30
6951.60
8049.00
7242.60
6463.70
14.60
69571.30
13455.00
17118.00
7845.00
11.90
42054.70
−4336.90
12326.70
1668.70
10250.00
6.50
−8.30
5229.20
167.60
11693.20
1187.50
17667.90
4756.50
54576.90
9173.30
Double DQN
3747.70
1793.30
5393.20
17356.50
734.70
106056.00
1030.60
31700.00
13772.80
1225.40
68.10
91.60
418.50
5409.40
5809.00
117282.00
35338.50
58044.20
−5.50
1211.80
15.50
33.30
1683.30
14840.80
412.00
20130.20
−2.70
1358.00
12992.00
7920.50
29710.00
0.00
2711.40
10616.00
12252.50
−29.90
20.90
129.70
15088.50
14884.50
44127.00
65.10
16452.70
−9021.80
3067.80
2525.50
60142.00
−2.90
−22.80
8339.00
218.40
22972.20
98.00
309941.90
7492.00
11712.60
10163.00
Double DQN with Pop-Art
3213.50
782.50
9011.60
18919.50
2869.30
340076.00
1103.30
8220.00
8299.40
1199.60
102.10
99.30
344.10
49065.80
775.00
119679.00
11099.00
63644.90
−11.50
2002.10
45.10
33.40
3469.60
56218.20
483.50
14225.20
−4.10
507.50
13150.00
9745.10
34393.00
0.00
4963.80
15851.20
6202.50
−2.60
20.60
286.70
5236.80
12530.80
47770.00
64.30
10932.30
−13585.10
4544.80
2589.70
589.00
−2.50
12.10
4870.00
183.90
22474.40
1172.00
56287.00
483.00
21409.50
14402.00"""

# COLUMN-ORIENTED processing

remove_re = re.compile(r"['’!\.]")
underscore_re = re.compile(r"[ \-\*]")
def game_metric_name(s):
    "Calculate the name of the Metric() object from a game's name"
    name = s.strip().lower()
    name.replace("pac_man", "pacman")  # the papers are inconsistent; "Pac-Man" is most correct but pacman most pythonic
    name = remove_re.sub("", name)
    name = underscore_re.sub("_", name)
    return name + "_metric"

verb = False # Set to True for debugging
TSIZE = 57   # Number of games reported in the more recent papers

def get_game_metric(metric_name, human_name, target, target_source):
    """Get a reference to the metric object for a game, creating it if necessary."""
    metric = globals().get(metric_name, None)
    if not metric:
        if verb: print("Creating metric for", human_name, "target: " + str(target) if target else "")
        metric = simple_games.metric("Atari 2600 " + human_name, target=target, 
                                     scale=atari_linear, target_source=target_source)
        globals()[metric_name] = metric
    return metric

def get_column(raw, n, size=TSIZE):
    assert isinstance(raw, list), "Not a list: {0}".format(type(raw))
    start_pos = n * (size + 1) # Size + headers
    name = raw[start_pos]
    data = raw[start_pos + 1:start_pos + size + 1]
    return name, data

def ingest_column(src, n, paper_url, alg=None, extras={}, size=TSIZE):
    algorithm, data = get_column(src, n, size=size)
    if verb and algorithm.lower() not in alg.lower():
        print(u"# {0} not in {1}".format(algorithm, alg))
    for i, score in enumerate(data):
        # Maybe someone should fix Python's float() function...
        score = float(score.replace(",", "").replace('\xe2\x88\x92', "-").replace("−", "-"))
        game = game_metric_name(games[i])
        metric = get_game_metric(game, games[i], targets[i], "https://arxiv.org/abs/1509.06461")
        if verb: print(u'{0}.measure(None, {1}, "{2}", url="{3}"{4})'.format(game, score, alg, paper_url, extras if extras else ""))
        metric.measure(None, score, alg, url=paper_url, **extras)


noop_data = wang_table_2.split("\n")
human_start_data = wang_table_3.split("\n")
es_data = es_table3.split("\n")
distributional_data = bellemare_figure_14.split("\n")
early_data = mnih_2013_table_1.split("\n")
pop_art_data = van_hasselt_2016_table1.split("\n")
_, games = get_column(noop_data, 0)

# Weirdly, the noop start human performance is consistently better than the human start human performance data
# Is this because it's newer and at a higher standard? Or because the recorded human starts consistently hamper strong
# human play?
_, human_noop = get_column(noop_data, 3)
human_noop = [float(score.replace(",", "")) for score in human_noop]
_, human_human = get_column(human_start_data, 3)
human_human = [float(score.replace(",", "")) for score in human_human]
targets = [max(scores) for scores in zip(human_noop, human_human)]

ingest_column(early_data, 2, "https://arxiv.org/abs/1312.5602", u"SARSA(λ)", 
              {"algorithm_src_url": "https://arxiv.org/abs/1207.4708v1"}, size=7)
ingest_column(es_data, 3, "https://arxiv.org/abs/1703.03864v1", "ES FF (1 hour) noop", size=51)
ingest_column(distributional_data, 7, "https://arxiv.org/abs/1707.06887v1", "C51 noop")
ingest_column(pop_art_data, 4, "https://arxiv.org/abs/1602.07714v1", "DDQN+Pop-Art noop")

ingest_column(noop_data, 4, "https://arxiv.org/abs/1509.06461v1", "DQN noop", 
              {"algorithm_src_url": "https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf",
               "min_date": date(2015, 2, 26)})
ingest_column(human_start_data, 4, "https://arxiv.org/abs/1509.06461v1", "DQN hs", 
              {"algorithm_src_url": "https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf",
               "min_date": date(2015, 2, 26)})
# v1 of the DDQN paper reported only "untuned" results
# TODO import those "untuned" results. May require OCR due to missing table columns...

# v3 of that paper added "tuned" results for the hs condition

# However this (presumably tuned) DDQN noop data is included by Wang et al but seems NOT to be in the DDQN paper.
# Conjecture, did Wang et al first report it?
ingest_column(noop_data, 5, "https://arxiv.org/abs/1511.06581v1", "DDQN (tuned) noop",
              {"algorithm_src_url": "https://arxiv.org/abs/1509.06461v3"}) 

ingest_column(human_start_data, 5, "https://arxiv.org/abs/1509.06461v3", alg="DDQN (tuned) hs")
ingest_column(noop_data, 6, "https://arxiv.org/abs/1511.06581v1", alg="Duel noop")
ingest_column(human_start_data, 6, "https://arxiv.org/abs/1511.06581v1", alg="Duel hs")
ingest_column(noop_data, 7, "https://arxiv.org/abs/1511.05952", alg="Prior noop")
ingest_column(human_start_data, 7, "https://arxiv.org/abs/1511.05952", alg="Prior hs")
ingest_column(noop_data, 8, "https://arxiv.org/abs/1511.06581v3", "Prior+Duel noop", 
              {"algorithm_src_url":"https://arxiv.org/abs/1511.05952"})
ingest_column(human_start_data, 8, "https://arxiv.org/abs/1509.06461v3", "Prior+Duel hs", 
              {"algorithm_src_url":"https://arxiv.org/abs/1511.05952"})

# ROW-ORIENTED DATA

# The row parsers are harder and need to be customized per table, essentially

# OCR output:
mnih_extended_table_2 = """Game	Random Play	Best Linear Learner	Contingency (SARSA)	Human	DQN (± std)	Normalized DQN (% Human)
Alien	227.8	939.2	103.2	6875	3069 (±1093)	42.7%
Amidar	5.8	103.4	183.6	1676	739.5 (±3024)	43.9%
Assault	222.4	628	537	1496	3359 (±775)	246.2%
Asterix	210	987.3	1332	8503	6012 (±1744)	70.0%
Asteroids	719.1	907.3	89	13157	1629 (±542)	7.3%
Atlantis	12850	62687	852.9	29028	85641 (±17600)	449.9%
Bank Heist	14.2	190.8	67.4	734.4	429.7 (±650)	57.7%
Battle Zone	2360	15820	16.2	37800	26300 (±7725)	67.6%
Beam Rider	363.9	929.4	1743	5775	6846 (±1619)	119.8%
Bowling	23.1	43.9	36.4	154.8	42.4 (±88)	14.7%
Boxing	0.1	44	9.8	4.3	71.8 (±8.4)	1707.9%
Breakout	1.7	5.2	6.1	31.8	401.2 (±26.9)	1327.2%
Centipede	2091	8803	4647	11963	8309 (±5237)	63.0%
Chopper Command	811	1582	16.9	9882	6687 (±2916)	64.8%
Crazy Climber	10781	23411	149.8	35411	114103 (±22797)	419.5%
Demon Attack	152.1	520.5	0	3401	9711 (±2406)	294.2%
Double Dunk	-18.6	-13.1	-16	-15.5	-18.1 (±2.6)	17.1%
Enduro	0	129.1	159.4	309.6	301.8 (±24.6)	97.5%
Fishing Derby	-91.7	-89.5	-85.1	5.5	-0.8 (±19.0)	93.5%
Freeway	0	19.1	19.7	29.6	30.3 (±0.7)	102.4%
Frostbite	65.2	216.9	180.9	4335	328.3 (±250.5)	6.2%
Gopher	257.6	1288	2368	2321	8520 (±3279)	400.4%
Gravitar	173	387.7	429	2672	306.7 (±223.9)	5.3%
H.E.R.O.	1027	6459	7295	25763	19950 (±158)	76.5%
Ice Hockey	-11.2	-9.5	-3.2	0.9	-1.6 (±2.5)	79.3%
James Bond	29	202.8	354.1	406.7	576.7 (±175.5)	145.0%
Kangaroo	52	1622	8.8	3035	6740 (±2959)	224.2%
Krull	1598	3372	3341	2395	3805 (±1033)	277.0%
Kung-Fu Master	258.5	19544	29151	22736	23270 (±5955)	102.4%
Montezuma's Revenge	0	10.7	259	4367	0 (±0)	0.0%
Ms. Pacman	307.3	1692	1227	15693	2311 (±525)	13.0%
Name This Game	2292	2500	2247	4076	7257 (±547)	278.3%
Pong	-20.7	-19	-17.4	9.3	18.9 (±1.3)	132.0%
Private Eye	24.9	684.3	86	69571	1788 (±5473)	2.5%
Q*Bert	163.9	613.5	960.3	13455	10596 (±3294)	78.5%
River Raid	1339	1904	2650	13513	8316 (±1049)	57.3%
Road Runner	11.5	67.7	89.1	7845	18257 (±4268)	232.9%
Robotank	2.2	28.7	12.4	11.9	51.6 (±4.7)	509.0%
Seaquest	68.4	664.8	675.5	20182	5286 (±1310)	25.9%
Space Invaders	148	250.1	267.9	1652	1976 (±893)	121.5%
Star Gunner	664	1070	9.4	10250	57997 (±3152)	598.1%
Tennis	-23.8	-0.1	0	-8.9	-2.5 (±1.9)	143.2%
Time Pilot	3568	3741	24.9	5925	5947 (±1600)	100.9%
Tutankham	11.4	114.3	98.2	167.6	186.7 (±41.9)	112.2%
Up and Down	533.4	3533	2449	9082	8456 (±3162)	92.7%
Venture	0	66	0.6	1188	380 (±238.6)	32.0%
Video Pinball	16257	16871	19761	17298	42684 (±16287)	2539.4%
Wizard of Wor	563.5	1981	36.9	4757	3393 (±2019)	67.5%
Zaxxon	32.5	3365	21.4	9173	4977 (±1235)	54.1%"""

nature_rows = mnih_extended_table_2.split("\n")[1:]
name_re = re.compile(r'[^0-9\t]+')
for row in nature_rows:
    match = name_re.match(row)
    game = game_metric_name(match.group(0))
    rest = name_re.sub("", row, 1)
    cols = rest.split()
    random, bll, sarsa, human, dqn, dqn_err, norm = cols
    dqn = float(dqn)
    dqn_err = float(re.search("[0-9]+", dqn_err).group(0))
    globals()[game].measure(date(2015, 2, 26), dqn, 'Nature DQN', 
        url='https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf', 
        papername="Human-level control through deep reinforcement learning", 
        uncertainty=dqn_err)
    if verb:
        print("{0}.measure(None, {1}, 'Nature DQN', papername='Human-level control through deep reinforcement learning' "
              "url='https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf'"
              ", uncertainty={2})".format(game, dqn, dqn_err))


a3c_table_s3 = """Game	DQN	Gorila	Double	Dueling	Prioritized	A3C FF, 1 day	A3C FF	A3C LSTM
Alien	570.2	813.5	1033.4	1486.5	900.5	182.1	518.4	945.3
Amidar	133.4	189.2	169.1	172.7	218.4	283.9	263.9	173.0
Assault	3332.3	1195.8	6060.8	3994.8	7748.5	3746.1	5474.9	14497.9
Asterix	124.5	3324.7	16837.0	15840.0	31907.5	6723.0	22140.5	17244.5
Asteroids	697.1	933.6	1193.2	2035.4	1654.0	3009.4	4474.5	5093.1
Atlantis	76108.0	629166.5	319688.0	445360.0	593642.0	772392.0	911091.0	875822.0
Bank Heist	176.3	399.4	886.0	1129.3	816.8	946.0	970.1	932.8
Battle Zone	17560.0	19938.0	24740.0	31320.0	29100.0	11340.0	12950.0	20760.0
Beam Rider	8672.4	3822.1	17417.2	14591.3	26172.7	13235.9	22707.9	24622.2
Berzerk			1011.1	910.6	1165.6	1433.4	817.9	862.2
Bowling	41.2	54.0	69.6	65.7	65.8	36.2	35.1	41.8
Boxing	25.8	74.2	73.5	77.3	68.6	33.7	59.8	37.3
Breakout	303.9	313.0	368.9	411.6	371.6	551.6	681.9	766.8
Centipede	3773.1	6296.9	3853.5	4881.0	3421.9	3306.5	3755.8	1997.0
Chopper Command	3046.0	3191.8	3495.0	3784.0	6604.0	4669.0	7021.0	10150.0
Crazy Climber	50992.0	65451.0	113782.0	124566.0	131086.0	101624.0	112646.0	138518.0
Defender			27510.0	33996.0	21093.5	36242.5	56533.0	233021.5
Demon Attack	12835.2	14880.1	69803.4	56322.8	73185.8	84997.5	113308.4	115201.9
Double Dunk	-21.6	-11.3	-0.3	-0.8	2.7	0.1	-0.1	0.1
Enduro	475.6	71.0	1216.6	2077.4	1884.4	-82.2	-82.5	-82.5
Fishing Derby	-2.3	4.6	3.2	-4.1	9.2	13.6	18.8	22.6
Freeway	25.8	10.2	28.8	0.2	27.9	0.1	0.1	0.1
Frostbite	157.4	426.6	1448.1	2332.4	2930.2	180.1	190.5	197.6
Gopher	2731.8	4373.0	15253.0	20051.4	57783.8	8442.8	10022.8	17106.8
Gravitar	216.5	538.4	200.5	297.0	218.0	269.5	303.5	320.0
H.E.R.O.	12952.5	8963.4	14892.5	15207.9	20506.4	28765.8	32464.1	28889.5
Ice Hockey	-3.8	-1.7	-2.5	-1.3	-1.0	-4.7	-2.8	-1.7
James Bond	348.5	444.0	573.0	835.5	3511.5	351.5	541.0	613.0
Kangaroo	2696.0	1431.0	11204.0	10334.0	10241.0	106.0	94.0	125.0
Krull	3864.0	6363.1	6796.1	8051.6	7406.5	8066.6	5560.0	5911.4
Kung-Fu Master	11875.0	20620.0	30207.0	24288.0	31244.0	3046.0	28819.0	40835.0
Montezuma’s Revenge	50.0	84.0	42.0	22.0	13.0	53.0	67.0	41.0
Ms. Pacman	763.5	1263.0	1241.3	2250.6	1824.6	594.4	653.7	850.7
Name This Game	5439.9	9238.5	8960.3	11185.1	11836.1	5614.0	10476.1	12093.7
Phoenix			12366.5	20410.5	27430.1	28181.8	52894.1	74786.7
Pit Fall			-186.7	-46.9	-14.8	-123.0	-78.5	-135.7
Pong	16.2	16.7	19.1	18.8	18.9	11.4	5.6	10.7
Private Eye	298.2	2598.6	-575.5	292.6	179.0	194.4	206.9	421.1
Q*Bert	4589.8	7089.8	11020.8	14175.8	11277.0	13752.3	15148.8	21307.5
River Raid	4065.3	5310.3	10838.4	16569.4	18184.4	10001.2	12201.8	6591.9
Road Runner	9264.0	43079.8	43156.0	58549.0	56990.0	31769.0	34216.0	73949.0
Robotank	58.5	61.8	59.1	62.0	55.4	2.3	32.8	2.6
Seaquest	2793.9	10145.9	14498.0	37361.6	39096.7	2300.2	2355.4	1326.1
Skiing			-11490.4	-11928.0	-10852.8	-13700.0	-10911.1	-14863.8
Solaris			810.0	1768.4	2238.2	1884.8	1956.0	1936.4
Space Invaders	1449.7	1183.3	2628.7	5993.1	9063.0	2214.7	15730.5	23846.0
Star Gunner	34081.0	14919.2	58365.0	90804.0	51959.0	64393.0	138218.0	164766.0
Surround			1.9	4.0	-0.9	-9.6	-9.7	-8.3
Tennis	-2.3	-0.7	-7.8	4.4	-2.0	-10.2	-6.3	-6.4
Time Pilot	5640.0	8267.8	6608.0	6601.0	7448.0	5825.0	12679.0	27202.0
Tutankham	32.4	118.5	92.2	48.0	33.6	26.1	156.3	144.2
Up and Down	3311.3	8747.7	19086.9	24759.2	29443.7	54525.4	74705.7	105728.7
Venture	54.0	523.4	21.0	200.0	244.0	19.0	23.0	25.0
Video Pinball	20228.1	112093.4	367823.7	110976.2	374886.9	185852.6	331628.1	470310.5
Wizard of Wor	246.0	10431.0	6201.0	7054.0	7451.0	5278.0	17244.0	18082.0
Yars Revenge			6270.6	25976.5	5965.1	7270.8	7157.5	5615.5
Zaxxon	831.0	6159.4	8593.0	10164.0	9501.0	2659.0	24622.0	23519.0"""

# Caption:
# Table S3. Raw scores for the human start condition (30 minutes emulator time). DQN scores taken from (Nair et al.,
# 2015). Double DQN scores taken from (Van Hasselt et al., 2015), Dueling scores from (Wang et al., 2015) and
# Prioritized scores taken from (Schaul et al., 2015)

a3c_rows = a3c_table_s3.split("\n")[1:]
for row in a3c_rows:
    cols = row.split("\t")
    game, dqn, gorila, ddqn, duel, prior, a3c_ff_1, a3c_ff, a3c_lstm = cols
    game1 = game_metric_name(game)
    metric = get_game_metric(game1, game, None, None)
    for alg, score in [("A3C FF (1 day) hs", a3c_ff_1), ("A3C FF hs", a3c_ff), ("A3C LSTM hs", a3c_lstm)]:
        score = float(score)
        metric.measure(None, score, alg, url="https://arxiv.org/abs/1602.01783")
        if verb: print('{0}.measure(None, {1}, "{2}", url="{3}")'.format(game1, score, alg, "https://arxiv.org/abs/1602.01783"))

    try:
        score = float(gorila)
        metric.measure(None, score, "Gorila", url="https://arxiv.org/abs/1507.04296")
        if verb: print('{0}.measure(None, {1}, "Gorila", url="{2}")'.format(game1, score, "https://arxiv.org/abs/1507.04296"))
    except ValueError:
        if verb: print("No Gorila score for", game)

# vim: set list:listchars=tab:!·,trail:·
