from math import log
            
# Different metrics and measurements for progress are made on very different types of scales
# we have some helper functions to regularise these a little bit, so we can tell (for instance)
# whether progress on some metric appears to be accelerating or decelerating.

# Interface:
#    improvement(score1, score2): retrns a consistent measure of how much better score2 is than score1
#    pseudolinear(score): returns a modified version of score where we would expect vaguely linear progress

class Linear():
    offset = (2,-2)
    axis_label = "Score"
    col_label = "Score"
    def improvement(self, score1, score2):
        return score2 - score1
    def pseudolinear(self, score):
        return score

class AtariLinear():
    offset = (2,-2)
    axis_label = "Score"
    col_label = "Raw Score"
    def improvement(self, score1, score2):
        return score2 - score1
    def pseudolinear(self, score):
        return score    
    
linear = Linear()
score = Linear()
atari_linear = AtariLinear()

class ELO:
    offset = (2,-2)
    axis_label = "ELO rating"
    col_label = "ELO"
    def improvement(self, score1, score2):
        """
        Normalise an ELO score
        
        An ELO increase of 400 improves your odds by 10x, so we could justify something like
        return 10.0 ** ((score2 - score1)/400.)
        However, it seems that at least for chess ELO progress has been roughly linear over
        time, both for humans and computers (though with different coefficients). Perhaps this
        tracks exponential increases in ability to search the game's state space, driven directly
        by Moore's law on the computer side, and indirectly for humans by access to better training
        tools and more profound libraries of past play.
        
        So for now let's treat this as linear? But ELO is not a chess-specific measure, and in other
        contexts we may want to do exponentiation as documented above?
        """
        return score2 - score1
    def pseudolinear(self, score):
        return score
    
elo = ELO()

class ErrorRate:
    """Many labelling contests use these measures"""
    offset = (2,2)
    axis_label = "Error rate"
    col_label = "Error"
    def improvement(self, score1, score2):
        # improvement is measured as a negative log of the error rate
        return log(score1) - log(score2)
    def pseudolinear(self, score):
        # error rate 1 => 0
        # error rate 0 => infinity
        return -log(score)
error_rate = ErrorRate()

# some problems have performance measured in bits per X (bits per character, bits per pixel, etc), 
# reflecting the amount of information necessary for a model to accurately encode something from a corpus.
# Lower is better and zero is infinitely good, so we can re-use the error rate math for now (though
# scores above 1 are possible)
bits_per_x = ErrorRate()
bits_per_x.axis_label = "Model Entropy"
bits_per_x.col_label = "Model<br>Entropy"
# perplexity is 2 to the bits_per_x
perplexity = ErrorRate()
perplexity.axis_label = "Perplexity"
perplexity.col_label = "Perplexity"

class CorrectPercent:
    "100 - error rate"
    offset = (3,-6)
    axis_label = "Percentage correct"
    col_label = "% correct"
    def erate(self, score):
        return (100. - score)/100.

    def improvement(self, score1, score2):
        return score2 - score1
    
    def pseudolinear(self, score):
        from math import log
        return -log(self.erate(score))

correct_percent = CorrectPercent()

class BLEUScore:
    "50 is a perfect BLEU score, meaning a system produces exact matches to professional human translations"
    offset = (3,-6)
    axis_label = "BLEU score"
    col_label = "BLEU"
    def erate(self, score):
        return (50. - score)/50.

    def improvement(self, score1, score2):
        return score2 - score1
    
    def pseudolinear(self, score):
        from math import log
        return -log(self.erate(score))

bleu_score = BLEUScore()

class ErrorPercent:
    "100 * error rate"
    offset = (3,-6)
    axis_label = "Percentage error"
    col_label = "% error"
    def erate(self, score):
        return score/100.

    def improvement(self, score1, score2):
        return score1 - score2
    
    def pseudolinear(self, score):
        from math import log
        return log(self.erate(score))
    
error_percent = ErrorPercent()

