library(ggplot2)

xseq <- seq(0.00, 1.00, by=0.005)

prior.alpha <- 1.6
prior.beta <- 0.178

n <- 200
y <- 172

posterior.alpha <- prior.alpha + y
posterior.beta <- prior.beta + n - y

prior.pdf <- dbeta(xseq, prior.alpha, prior.beta)
posterior.pdf <- dbeta(xseq, posterior.alpha, posterior.beta)

dataframe <- data.frame(x=xseq, prior=prior.pdf, posterior=posterior.pdf)

g1 <- ggplot(dataframe, mapping=aes(x, prior))
g1 = g1 + geom_line(col="blue")
g1 = g1 + geom_line(mapping=aes(y=posterior), col="red")
g1 = g1 + xlab(expression(theta))

print(g1)
