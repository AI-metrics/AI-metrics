from taxonomy import Problem
from scales import *
import datetime
date = datetime.date

print "in data/language, name is ", __name__

turing_test = Problem("Conduct arbitrary sustained, probing conversation", ["agi", "language", "world-modelling", "communication"])
easy_turing_test = Problem("Turing test for casual conversation", ["agi", "language", "world-modelling", "communication"])
turing_test.add_subproblem(easy_turing_test)

loebner = easy_turing_test.metric("The Loebner Prize scored selection answers", url="http://www.aisb.org.uk/events/loebner-prize", 
                                  scale=correct_percent, changeable=True, target=100, target_label="Completely plausible answers",
                                axis_label='Percentage of answers rated plausible\n(each year is a different test)')
# XXX humans probably don't get 100% on the Loebner Prize selection questions; we should ask the organizers to score
# some humans


loebner.notes = """
The Loebner Prize is an actual enactment of the Turing Test. Importantly, judges are instructed to engage in casual, natural
conversation rather than deliberately probing to determine if participants are "intelligent" (Brian Christian, The Most Human Human).
This makes it considerably easier than a probing Turing Test, and it is close to being solved. 

However these aren't scores for the full Loebner Turing Test; since 2014 the Loebner prize has scored its entrants by
giving them a corpus of conversation and scoring their answers. We use these numbers because they remove variability
in the behaviour of the judges. Unfortunately, these questions change from year to year (and have to, since 
entrants will test with last year's data).
"""
loebner.measure(date(2016,9,17), 90, "Mitsuku 2016", url="http://www.aisb.org.uk/events/loebner-prize#Results16")
loebner.measure(date(2016,9,17), 78.3, "Tutor 2016", url="http://www.aisb.org.uk/events/loebner-prize#Results16")
loebner.measure(date(2016,9,17), 77.5, "Rose 2016", url="http://www.aisb.org.uk/events/loebner-prize#Results16")
loebner.measure(date(2016,9,17), 77.5, "Arckon 2016", url="http://www.aisb.org.uk/events/loebner-prize#Results16")
loebner.measure(date(2016,9,17), 76.7, "Katie 2016", url="http://www.aisb.org.uk/events/loebner-prize#Results16")

loebner.measure(date(2015,9,19), 83.3, "Mitsuku 2015", url="http://www.aisb.org.uk/events/loebner-prize#Results15")
loebner.measure(date(2015,9,19), 80, "Lisa 2015", url="http://www.aisb.org.uk/events/loebner-prize#Results15")
loebner.measure(date(2015,9,19), 76.7, "Izar 2015", url="http://www.aisb.org.uk/events/loebner-prize#Results15")
loebner.measure(date(2015,9,19), 75, "Rose 2015",url="http://www.aisb.org.uk/events/loebner-prize#Results15")

loebner.measure(date(2014,11,15), 89.2, "Rose 2014", url="http://www.aisb.org.uk/events/loebner-prize#contest2014")
loebner.measure(date(2014,11,15), 88.3, "Izar 2014", url="http://www.aisb.org.uk/events/loebner-prize#contest2014")
loebner.measure(date(2014,11,15), 88.3, "Misuku 2014", url="http://www.aisb.org.uk/events/loebner-prize#contest2014")
loebner.measure(date(2014,11,15), 81.67, "Uberbot 2014", url="http://www.aisb.org.uk/events/loebner-prize#contest2014")
loebner.measure(date(2014,11,15), 80.83, "Tutor 2014", url="http://www.aisb.org.uk/events/loebner-prize#contest2014")
loebner.measure(date(2014,11,15), 76.7, "The Professor 2014", url="http://www.aisb.org.uk/events/loebner-prize#contest2014")

reading_comprehension = Problem("Language comprehension and question-answering", ["language", "world-modelling", "agi"])
turing_test.add_subproblem(reading_comprehension)

# Overview of Machine Reading Comprehension (MRC) datasets here:
# http://eric-yuan.me/compare-popular-mrc-datasets/

bAbi10k = reading_comprehension.metric("bAbi 20 QA (10k training examples)", url="http://fb.ai/babi", scale=correct_percent, target=99, target_label="Excellent performance")
bAbi1k = reading_comprehension.metric("bAbi 20 QA (1k training examples)", url="http://fb.ai/babi", scale=correct_percent, target=99, target_label="Excellent performance")

