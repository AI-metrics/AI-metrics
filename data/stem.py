from taxonomy import Problem
from scales import *
import datetime
date = datetime.date

read_stem_papers = Problem("Read a scientific or technical paper, and comprehend its contents", ["language", "world-modelling", "super"])

# Getting some major results from an abstract, tables or conclusion is much easier than understanding the entire paper, its assumptions, robustness, support for its claims, etc
extract_results = Problem("Extract major numerical results or progress claims from a STEM paper", ["language", "world-modelling", "agi"])
read_stem_papers.add_subproblem(extract_results)

extract_results.metric("Automatically find new relevant ML results on arXiv")
extract_results.notes = """
This metric is the ability to automatically update the ipython Notebook you are reading by spotting results in pdfs uploaded to arxiv.org.
Pull requests demonstrating solutions are welcome :)
"""

solve_technical_problems = Problem("Given an arbitrary technical problem, solve it as well as a typical professional in that field", ["language", "world-modelling"])

program_induction = Problem("Writing software from specifications")
solve_technical_problems.add_subproblem(program_induction)
program_induction.metric("Card2Code", url="https://github.com/deepmind/card2code", scale=correct_percent)

vaguely_constrained_technical_problems = Problem("Solve vaguely or under-constrained technical problems")
solve_technical_problems.add_subproblem(vaguely_constrained_technical_problems)

# This subset of technical problems is much easier; here we assume that a human / worldly problem has been reduced to something that can be
# subjected to clear computational evaluation ("is this purported proof of theorem X correct?", "does this circuit perform task Y efficiently?"
# "will this airframe fly with reasonable characteristics?")
solve_constrained_technical_problems = Problem("Solve technical problems with clear constraints (proofs, circuit design, aerofoil design, etc)")
solve_technical_problems.add_subproblem(solve_constrained_technical_problems)
vaguely_constrained_technical_problems.add_subproblem(read_stem_papers)

# Note that this theorem proving problem (learning to prove theorems) is a little different from the pure search
# through proof space that characterises the classic ATP field, though progress there may also be interesting
theorem_proving = Problem("Given examples of proofs, find correct proofs of simple mathematical theorems", ["agi", "math"])
circuit_design = Problem("Given desired circuit characteristics, and many examples, design new circuits to spec", ["agi", "math"])
solve_constrained_technical_problems.add_subproblem(theorem_proving)
theorem_proving.metric("HolStep", url="https://arxiv.org/abs/1703.00426")
solve_constrained_technical_problems.add_subproblem(circuit_design)

# TODO: find well-defined metrics for some of these problems in the literature. Or create some!
# Some relevant papers:
# http://www.ise.bgu.ac.il/faculty/kalech/publications/ijcai13.pdf
# https://www.researchgate.net/publication/2745078_Use_of_Automatically_Defined_Functions_and_ArchitectureAltering_Operations_in_Automated_Circuit_Synthesis_with_Genetic_Programming
# https://link.springer.com/article/10.1007/s10817-014-9301-5

program_induction = Problem("Write computer programs from specifications")
vaguely_constrained_technical_problems.add_subproblem(program_induction)
card2code_mtg_acc = program_induction.metric("Card2Code MTG accuracy", url="https://github.com/deepmind/card2code", scale=correct_percent, target=100, target_label="Bug-free card implementation")
card2code_hs_acc = program_induction.metric("Card2Code Hearthstone accuracy", url="https://github.com/deepmind/card2code", scale=correct_percent, target=100, target_label="Bug-free card implementation")

card2code_mtg_acc.measure(None, 4.8, "LPN", url="https://arxiv.org/abs/1603.06744v1")
card2code_hs_acc.measure(None, 6.1, "LPN", url="https://arxiv.org/abs/1603.06744v1")
card2code_hs_acc.measure(None, 13.6, "Seq2Tree-Unk", url="https://arxiv.org/abs/1704.01696v1", algorithm_src_url="https://arxiv.org/abs/1601.01280v1")
card2code_hs_acc.measure(None, 1.5, "NMT", url="https://arxiv.org/abs/1704.01696v1", algorithm_src_url="https://arxiv.org/abs/1409.0473v1")
#card2code_hs_acc.measure(None, 16.2, "SNM", url="https://arxiv.org/abs/1704.01696v1")
card2code_hs_acc.measure(None, 16.7, "SNM -frontier embed", url="https://arxiv.org/abs/1704.01696v1")

