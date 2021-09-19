from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta


@dataclass
class BetaHyperParameters:
    alpha: float
    beta: float


@dataclass
class BinomialSampling:
    n: float
    y: float


xseq = np.arange(0.00, 1.00, 0.005)

prior = BetaHyperParameters(1.6, 0.178)
sampling = BinomialSampling(200, 172)
posterior = BetaHyperParameters(prior.alpha + sampling.y, prior.beta + sampling.n - sampling.y)

prior_pdf = beta.pdf(xseq, prior.alpha, prior.beta)
posterior_pdf = beta.pdf(xseq, posterior.alpha, posterior.beta)

plt.plot(xseq, prior_pdf)
plt.plot(xseq, posterior_pdf)
plt.show()