bAbi1k.notes = """
A synthetic environment inspired by text adventures and SHRDLU, which enables generation
of ground truths, describing sentences, and inferential questions. Includes:
supporting facts, relations, yes/no questions, counting, lists/sets, negation, indefiniteness,
conference, conjunction, time, basic deduction and induction, reasoning about position, size,
path finding and motivation.

Table 3 of https://arxiv.org/abs/1502.05698 actually breaks this down into 20 submeasures
but initially we're lumping all of this together.

Originally "solving" bABI was defined as 95% accuracy (or perhaps) 95% accuracy on all submeasures,
but clearly humans and now algorithms are better than that.

TODO: bAbi really needs to be decomposed into semi-supervised and unsupervised variants, and 
by amount of training data provided
"""
bAbi10k.measure(date(2015,2,19), 93.3, "MemNN-AM+NG+NL (1k + strong supervision)", "https://arxiv.org/abs/1502.05698v1", not_directly_comparable=True, long_label=True) # not literally a 10K example, but more comparable to it

#bAbi1k.measure(None, 48.7, "LSTM", "https://arxiv.org/abs/1502.05698v1", algorithm_src_url="http://isle.illinois.edu/sst/meetings/2015/hochreiter-lstm.pdf", min_date=date(1997,11,15))
bAbi1k.measure(date(2015,3,31), 86.1, "MemN2N-PE+LS+RN", "https://arxiv.org/abs/1503.08895")
bAbi10k.measure(date(2015,3,31), 93.4, "MemN2N-PE+LS+RN", "https://arxiv.org/abs/1503.08895")
bAbi1k.measure(date(2015,6,24), 93.6, "DMN", "https://arxiv.org/abs/1506.07285") # The paper doesn't say if this is 1k or 10k, but seems like 1k
bAbi10k.measure(date(2016,1,5), 96.2, "DNC", "https://www.gwern.net/docs/2016-graves.pdf")

bAbi10k.measure(date(2016,9,27), 97.1, "SDNC", "https://arxiv.org/abs/1606.04582v4")
bAbi10k.measure(date(2016,12,12), 99.5, "EntNet", "https://arxiv.org/abs/1612.03969")
bAbi1k.measure(date(2016,12,12), 89.1, "EntNet", "https://arxiv.org/abs/1612.03969")

bAbi10k.measure(date(2016,12,9),  99.7, "QRN", "https://arxiv.org/abs/1606.04582v4")
bAbi1k.measure(date(2016,12,9),  90.1, "QRN", "https://arxiv.org/abs/1606.04582v4")
bAbi1k.measure(None, 66.8, "DMN+", "https://arxiv.org/abs/1606.04582v4", algorithm_src_url="https://arxiv.org/abs/1607.00036", replicated="https://github.com/therne/dmn-tensorflow")
bAbi10k.measure(date(2016,6,30),  97.2, "DMN+", "https://arxiv.org/abs/1607.00036")

# More papers:
# https://www.aclweb.org/anthology/D/D13/D13-1020.pdf


mctest160 = reading_comprehension.metric("Reading comprehension MCTest-160-all", scale=correct_percent, url="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/MCTest_EMNLP2013.pdf")
mctest160.measure(date(2013, 10, 1), 69.16, "SW+D+RTE", url="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/MCTest_EMNLP2013.pdf", papername="MCTest: A Challenge Dataset for the Open-Domain Machine Comprehension of Text")
mctest160.measure(date(2015, 7, 26), 75.27, "Wang-et-al", url="http://arxiv.org/abs/1603.08884")
mctest160.measure(date(2015, 7, 26), 73.27, "Narasimhan-model3", url="https://people.csail.mit.edu/regina/my_papers/MCDR15.pdf", papername="Machine Comprehension with Discourse Relations")
mctest160.measure(date(2016, 3, 29), 74.58, "Parallel-Hierarchical", url="http://arxiv.org/abs/1603.08884")

