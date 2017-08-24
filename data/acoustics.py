"Hand-entered acoustic data"
from taxonomy import Problem
from scales import *
import datetime
date = datetime.date

"""
        http://melodi.ee.washington.edu/s3tp/

* * *
**_Word error rate on Switchboard (specify details): [Month, Year: Score [SWB]: Team].  Compiled by Jack Clark._**

A note about measurement: We're measuring Switchboard (SWB) and Call Home (CH) performance (mostly) from the Hub5'00 dataset, with main scores assesses in terms of word error rate on SWB. We also create 

Why do we care: Reflects the improvement of audio processing systems on speech over time.

"""
speech_recognition = Problem(name="Speech Recognition", attributes=["language", "agi"])
swb_hub_500 = speech_recognition.metric(name="Word error rate on Switchboard trained against the Hub5'00 dataset",
                                               scale=error_percent, target=5.9)
swb_hub_500.measure(date(2011,8,31), 16.1, "CD-DNN", "https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/CD-DNN-HMM-SWB-Interspeech2011-Pub.pdf")
swb_hub_500.measure(date(2012,4,27), 18.5, "DNN-HMM", "https://pdfs.semanticscholar.org/ce25/00257fda92338ec0a117bea1dbc0381d7c73.pdf?_ga=1.195375081.452266805.1483390947")

swb_hub_500.measure(date(2013,8,25), 12.9, "DNN MMI", "http://www.danielpovey.com/files/2013_interspeech_dnn.pdf")
swb_hub_500.measure(date(2013,8,25), 12.6, "DNN sMBR", "http://www.danielpovey.com/files/2013_interspeech_dnn.pdf")
swb_hub_500.measure(date(2013,8,25), 12.9, "DNN MPE", "http://www.danielpovey.com/files/2013_interspeech_dnn.pdf")
swb_hub_500.measure(date(2013,8,25), 12.9, "DNN BMMI", "http://www.danielpovey.com/files/2013_interspeech_dnn.pdf")

swb_hub_500.measure(date(2014,6,30), 16, "DNN", "https://arxiv.org/abs/1406.7806v1")

swb_hub_500.measure(date(2014,12,7), 20, "Deep Speech", "https://arxiv.org/abs/1412.5567")
swb_hub_500.measure(date(2014,12,7), 12.6, "Deep Speech + FSH", url="https://arxiv.org/abs/1412.5567") # TODO: why is this also included?

swb_hub_500.measure(date(2015,5,21), 8.0, "IBM 2015", "https://arxiv.org/abs/1505.05899") # TODO: (name check)
swb_hub_500.measure(date(2016,4,27), 6.9, "IBM 2016", "https://arxiv.org/abs/1604.08242v1") # TODO: (name check)

swb_hub_500.measure(date(2017,2,17), 6.9, "RNNLM", "https://arxiv.org/abs/1609.03528") # TODO: (name check)
swb_hub_500.measure(date(2017,2,17), 6.2, "Microsoft 2016", "https://arxiv.org/abs/1609.03528") # TODO: (name check)

swb_hub_500.measure(date(2016,10,17), 6.6, "CNN-LSTM", "https://arxiv.org/abs/1610.05256") # TODO: (name check)
swb_hub_500.measure(None, 5.8, "Microsoft 2016b", "https://arxiv.org/abs/1610.05256") # TODO: (name check)

"""
Author    Yann Bayle
E-mail    bayle.yann@live.fr
Created   03/08/2017
Updated   04/08/2017
Object    Music Information Retrieval tasks

Why do we care: Reflects the improvement of music auto-tagging over time.
"""

# Precision for the Instrumentals detection in a musical database in order to create an Instrumental playlist
instrumentals_recognition = Problem(name="Detection of Instrumentals musical tracks", attributes=["language", "agi"])
satin = instrumentals_recognition.metric(name="Precision of Instrumentals detection reached when tested on SATIN (Bayle et al. 2017)", scale=correct_percent, target=99)
satin.measure(date(2013, 10, 17), 17.3, "Ghosal et al.", "https://link.springer.com/article/10.1186/2193-1801-2-526")
satin.measure(date(2014, 9, 30), 12.5, "SVMBFF", "https://arxiv.org/pdf/1410.0001.pdf")
satin.measure(date(2014, 9, 30), 29.8, "VQMM", "https://arxiv.org/pdf/1410.0001.pdf")
satin.measure(date(2017, 6, 23), 82.5, "Bayle et al.", "https://arxiv.org/abs/1706.07613")

# MAP and MAR for Cover Song Identification currently being written

# Need for people to work on genres recognition
