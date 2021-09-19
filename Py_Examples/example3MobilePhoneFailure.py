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

prior_beta = beta(prior.alpha, prior.beta)
prior_pdf = prior_beta.pdf(xseq)

posterior_beta = beta(posterior.alpha, posterior.beta)
posterior_pdf = posterior_beta.pdf(xseq)

plt.plot(xseq, prior_pdf)
plt.plot(xseq, posterior_pdf)
plt.show()

print("Chance of being 90% or above: {}".format(1 - posterior_beta.cdf(0.9)))
print("Chance of being 95% or above: {}".format(1 - posterior_beta.cdf(0.95)))
