# -*- coding: utf-8 -*-
"Hand-entered data about written language problems"
from taxonomy import Problem
from scales import *
import datetime
date = datetime.date

modelling_english = Problem("Accurate modelling of human language.", ["language", "agi"])
ptperplexity = modelling_english.metric(name="Penn Treebank (Perplexity when parsing English sentences)", scale=perplexity)
ptperplexity.measure(date(2016,9,26), 70.9, "Pointer Sentinel-LSTM", "https://arxiv.org/pdf/1609.07843v1.pdf")
ptperplexity.measure(date(2016,10,5), 73.4, "Variational LSTM", "https://arxiv.org/pdf/1512.05287v5.pdf")
ptperplexity.measure(date(2013,12,20), 107.5, "Deep RNN", "https://arxiv.org/abs/1312.6026")
ptperplexity.measure(date(2012,4,7), 78.8, "KN5+RNNME ensemble", "http://www.fit.vutbr.cz/~imikolov/rnnlm/google.pdf")
ptperplexity.measure(date(2012,4,7), 125.7, "KN5+cache baseline", "http://www.fit.vutbr.cz/~imikolov/rnnlm/google.pdf")

ptperplexity.measure(date(2012,7,27), 124.7, "RNNLM", "https://www.microsoft.com/en-us/research/wp-content/uploads/2012/07/rnn_ctxt_TR.sav_.pdf")
ptperplexity.measure(date(2012,7,27), 74.1, "RNN-LDA+all", "https://www.microsoft.com/en-us/research/wp-content/uploads/2012/07/rnn_ctxt_TR.sav_.pdf")
ptperplexity.measure(date(2012,7,27), 113.7, "RNN-LDA LM", "https://www.microsoft.com/en-us/research/wp-content/uploads/2012/07/rnn_ctxt_TR.sav_.pdf")
ptperplexity.measure(date(2012,7,27), 92.0, "RNN-LDA LM+KN5+cache", "https://www.microsoft.com/en-us/research/wp-content/uploads/2012/07/rnn_ctxt_TR.sav_.pdf")
ptperplexity.measure(date(2012,7,27), 80.1, "RNN-LDA ensemble", "https://www.microsoft.com/en-us/research/wp-content/uploads/2012/07/rnn_ctxt_TR.sav_.pdf")
ptperplexity.measure(None, 68.7, "RNN Dropout Regularization", "https://arxiv.org/abs/1409.2329v1")
ptperplexity.measure(None, 68.5, "RHN", "https://arxiv.org/pdf/1607.03474v3")
ptperplexity.measure(None, 66, "RHN+WT", "https://arxiv.org/pdf/1607.03474v3")
ptperplexity.measure(None, 71.3, "RHN", "https://arxiv.org/abs/1607.03474v2")
ptperplexity.measure(None, 65.4, "RHN+WT", "https://arxiv.org/abs/1607.03474v4")
ptperplexity.measure(None, 62.4, "Neural Architecture Search", url="https://arxiv.org/abs/1611.01578v2", venue="ICLR 2017")


hp_compression = modelling_english.metric(name="Hutter Prize (bits per character to encode English text)", scale=bits_per_x, 
                                          target=1.3, target_label="Region of human performance",
                                          target_source="http://languagelog.ldc.upenn.edu/myl/Shannon1950.pdf")
hp_compression.measure(date(2016,10,31), 1.313, "Surprisal-Driven Zoneout",
                   "https://pdfs.semanticscholar.org/e9bc/83f9ff502bec9cffb750468f76fdfcf5dd05.pdf")
hp_compression.measure(date(2016,10,19), 1.37, "Surprisal-Driven Feedback RNN",
                   "https://arxiv.org/pdf/1608.06027.pdf")
hp_compression.measure(date(2016,9,27), 1.39, "Hypernetworks", "https://arxiv.org/abs/1609.09106")
hp_compression.measure(date(2016,9,6), 1.32, " Hierarchical Multiscale RNN", "https://arxiv.org/abs/1609.01704")
hp_compression.measure(date(2016,7,12), 1.32, "Recurrent Highway Networks", "https://arxiv.org/abs/1607.03474")
hp_compression.measure(date(2015,7,6), 1.47, "Grid LSTM", "https://arxiv.org/abs/1507.01526")
hp_compression.measure(date(2015,2,15), 1.58, "Gated Feedback RNN", "https://arxiv.org/abs/1502.02367")
# we need to match/double check the release date of the specific version of cmix that got this performance?
# hp_compression.measure(date(2014,4,13), 1.245, "cmix", "http://www.byronknoll.com/cmix.html")
hp_compression.measure(date(2013,8,4), 1.67, "RNN, LSTM", "https://arxiv.org/abs/1308.0850")
hp_compression.measure(date(2011,6,28), 1.60, "RNN", "http://www.cs.utoronto.ca/~ilya/pubs/2011/LANG-RNN.pdf")

hp_compression.measure(None, 1.42, "RHN", "https://arxiv.org/abs/1607.03474v2")
hp_compression.measure(None, 1.27, "Large RHN depth 10", "https://arxiv.org/abs/1607.03474v4")