understand_conditional_expressions = Problem("Parse and implement complex conditional expressions")
program_induction.add_subproblem(understand_conditional_expressions)

science_question_answering = Problem("Answering Science Exam Questions", ["science", "qa"])
vaguely_constrained_technical_problems.add_subproblem(science_question_answering)

ny_4_science = science_question_answering.metric("NY Regents 4th Grade Science Exams", url="http://www.nysedregents.org/Grade4/Science/home.html", scale=correct_percent, target=100,
target_label="Perfect score")
ny_4_science.measure(None, 47.5, "Praline", url="https://pdfs.semanticscholar.org/478b/4a5123bd5fda98bb35e6317d7f3555fec97d.pdf", papername="Combining Retrieval, Statistics, and Inference to Answer Elementary Science Questions", venue="AAAI 2016", algorithm_src_url="http://aclweb.org/anthology/D15-1080", min_date=date(2015, 11, 17))
ny_4_science.measure(None, 60.7, "PMI", "https://pdfs.semanticscholar.org/478b/4a5123bd5fda98bb35e6317d7f3555fec97d.pdf", papername="Combining Retrieval, Statistics, and Inference to Answer Elementary Science Questions", venue="AAAI 2016")
ny_4_science.measure(None, 60.6, "IR", "https://pdfs.semanticscholar.org/478b/4a5123bd5fda98bb35e6317d7f3555fec97d.pdf", papername="Combining Retrieval, Statistics, and Inference to Answer Elementary Science Questions", venue="AAAI 2016")
ny_4_science.measure(None, 55.4, "SVM", "https://pdfs.semanticscholar.org/478b/4a5123bd5fda98bb35e6317d7f3555fec97d.pdf", papername="Combining Retrieval, Statistics, and Inference to Answer Elementary Science Questions", venue="AAAI 2016")
ny_4_science.measure(None, 54.3, "RULE", "https://pdfs.semanticscholar.org/478b/4a5123bd5fda98bb35e6317d7f3555fec97d.pdf", papername="Combining Retrieval, Statistics, and Inference to Answer Elementary Science Questions", venue="AAAI 2016")
ny_4_science.measure(None, 43.8, "ILP", "https://pdfs.semanticscholar.org/478b/4a5123bd5fda98bb35e6317d7f3555fec97d.pdf", papername="Combining Retrieval, Statistics, and Inference to Answer Elementary Science Questions", venue="AAAI 2016")
ny_4_science.measure(None, 71.3, "Aristo (ALL)", "https://pdfs.semanticscholar.org/478b/4a5123bd5fda98bb35e6317d7f3555fec97d.pdf", papername="Combining Retrieval, Statistics, and Inference to Answer Elementary Science Questions", venue="AAAI 2016")
ny_4_science.measure(None, 61.5, "TableILP", "https://arxiv.org/pdf/1604.06076.pdf")
ny_4_science.measure(None, 69.0, "TableILP+IR+PMI", "https://arxiv.org/pdf/1604.06076.pdf")

elementery_ndmc_acc = science_question_answering.metric("Elementery Non-Diagram Multiple Choice (NDMC) Science Exam accuracy", 
    url="http://data.allenai.org/ai2-science-questions/", scale=correct_percent, target=100, target_label="Perfect Score")

elementery_dmc_acc = science_question_answering.metric("Elementery Diagram Multiple Choice (DMC) Science Exam accuracy", 
    url="http://data.allenai.org/ai2-science-questions/", scale=correct_percent, target=100, target_label="Perfect Score")

ms_ndmc_acc = science_question_answering.metric("Middle School Non-Diagram Multiple Choice (NDMC) Science Exam accuracy", 
    url="http://data.allenai.org/ai2-science-questions/", scale=correct_percent, target=100, target_label="Perfect Score")

ms_dmc_acc = science_question_answering.metric("Middle School Diagram Multiple Choice (DMC) Science Exam accuracy", 
    url="http://data.allenai.org/ai2-science-questions/", scale=correct_percent, target=100, target_label="Perfect Score")