mctest500 = reading_comprehension.metric("Reading comprehension MCTest-500-all", scale=correct_percent, url="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/MCTest_EMNLP2013.pdf")
mctest500.measure(date(2013, 10, 1), 63.33, "SW+D+RTE", url="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/MCTest_EMNLP2013.pdf", papername="MCTest: A Challenge Dataset for the Open-Domain Machine Comprehension of Text")
mctest500.measure(date(2015, 7, 26), 69.94, "Wang-et-al", url="http://arxiv.org/abs/1603.08884")
mctest500.measure(date(2015, 7, 26), 63.75, "Narasimhan-model3", url="https://people.csail.mit.edu/regina/my_papers/MCDR15.pdf", papername="Machine Comprehension with Discourse Relations")
mctest500.measure(date(2015, 7, 26), 67.83, "LSSVM", url="https://pdfs.semanticscholar.org/f26e/088bc4659a9b7fce28b6604d26de779bcf93.pdf", papername="Learning Answer-Entailing Structures for Machine Comprehension")
mctest500.measure(date(2016, 3, 29), 71.00, "Parallel-Hierarchical", url="http://arxiv.org/abs/1603.08884")

cbtest_ne = reading_comprehension.metric("bAbi Children's Book comprehension CBtest NE", url="http://fb.ai/babi", scale=correct_percent, target=81.6, target_source="https://arxiv.org/abs/1511.02301")
cbtest_cn = reading_comprehension.metric("bAbi Children's Book comprehension CBtest CN", url="http://fb.ai/babi", scale=correct_percent, target=81.6, target_source="https://arxiv.org/abs/1511.02301")
cnn = reading_comprehension.metric("CNN Comprehension test", url="https://github.com/deepmind/rc-data/", scale=correct_percent)
daily_mail = reading_comprehension.metric("Daily Mail Comprehension test", url="https://github.com/deepmind/rc-data/", scale=correct_percent)

cnn.measure(date(2015, 6, 10), 63.0, "Attentive reader", url="https://arxiv.org/abs/1506.03340")
cnn.measure(date(2015, 6, 10), 63.8, "Impatient reader", url="https://arxiv.org/abs/1506.03340")
daily_mail.measure(date(2015, 6, 10), 69.0, "Attentive reader", url="https://arxiv.org/abs/1506.03340")
daily_mail.measure(date(2015, 6, 10), 68.0, "Impatient reader", url="https://arxiv.org/abs/1506.03340")

cnn.measure(date(2016, 6, 7), 75.7, "AIA", url="https://arxiv.org/abs/1606.02245v1")
cbtest_ne.measure(date(2016, 6, 7), 72.0, "AIA", url="https://arxiv.org/abs/1606.02245v1")
cbtest_ne.measure(date(2016, 6, 7), 71.0, "AIA", url="https://arxiv.org/abs/1606.02245v1")

cnn.measure(date(2016, 11, 9), 76.1, "AIA", url="https://arxiv.org/abs/1606.02245v4")

cnn.measure(date(2016, 6, 7), 74.0, "EpiReader", url="https://arxiv.org/abs/1606.02270")
cbtest_ne.measure(date(2016, 6, 7), 69.7, "EpiReader", url="https://arxiv.org/abs/1606.02270")
cbtest_cn.measure(date(2016, 6, 7), 67.4, "EpiReader", url="https://arxiv.org/abs/1606.02270")

cbtest_cn.measure(date(2016, 6, 5), 69.4, "GA reader", url="https://arxiv.org/abs/1606.01549v1")
cbtest_ne.measure(date(2016, 6, 5), 71.9, "GA reader", url="https://arxiv.org/abs/1606.01549v1")
cnn.measure(date(2016, 6, 5), 77.4, "GA reader", url="https://arxiv.org/abs/1606.01549v1")
daily_mail.measure(date(2016, 6, 5), 78.1, "GA reader", url="https://arxiv.org/abs/1606.01549v1")

cnn.measure(None, 77.9, "GA update L(w)", url="https://arxiv.org/abs/1606.01549v2")
daily_mail.measure(None, 80.9, "GA update L(w)", url="https://arxiv.org/abs/1606.01549v2")
cbtest_ne.measure(None, 74.9, "GA +feature, fix L(w)", url="https://arxiv.org/abs/1606.01549v2")
cbtest_cn.measure(None, 70.7, "GA +feature, fix L(w)", url="https://arxiv.org/abs/1606.01549v2")