lambada = modelling_english.metric("LAMBADA prediction of words in discourse", url="https://arxiv.org/abs/1606.06031",
                                   scale=correct_percent, target=86, target_source="https://arxiv.org/abs/1610.08431v3")
lambada.measure(None, 21.7, "Stanford Reader", url="https://arxiv.org/abs/1610.08431v3", algorithm_src_url="https://arxiv.org/abs/1606.02858")
lambada.measure(None, 32.1, "Modified Stanford", url="https://arxiv.org/abs/1610.08431v3", algorithm_src_url="https://arxiv.org/abs/1606.02858")
lambada.measure(None, 49.0, "GA + feat.", url="https://arxiv.org/abs/1610.08431v3", algorithm_src_url="https://arxiv.org/abs/1606.01549v2")
lambada.measure(None, 44.5, "AS + feat.", url="https://arxiv.org/abs/1610.08431v3", algorithm_src_url="https://arxiv.org/abs/1603.01547")
lambada.measure(None, 51.6, "GA+MAGE (48)", url="https://arxiv.org/abs/1703.02620v1")

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
bAbi10k.measure(date(2015,2,19), 93.3, "MemNN-AM+NG+NL (1k + strong supervision)", "https://arxiv.org/abs/1502.05698v1", 
                not_directly_comparable=True, long_label=True, offset=(2,5)) # not literally a 10K example, but more comparable to it

#bAbi1k.measure(None, 48.7, "LSTM", "https://arxiv.org/abs/1502.05698v1", algorithm_src_url="http://isle.illinois.edu/sst/meetings/2015/hochreiter-lstm.pdf", min_date=date(1997,11,15))
bAbi1k.measure(date(2015,3,31), 86.1, "MemN2N-PE+LS+RN", "https://arxiv.org/abs/1503.08895")
bAbi10k.measure(date(2015,3,31), 93.4, "MemN2N-PE+LS+RN", "https://arxiv.org/abs/1503.08895")
bAbi1k.measure(date(2015,6,24), 93.6, "DMN", "https://arxiv.org/abs/1506.07285", offset=(3,-2), not_directly_comparable=True) # The paper doesn't say if this is 1k or 10k
bAbi10k.measure(date(2016,1,5), 96.2, "DNC", "https://www.gwern.net/docs/2016-graves.pdf")

bAbi10k.measure(date(2016,9,27), 97.1, "SDNC", "https://arxiv.org/abs/1606.04582v4")
bAbi10k.measure(date(2016,12,12), 99.5, "EntNet", "https://arxiv.org/abs/1612.03969")
bAbi1k.measure(date(2016,12,12), 89.1, "EntNet", "https://arxiv.org/abs/1612.03969")

bAbi10k.measure(date(2016,12,9),  99.7, "QRN", "https://arxiv.org/abs/1606.04582v4", offset=(2,3))
bAbi1k.measure(date(2016,12,9),  90.1, "QRN", "https://arxiv.org/abs/1606.04582v4")
bAbi1k.measure(None, 66.8, "DMN+", "https://arxiv.org/abs/1606.04582v4", algorithm_src_url="https://arxiv.org/abs/1607.00036", replicated="https://github.com/therne/dmn-tensorflow")
bAbi10k.measure(date(2016,6,30),  97.2, "DMN+", "https://arxiv.org/abs/1607.00036")

bAbi1k.measure(None, 91.3, "GA+MAGE (16)", url="https://arxiv.org/abs/1703.02620v1")
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
squad_em = reading_comprehension.metric("Stanford Question Answering Dataset EM test", url="https://stanford-qa.com/", target=82.304, target_source="http://arxiv.org/abs/1606.05250")
squad_f1 = reading_comprehension.metric("Stanford Question Answering Dataset F1 test", url="https://stanford-qa.com/", target=91.221, target_source="http://arxiv.org/abs/1606.05250")

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

cnn.measure(None, 74.7, "ReasoNet", url="https://arxiv.org/abs/1609.05284v1")
daily_mail.measure(None, 76.6, "ReasoNet", url="https://arxiv.org/abs/1609.05284v1")
squad_em.measure(None, 73.4, "ReasoNet ensemble", url="https://arxiv.org/abs/1609.05284v3")
squad_f1.measure(None, 82.9, "ReasoNet ensemble", url="https://arxiv.org/abs/1609.05284v3")

cnn.measure(None, 78.6, "GA+MAGE (32)", url="https://arxiv.org/abs/1703.02620v1")
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

squad_em.measure(None, 75.37, "MEMEN", url="https://arxiv.org/abs/1707.09098v1")
squad_f1.measure(None, 82.66, "MEMEN", url="https://arxiv.org/abs/1707.09098v1")

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

squad_em.measure(date(2016, 11, 4), 66.233, "Dynamic Coattention Networks (single model)", url="https://arxiv.org/pdf/1611.01604v1")
squad_f1.measure(date(2016, 11, 4), 75.896, "Dynamic Coattention Networks (single model)", url="https://arxiv.org/pdf/1611.01604v1")

