from taxonomy import Problem
from scales import *
import datetime
date = datetime.date

abstract_strategy_games = Problem("Abstract strategy games", ["agi", "abstract-games"])

playing_with_hints = Problem("Playing abstract games with extensive hints", ["abstract-games"], solved=True)
abstract_strategy_games.add_subproblem(playing_with_hints)
playing_with_hints.notes = """
  Complex abstract strategy games have been solved to super-human levels
  by computer systems with extensive rule-hinting and heuristics,
  in some cases combined with machine learning techniques.
"""
computer_chess = playing_with_hints.metric("Computer Chess", scale=elo, target=2882, target_label="Best human play", target_source="https://en.wikipedia.org/w/index.php?title=Comparison_of_top_chess_players_throughout_history&oldid=777500496#Elo_system")
computer_go = playing_with_hints.metric("Computer Go", scale=elo, target=3632, target_label="Best human play", target_source="https://www.goratings.org/en/history/")
computer_go.solved = True # until we get proper data

# For some caveats, see https://en.wikipedia.org/w/index.php?title=Chess_engine&oldid=764341963#Ratings
# We could script ingestion of data from CCRL, or get data from Katja
computer_chess.measure(date(1997,05,11), 2725, "Deep Blue", uncertainty=25, url="https://www.quora.com/What-was-Deep-Blues-Elo-rating")
computer_chess.measure(date(2006,05,27), 2995, "Rybka 1.1 64bit", uncertainty=25, url="https://web.archive.org/web/20060531091049/http://www.computerchess.org.uk/ccrl/4040/rating_list_all.html")
computer_chess.measure(date(2010,8,7), 3269, "Rybka 4 64bit", uncertainty=22, url="https://web.archive.org/web/20100923131123/http://www.computerchess.org.uk/ccrl/4040/rating_list_all.html")
computer_chess.measure(date(2013,7,20), 3248, "Houdini 3 64bit", uncertainty=16, url="https://web.archive.org/web/20130415000000*/http://www.computerchess.org.uk/ccrl/4040/rating_list_all.html")
computer_chess.measure(date(2015,7,4), 3332, "Komodo 9", uncertainty=24, url="https://web.archive.org/web/20150708104805/http://www.computerchess.org.uk/ccrl/4040/rating_list_all.html")
computer_chess.measure(date(2017,02,27), 3393, "Stockfish", uncertainty=50, url="https://web.archive.org/web/20170227044521/http://www.computerchess.org.uk/ccrl/4040/")
# Wikipedia has some nice data here:
computer_chess.measure(date(1984,12,31), 1631, "Novag Super Constellation 6502 4 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1985,12,31), 1827, "Mephisto Amsterdam 68000 12 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1986,12,31), 1827, "Mephisto Amsterdam 68000 12 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1987,12,31), 1923, "Mephisto Dallas 68020 14 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1988,12,31), 1993, "Mephisto MM 4 Turbo Kit 6502 16 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1989,12,31), 2027, "Mephisto Portorose 68020 12 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1990,12,31), 2138, "Mephisto Portorose 68030 36 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1991,12,31), 2127, "Mephisto Vancouver 68030 36 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1992,12,31), 2174, "Chess Machine Schroder 3.0 ARM2 30 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1993,12,31), 2235, "Mephisto Genius 2.0 486/50-66 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1995,12,31), 2306, "MChess Pro 5.0 Pentium 90 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1996,12,31), 2337, "Rebel 8.0 Pentium 90 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1997,12,31), 2418, "HIARCS 6.0 49MB P200 MMX", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1998,12,31), 2460, "Fritz 5.0 PB29% 67MB P200 MMX", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(1999,12,31), 2594, "Chess Tiger 12.0 DOS 128MB K6-2 450 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2000,12,31), 2607, "Fritz 6.0 128MB K6-2 450 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2001,12,31), 2709, "Chess Tiger 14.0 CB 256MB Athlon 1200", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2002,12,31), 2759, "Deep Fritz 7.0 256MB Athlon 1200 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2003,12,31), 2791, "Shredder 7.04 UCI 256MB Athlon 1200 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2004,12,31), 2800, "Shredder 8.0 CB 256MB Athlon 1200 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2005,12,31), 2808, "Shredder 9.0 UCI 256MB Athlon 1200 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2006,12,31), 2902, "Rybka 1.2 256MB Athlon 1200 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2007,12,31), 2935, "Rybka 2.3.1 Arena 256MB Athlon 1200 MHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2008,12,31), 3238, "Deep Rybka 3 2GB Q6600 2.4 GHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2009,12,31), 3232, "Deep Rybka 3 2GB Q6600 2.4 GHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2010,12,31), 3227, "Deep Rybka 3 2GB Q6600 2.4 GHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2011,12,31), 3216, "Deep Rybka 4 2GB Q6600 2.4 GHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2012,12,31), 3221, "Deep Rybka 4 x64 2GB Q6600 2.4 GHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2013,12,31), 3241, "Komodo 5.1 MP x64 2GB Q6600 2.4 GHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2014,12,31), 3295, "Komodo 7.0 MP x64 2GB Q6600 2.4 GHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2015,12,31), 3334, "Stockfish 6 MP x64 2GB Q6600 2.4 GHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")
computer_chess.measure(date(2016,12,31), 3366, "Komodo 9.1 MP x64 2GB Q6600 2.4 GHz", url="https://en.wikipedia.org/wiki/Swedish_Chess_Computer_Association#Rating_list_year-end_leaders")

mastering_historical_games = Problem("Superhuman mastery of arbitrary abstract strategy games", ["super", "abstract-games"])
abstract_strategy_games.add_subproblem(mastering_historical_games)
mastering_chess = mastering_historical_games.metric("mastering chess")
mastering_chess.notes = """
  Beating all humans at chess, given a corpus of past play amongst masters,
  but no human-crafted policy constraints and heuristics. This will probably fall out
  immediately once learning_abstract_game_rules is solved, since playing_with_hints
  has been solved.
"""

# Are there any published metrics for these yet?
learning_abstract_game_rules = Problem("Learning the rules of complex strategy games from examples", ["agi", "abstract-games"])
abstract_strategy_games.add_subproblem(learning_abstract_game_rules)
learning_chess = learning_abstract_game_rules.metric("learning chess")
learning_chess.notes = """
  Chess software contains hard-coded policy constraints for valid play; this metric is whether RL
  or other agents can correctly build those policy constraints from examples or oracles"""
learning_go = learning_abstract_game_rules.metric("learning go")
learning_go.notes = """
  Go software contains policy constraints for valid play and evaluating the number of
  liberties for groups. This metric is whether RL or other agents can correctly build those 
  policy constraints from examples or oracles"""

learning_arbitrary_abstract_games = Problem("Play an arbitrary abstract game, first learning the rules", ["agi", "abstract-games"])
abstract_strategy_games.add_subproblem(learning_arbitrary_abstract_games)
computer_chess.graph()