# Neural semantic encoders invented in https://arxiv.org/abs/1607.04315v1 and retrospectively applied to CBTest by other authors
cbtest_ne.measure(date(2016, 12, 1), 73.2, "NSE", url="https://arxiv.org/abs/1606.01549v2", algorithm_src_url="https://arxiv.org/abs/1607.04315", min_date=date(2016,7,4))
cbtest_cn.measure(date(2016, 12, 1), 71.9, "NSE", url="https://arxiv.org/abs/1606.01549v2", algorithm_src_url="https://arxiv.org/abs/1607.04315", min_date=date(2016,7,4))


cnn.measure(date(2016, 8, 4), 74.4, "AoA reader", url="https://arxiv.org/pdf/1607.04423")
cbtest_ne.measure(date(2016, 8, 4), 72.0, "AoA reader", url="https://arxiv.org/pdf/1607.04423")
cbtest_cn.measure(date(2016, 8, 4), 69.4, "AoA reader", url="https://arxiv.org/pdf/1607.04423")

cnn.measure(date(2016, 8, 8), 77.6, "Attentive+relabling+ensemble", url="https://arxiv.org/abs/1606.02858")
daily_mail.measure(date(2016, 8, 8), 79.2, "Attentive+relabling+ensemble", url="https://arxiv.org/abs/1606.02858")

cnn.measure(None, 75.4, "AS reader (avg)", url="https://arxiv.org/abs/1603.01547v1")
cnn.measure(None, 74.8, "AS reader (greedy)", url="https://arxiv.org/abs/1603.01547v1")
daily_mail.measure(None, 77.1, "AS reader (avg)", url="https://arxiv.org/abs/1603.01547v1")
daily_mail.measure(None, 77.7, "AS reader (greedy)", url="https://arxiv.org/abs/1603.01547v1")
cbtest_ne.measure(None, 70.6, "AS reader (avg)", url="https://arxiv.org/abs/1603.01547v1")
cbtest_ne.measure(None, 71.0, "AS reader (greedy)", url="https://arxiv.org/abs/1603.01547v1")
cbtest_cn.measure(None, 68.9, "AS reader (avg)", url="https://arxiv.org/abs/1603.01547v1")
cbtest_cn.measure(None, 67.5, "AS reader (greedy)", url="https://arxiv.org/abs/1603.01547v1")

squad_em = reading_comprehension.metric("Stanford Question Answering Dataset EM test", url="https://stanford-qa.com/")
squad_f1 = reading_comprehension.metric("Stanford Question Answering Dataset F1 test", url="https://stanford-qa.com/")

squad_em.measure(date(2017, 3, 8), 76.922, "r-net (ensemble)", url="https://www.microsoft.com/en-us/research/wp-content/uploads/2017/05/r-net.pdf")
squad_f1.measure(date(2017, 3, 8), 84.006, "r-net (ensemble)", url="https://www.microsoft.com/en-us/research/wp-content/uploads/2017/05/r-net.pdf")

squad_em.measure(date(2017, 3, 8), 74.614, "r-net (single model)", url="https://www.microsoft.com/en-us/research/wp-content/uploads/2017/05/r-net.pdf")
squad_f1.measure(date(2017, 3, 8), 82.458, "r-net (single model)", url="https://www.microsoft.com/en-us/research/wp-content/uploads/2017/05/r-net.pdf")

squad_em.measure(date(2017, 5, 8), 73.754, "Mnemonic reader (ensemble)", url="https://arxiv.org/pdf/1705.02798.pdf")
squad_f1.measure(date(2017, 5, 8), 81.863, "Mnemonic reader (ensemble)", url="https://arxiv.org/pdf/1705.02798.pdf")

squad_em.measure(date(2017, 4, 20), 73.723, "SEDT+BiDAF (ensemble)", url="https://arxiv.org/pdf/1703.00572.pdf")
squad_f1.measure(date(2017, 4, 20), 81.53, "SEDT+BiDAF (ensemble)", url="https://arxiv.org/pdf/1703.00572.pdf")

squad_em.measure(date(2017, 2, 24), 73.744, "BiDAF (ensemble)", url="https://arxiv.org/abs/1611.01603")
squad_f1.measure(date(2017, 2, 24), 81.525, "BiDAF (ensemble)", url="https://arxiv.org/abs/1611.01603")

