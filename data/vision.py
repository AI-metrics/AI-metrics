from taxonomy import Problem
from scales import *
import datetime

date = datetime.date

vision = Problem("Vision", ["agi", "vision", "world-modelling"])

image_comprehension = Problem("Image comprehension", ["agi", "vision", "language", "world-modelling"])
image_classification = Problem("Image classification", ["vision", "agi"])
image_classification.add_subproblem(image_comprehension)
vision.add_subproblem(image_classification)

imagenet = image_classification.metric("Imagenet Image Recognition", "http://image-net.org", scale=error_rate, target=0.051)
imagenet.notes = """
Correctly label images from the Imagenet dataset. As of 2016, this includes:
 - Object localization for 1000 categories.
 - Object detection for 200 fully labeled categories.
 - Object detection from video for 30 fully labeled categories.
 - Scene classification for 365 scene categories (Joint with MIT Places team) on Places2 Database http://places2.csail.mit.edu.
 - Scene parsing for 150 stuff and discrete object categories (Joint with MIT Places team).
"""
imagenet.measure(date(2010,8,31), 0.28191, "NEC UIUC", "http://image-net.org/challenges/LSVRC/2010/results")
imagenet.measure(date(2011,10,26), 0.2577, "XRCE","http://image-net.org/challenges/LSVRC/2011/results")
imagenet.measure(date(2012,10,13), 0.16422, "SuperVision", "http://image-net.org/challenges/LSVRC/2012/results.html")
imagenet.measure(date(2013,11,14), 0.11743, "Clarifai","http://www.image-net.org/challenges/LSVRC/2013/results.php")
imagenet.measure(date(2014,8,18), 0.07405, "VGG", "http://image-net.org/challenges/LSVRC/2014/index")
imagenet.measure(date(2015,12,10), 0.03567, "MSRA", "http://image-net.org/challenges/LSVRC/2015/results", algorithms=["residual-networks"])
imagenet.measure(date(2016,9,26), 0.02991, "Trimps-Soushen", "http://image-net.org/challenges/LSVRC/2016/results")

# Test automatic detection of withdrawn papers
imagenet.measure(None, 0.0458, "withdrawn", "https://arxiv.org/abs/1501.02876")

video_classification = Problem("Recognise events in videos")
vision.add_subproblem(video_classification)
video_classification.metric("YouTube-8M video labelling", url="https://research.google.com/youtube8m/")

# The VQA paper breaks human performance down by real/abstract image so we need to compute the overall number...
# Also they don't seem to have human performance numbers for VQA multiple choice?
vqa_abstract_human_performance = 87.49
vqa_real_human_performance = 83.3
vqa_imgs = 50000 + 204751.
vqa_target = (50000/vqa_imgs) * vqa_abstract_human_performance + (204751 / vqa_imgs) * vqa_real_human_performance

vqa_oe = image_comprehension.metric("COCO Visual Question Answering (VQA) 1.0 open ended", url="http://visualqa.org/", target=vqa_target, target_source="https://arxiv.org/abs/1505.00468", scale=correct_percent)
vqa_mc = image_comprehension.metric("COCO Visual Question Answering (VQA) 1.0 multiple choice", url="http://visualqa.org/", scale=correct_percent, solved=False)
# other visual question answering metrics (we don't have data for these yet)
# For a survey: https://arxiv.org/pdf/1607.05910
image_comprehension.metric("Toronto COCO-QA", url="http://www.cs.toronto.edu/~mren/imageqa/data/cocoqa/" )
image_comprehension.metric("DAQUAR", url="https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/research/vision-and-language/visual-turing-challenge/", scale=correct_percent, target=60.27, target_source="https://arxiv.org/abs/1505.02074")
visual_genome_pairs = image_comprehension.metric("Visual Genome (pairs)", url="http://visualgenome.org", scale=correct_percent, axis_label="Top-1 precision")
visual_genome_subjects = image_comprehension.metric("Visual Genome (subjects)", url="http://visualgenome.org", scale=correct_percent, axis_label="Top-1 precision")

visual7w = image_comprehension.metric("Visual7W", url="https://arxiv.org/abs/1511.03416", scale=correct_percent)
image_comprehension.metric("FM-IQA", url="http://idl.baidu.com/FM-IQA.html")
image_comprehension.metric("Visual Madlibs", url="http://tamaraberg.com/visualmadlibs/")

vqa_oe.measure(date(2015,12,15), 55.89, "iBOWIMG baseline", url="https://arxiv.org/abs/1512.02167")
vqa_mc.measure(date(2015,12,15), 61.97, "iBOWIMG baseline", url="https://arxiv.org/abs/1512.02167")

vqa_oe.measure(None, 58.24, "SMem-VQA", url="https://arxiv.org/abs/1511.05234v2")

# not so clear what the number in the SANv1 paper was...
#vqa_oe.measure(None, 57.6, "SAN(2,CNN)", url="https://arxiv.org/abs/1511.02274v1")
vqa_oe.measure(None, 58.9, "SAN", url="https://arxiv.org/abs/1511.02274v2")

vqa_oe.measure(None, 59.5, "CNN-RNN", url="https://arxiv.org/abs/1603.02814v1")

vqa_oe.measure(None, 59.5, "FDA", url="https://arxiv.org/abs/1604.01485v1")
vqa_mc.measure(None, 64.2, "FDA", url="https://arxiv.org/abs/1604.01485v1")

vqa_oe.measure(None, 62.1, "HQI+ResNet", url="https://arxiv.org/abs/1606.00061v1")
vqa_mc.measure(None, 66.1, "HQI+ResNet", url="https://arxiv.org/abs/1606.00061v1")

vqa_oe.measure(None, 58.2, "LSTM Q+I", url="https://arxiv.org/abs/1505.00468v1")
vqa_mc.measure(None, 63.1, "LSTM Q+I", url="https://arxiv.org/abs/1505.00468v1")

vqa_oe.measure(None, 63.2, "joint-loss", url="https://arxiv.org/abs/1606.03647")
vqa_mc.measure(None, 67.3, "joint-loss", url="https://arxiv.org/abs/1606.03647")

vqa_oe.measure(None, 66.5, "7 att. ensemble", url="https://arxiv.org/abs/1606.01847v1")
vqa_mc.measure(None, 70.1, "7 att. ensemble", url="https://arxiv.org/abs/1606.01847v1")
visual7w.measure(None, 62.2, "MCB+Att.", url="https://arxiv.org/abs/1606.01847v1")

visual7w.measure(None, 72.53, "CMN", url="https://arxiv.org/abs/1611.09978v1")
visual_genome_pairs.measure(None, 28.52, "CMN", url="https://arxiv.org/abs/1611.09978v1")
visual_genome_subjects.measure(None, 44.24, "CMN", url="https://arxiv.org/abs/1611.09978v1")

