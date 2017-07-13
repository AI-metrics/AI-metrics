"Hand-entered data about performance of generative models"
from taxonomy import Problem
from scales import *
import datetime
date = datetime.date

""" 
* * *
**_Generative models of CIFAR-10 Natural Images _****[Year: bits-per-subpixel, method]. Compiled by Durk Kingma.**

**Why we care:**
(1) The compression=prediction=understanding=intelligence view (see Hutter prize, etc.). (Note that perplexity, log-likelihood, and #bits are all equivalent measurements.)
(2) Learning a generative model is a prominent auxiliary task towards semi-supervised learning. Current SOTA semi-supervised classification results utilize generative models.
3) You're finding patterns in the data that let you compress it more efficiently. Ultimate pattern recognition benchmark because you're trying to find the patterns in all the data. 

"""

image_generation = Problem("Drawing pictures", ["vision", "agi"])
# note: this section is not on scene generation, but making the distinction seemed like a good idea.
scene_generation = Problem("Be able to generate complex scene e.g. a baboon receiving their degree at convocatoin.", ["vision", "world-modelling", "agi"])
scene_generation.add_subproblem(image_generation)

# NOTE: scale, and target need to be checked
image_generation_metric = image_generation.metric("Generative models of CIFAR-10 images", scale=bits_per_x, axis_label="Model entropy (bits per pixel)")

image_generation_metric.measure(date(2014,10,30), 4.48, "NICE", "https://arxiv.org/abs/1410.8516")
image_generation_metric.measure(date(2015,2,16), 4.13, "DRAW", "https://arxiv.org/abs/1502.04623")
image_generation_metric.measure(date(2016,5,27), 3.49, "Real NVP", "https://arxiv.org/abs/1605.08803")
image_generation_metric.measure(date(2016,6,15), 3.11, "VAE with IAF", "https://papers.nips.cc/paper/6581-improved-variational-inference-with-inverse-autoregressive-flow")
image_generation_metric.measure(date(2016,5,27), 3.0, "PixelRNN", "https://arxiv.org/abs/1605.08803")
image_generation_metric.measure(date(2016,11,4), 2.92, "PixelCNN++","https://openreview.net/forum?id=BJrFC6ceg", replicated="https://github.com/openai/pixel-cnn")