squad_em.measure(date(2017, 5,31), 73.01, "jNet (ensemble)",url="https://arxiv.org/abs/1703.04617", min_date=date(2017,5,1))
squad_f1.measure(date(2017, 5,31), 81.517, "jNet (ensemble)", url="https://arxiv.org/abs/1703.04617", min_date=date(2017,5,1))

squad_em.measure(date(2016, 12, 13), 73.765, "MPM (ensemble)", url="https://arxiv.org/abs/1612.04211")
squad_f1.measure(date(2016, 12, 13), 81.257, "MPM (ensemble)", url="https://arxiv.org/abs/1612.04211")

squad_em.measure(date(2017, 2, 13), 71.2, "Dynamic Coattention Networks (ensemble)", url="https://arxiv.org/pdf/1611.01604.pdf")
squad_f1.measure(date(2017, 2, 13), 80.4, "Dynamic Coattention Networks (ensemble)", url="https://arxiv.org/pdf/1611.01604.pdf")

squad_em.measure(date(2017, 5,31), 70.607, "jNet (single model)", url="https://arxiv.org/abs/1703.04617", min_date=date(2017,5,1))
squad_f1.measure(date(2017, 5,31), 79.456, "jNet (single model)", url="https://arxiv.org/abs/1703.04617", min_date=date(2017,5,1))

squad_em.measure(date(2017, 4, 24), 70.639, "Ruminating Reader (single model)", url="https://arxiv.org/pdf/1704.07415.pdf")
squad_f1.measure(date(2017, 4, 24), 79.821, "Ruminating Reader (single model)", url="https://arxiv.org/pdf/1704.07415.pdf")

squad_em.measure(date(2017, 3, 31), 70.733, "Document Reader (single model)", url="https://arxiv.org/abs/1704.00051")
squad_f1.measure(date(2017, 3, 31), 79.353, "Document Reader (single model)", url="https://arxiv.org/abs/1704.00051")

squad_em.measure(date(2017, 5, 8), 69.863, "Mnemonic reader (single model)", url="https://arxiv.org/pdf/1705.02798.pdf")
squad_f1.measure(date(2017, 5, 8), 79.207, "Mnemonic reader (single model)", url="https://arxiv.org/pdf/1705.02798.pdf")

squad_em.measure(date(2016, 12, 29), 70.849, "FastQAExt", url="https://arxiv.org/abs/1703.04816")
squad_f1.measure(date(2016, 12, 29), 78.857, "FastQAExt", url="https://arxiv.org/abs/1703.04816")

squad_em.measure(date(2016, 12, 13), 70.387, "MPM (single model)", url="https://arxiv.org/abs/1612.04211")
squad_f1.measure(date(2016, 12, 13), 78.784, "MPM (single model)", url="https://arxiv.org/abs/1612.04211")

squad_em.measure(date(2017, 5, 31), 70.849, "RaSoR (single model)", url="https://arxiv.org/abs/1611.01436", min_date=date(2017,5,1))
squad_f1.measure(date(2017, 5, 31), 78.741, "RaSoR (single model)", url="https://arxiv.org/abs/1611.01436", min_date=date(2017,5,1))

squad_em.measure(date(2017, 4, 20), 68.478, "SEDT+BiDAF (single model)", url="https://arxiv.org/pdf/1703.00572.pdf")
squad_f1.measure(date(2017, 4, 20), 77.971, "SEDT+BiDAF (single model)", url="https://arxiv.org/pdf/1703.00572.pdf")

squad_em.measure(date(2016, 11, 29), 68.478, "BiDAF (single model)", url="https://arxiv.org/abs/1611.01603")
squad_f1.measure(date(2016, 11, 29), 77.971, "BiDAF (single model)", url="https://arxiv.org/abs/1611.01603")

squad_em.measure(date(2016, 12, 29), 68.436, "FastQA", url="https://arxiv.org/abs/1703.04816")
squad_f1.measure(date(2016, 12, 29), 77.07, "FastQA", url="https://arxiv.org/abs/1703.04816")

squad_em.measure(date(2016, 11, 7), 67.901, "Match-LSTM+Ans-Ptr", url="https://arxiv.org/pdf/1608.07905v2")
squad_f1.measure(date(2016, 11, 7), 77.022, "Match-LSTM+Ans-Ptr", url="https://arxiv.org/pdf/1608.07905v2")