squad_em.measure(date(2016, 11, 4), 71.625, "Dynamic Coattention Networks (ensemble)", url="https://arxiv.org/pdf/1611.01604v1")
squad_f1.measure(date(2016, 11, 4), 80.383, "Dynamic Coattention Networks (ensemble)", url="https://arxiv.org/pdf/1611.01604v1")

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

squad_em.measure(date(2017, 8, 21), 77.678, "RMR (ensemble)", url="https://arxiv.org/abs/1705.02798")
squad_f1.measure(date(2017, 8, 21), 84.888, "RMR (ensemble)", url="https://arxiv.org/abs/1705.02798")

squad_em.measure(date(2017, 8, 16), 78.706, "DCN+ (ensemble)", url="https://rajpurkar.github.io/SQuAD-explorer/")
squad_f1.measure(date(2017, 8, 16), 85.619, "DCN+ (ensemble)", url="https://rajpurkar.github.io/SQuAD-explorer/")

squad_em.measure(date(2017, 9, 20), 78.842, "AIR-FusionNet (ensemble)", url="https://rajpurkar.github.io/SQuAD-explorer/")
squad_f1.measure(date(2017, 9, 20), 85.936, "AIR-FusionNet (ensemble)", url="https://rajpurkar.github.io/SQuAD-explorer/")

translation = Problem("Translation between human langauges", ["agi", "language"])
en_fr_bleu = translation.metric("news-test-2014 En-Fr BLEU", url="http://aclweb.org/anthology/P/P02/P02-1040.pdf", scale=bleu_score, target_label="Identical to professional human translations", target=50)
en_de_bleu = translation.metric("news-test-2014 En-De BLEU", url="http://aclweb.org/anthology/P/P02/P02-1040.pdf", scale=bleu_score, target_label="Identical to professional human translations", target=50)
en_ro_bleu = translation.metric("news-test-2016 En-Ro BLEU", url="http://www.statmt.org/wmt16/book.pdf", scale=bleu_score, target_label="Identical to professional human translations", target=50)


en_fr_bleu.measure(None, 37, "PBMT", url="http://www.anthology.aclweb.org/W/W14/W14-33.pdf", papername=u"Edinburgh’s phrase-based machine translation systems for WMT-14", venue="WMT 2014")
en_de_bleu.measure(None, 20.7, "PBMT", url="http://www.anthology.aclweb.org/W/W14/W14-33.pdf", papername=u"Edinburgh’s phrase-based machine translation systems for WMT-14", venue="WMT 2014")

en_fr_bleu.measure(date(2014, 9, 1), 36.15, "RNN-search50*", url="https://arxiv.org/abs/1409.0473")
en_fr_bleu.measure(date(2014, 10, 30), 37.5, "LSTM6 + PosUnk", url="https://arxiv.org/abs/1410.8206")

# XXX need a better way of indicating that LSTM is old.... we don't want the axes running
# all the way back to 1997; maybe we can use ellipses?
en_fr_bleu.measure(None, 34.81, "LSTM", "https://arxiv.org/abs/1409.3215v1", algorithm_src_url="http://www.bioinf.jku.at/publications/older/2604.pdf")#, min_date=date(2010,1,1))
en_fr_bleu.measure(None, 36.5, "SMT+LSTM5", "https://arxiv.org/abs/1409.3215v1")

en_fr_bleu.measure(date(2016, 9, 26), 39.92, "GNMT+RL", url="https://arxiv.org/abs/1609.08144")
en_de_bleu.measure(date(2016, 9, 26), 26.30, "GNMT+RL", url="https://arxiv.org/abs/1609.08144")

# Lots of this data is coming via https://arxiv.org/abs/1609.08144
en_fr_bleu.measure(date(2016, 7, 23), 39.2, "Deep-Att + PosUnk", url="https://arxiv.org/abs/1606.04199")
en_de_bleu.measure(date(2016, 7, 23), 20.7, "Deep-Att", url="https://arxiv.org/abs/1606.04199")

en_fr_bleu.measure(date(2017, 1, 23), 40.56, "MoE 2048", url="https://arxiv.org/pdf/1701.06538")
en_de_bleu.measure(date(2017, 1, 23), 26.03, "MoE 2048", url="https://arxiv.org/pdf/1701.06538")

en_fr_bleu.measure(None, 41.29, "ConvS2S ensemble", url="https://arxiv.org/abs/1705.03122v2")
en_de_bleu.measure(None, 26.36, "ConvS2S ensemble", url="https://arxiv.org/abs/1705.03122v2")


en_de_bleu.measure(date(2016, 7, 14), 17.93, "NSE-NSE", url="https://arxiv.org/abs/1607.04315v1")

en_ro_bleu.measure(date(2016, 7, 11), 28.9, "GRU BPE90k", papername="The QT21/HimL Combined Machine Translation System", url="http://www.statmt.org/wmt16/pdf/W16-2320.pdf")
en_ro_bleu.measure(None, 29.88, "ConvS2S BPE40k", url="https://arxiv.org/abs/1705.03122v2")

# XXX add more languages
