# Information & Entropy

## Information

Data $+$ context. Identification of relevant patterns within the data. Can lead us to take decisions. Conveys meaning (purpose).

### Information Theory
Branch of applied mathematics that help us quantify the amount of information contained in a signal (data).

- **Intuiton**: learning that an unlikely event has happened is more informative than knowing that a likely event happened.
- **Example**: the message "the sun rose this morning" is so uninformative that it is unnecessary to communicate; whereas the message "ther was a solar eclipse this morning" is highly informative.

Assumptions:
- Highly probable events contain little information
- In the extreme case, events whose occurrence is certain, should not have information at all
- Unlikely events must have a lot of information
- Independent events must have additive information
- The length of the message carrying the information must be proportional to the amount of information

### Distribution of events
Very certain outcome
- One-hot distribution on possible outcomes
- Low entropy
- 1 event $\Rightarrow$ no information

Very uncertain outcome
- Uniform distribution on possible outcomes
- High entropy
- 1 event $\Rightarrow$ lots of information

### Information
Let's think of an event as a random variable.  
The **information** (suprise) $I(x)$ for a random variable $x$, with probability $p(x)$, is **defined** as the inverse of its probability:
$$I(x) = \frac{1}{p(x)}$$
If an event is highly probable, then there is no surprise.

Notemos lo siguiente,
$$p(x) = 1 \Rightarrow I(x) = 1$$
Que no es lo que estamos buscando. Use instead $log(\cdot)$: $log(\frac{1}{1}) = 0$  
Tenemos pues que,
$$I(x) = log\left(\frac{1}{p(x)}\right),$$
$$= -log[p(x)]$$

Así pues,
$$p(x) = 0 \Rightarrow log\left(\frac{1}{0}\right) = log(1) - log(0) = inf$$
Which would be the surprise of something that never happens.  
Often, $ln(\cdot)$ is used (nats), or $log_2(\cdot)$ (bits)

## Entropy
Expected value of surprise.  
We can quantify the amount of information in a whole $pdf$ using the concept of Entropy.

$$H(x) = \mathbb{E}[I(x)],$$
$$=-\sum_xp(x)log(p(x))$$

where,
- $H(x)$ indicates the amount of information expected from an event sampled from that distribution
- This is the number of bits required to enconde (communicate) the outcomes of such distribution