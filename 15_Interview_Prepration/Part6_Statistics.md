# **mean, median, and mode**

## 📊 Concepts

- **Mean (Average):**  
  Sum of all values divided by the number of values.  
  Example: For {1, 2, 3, 4, 5}, mean = (1+2+3+4+5)/5 = 3.

- **Median (Middle Value):**  
  The middle value when data is sorted.  
  - Odd count → middle element.  
  - Even count → average of two middle elements.  
  Example: For {1, 2, 3, 4}, median = (2+3)/2 = 2.5.

- **Mode (Most Frequent Value):**  
  The value(s) that occur most often.  
  Example: For {1, 2, 2, 3, 4}, mode = 2.  
  For {1, 1, 2, 3, 3}, modes = 1 and 3 (bimodal). 

---

## 🧮 Step‑by‑Step Logic

- **Mean:**  
  Add all numbers → divide by count.

- **Median:**  
  Sort the list →  
  - If odd length → middle element.  
  - If even length → average of two middle elements.

- **Mode:**  
  Count frequency of each number → return the one(s) with highest frequency.

---

## 🐍 Python Implementation (No Built‑ins)

```python
# Custom functions for mean, median, mode

def calc_mean(data):
    total = 0
    count = 0
    for num in data:
        total += num
        count += 1
    return total / count

def calc_median(data):
    # Sort manually (simple bubble sort for clarity)
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid-1] + arr[mid]) / 2
    else:
        return arr[mid]

def calc_mode(data):
    freq = {}
    for num in data:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_count = 0
    modes = []
    for num, count in freq.items():
        if count > max_count:
            max_count = count
            modes = [num]
        elif count == max_count:
            modes.append(num)
    
    return modes

# Example usage
data = [1, 2, 2, 3, 4, 5, 5]

print("Mean:", calc_mean(data))
print("Median:", calc_median(data))
print("Mode:", calc_mode(data))
```

---

## 🔎 Sample Output
For `data = [1, 2, 2, 3, 4, 5, 5]`:
- **Mean:** 3.14  
- **Median:** 3  
- **Mode:** [2, 5] (bimodal)

---

# Variance

Variance is a **measure of how spread out the data is** around the mean. It tells you how much the values differ from the average.  

---

## 📊 Concept

- **Mean (μ):** Average of the data.  
- **Deviation:** Difference between each value and the mean.  
- **Variance (σ²):** Average of squared deviations.  

\[
\sigma^2 = \frac{\sum (x_i - \mu)^2}{n}
\]

- If variance is **small**, data points are close to the mean.  
- If variance is **large**, data points are spread out.  

---

## 🐍 Python Code (Without Built‑ins)

```python
def calc_mean(data):
    total = 0
    count = 0
    for num in data:
        total += num
        count += 1
    return total / count

def calc_variance(data):
    mean = calc_mean(data)
    squared_diff_sum = 0
    count = 0
    for num in data:
        squared_diff_sum += (num - mean) ** 2
        count += 1
    return squared_diff_sum / count   # Population variance

# Example usage
data = [2, 4, 6, 8, 10]

print("Mean:", calc_mean(data))
print("Variance:", calc_variance(data))
```

---

## 🔎 Example Output
For `data = [2, 4, 6, 8, 10]`:
- **Mean = 6**  
- **Variance = 8**  

---

# Standard Deviation

## 📊 Concept

- **Variance (σ²):** Average of squared deviations from the mean.  
- **Standard Deviation (σ):** Square root of variance.  

\[
\sigma = \sqrt{\sigma^2}
\]

It’s more intuitive than variance because it’s in the **same units** as the original data.  
Example: If your dataset is in kilograms, variance is in kg², but standard deviation is back in kg.

---

## 🐍 Python Code (Without Built‑ins)

```python
def calc_mean(data):
    total = 0
    count = 0
    for num in data:
        total += num
        count += 1
    return total / count

def calc_variance(data):
    mean = calc_mean(data)
    squared_diff_sum = 0
    count = 0
    for num in data:
        squared_diff_sum += (num - mean) ** 2
        count += 1
    return squared_diff_sum / count   # Population variance

def calc_std_dev(data):
    variance = calc_variance(data)
    return variance ** 0.5   # Square root of variance

# Example usage
data = [2, 4, 6, 8, 10]

print("Mean:", calc_mean(data))
print("Variance:", calc_variance(data))
print("Standard Deviation:", calc_std_dev(data))
```

---

## 🔎 Example Output
For `data = [2, 4, 6, 8, 10]`:
- **Mean = 6**  
- **Variance = 8**  
- **Standard Deviation ≈ 2.828**

---

👉 Quick note:  
- Divide by `n` → **Population standard deviation**.  
- Divide by `n-1` → **Sample standard deviation** (used when data is a sample of a larger population).  

---
Standard deviation tells you **how much the data values deviate from the mean on average**. It’s essentially a measure of **spread or dispersion** in the same units as your data.  

---

## 📊 Intuition
- **Small standard deviation:** Data points are tightly clustered around the mean.  
  Example: Exam scores {49, 50, 51} → mean ≈ 50, std. dev. ≈ 1.  
- **Large standard deviation:** Data points are widely spread out.  
  Example: Exam scores {10, 50, 90} → mean ≈ 50, std. dev. ≈ 40.  

So, it tells you whether your dataset is **consistent** or **variable**.  

---

## 🧠 Why It Matters
- In statistics: Helps understand variability in experiments.  
- In finance: Used to measure risk (volatility of returns).  
- In machine learning: Guides normalization and feature scaling.  

---

# Variance Vs Standard Deviation

Standard deviation tells you **how much the data values deviate from the mean on average**. It’s essentially a measure of **spread or dispersion** in the same units as your data.  

---

## 📊 Intuition
- **Small standard deviation:** Data points are tightly clustered around the mean.  
  Example: Exam scores {49, 50, 51} → mean ≈ 50, std. dev. ≈ 1.  
- **Large standard deviation:** Data points are widely spread out.  
  Example: Exam scores {10, 50, 90} → mean ≈ 50, std. dev. ≈ 40.  

So, it tells you whether your dataset is **consistent** or **variable**.  

---

## 🧠 Why It Matters
- In statistics: Helps understand variability in experiments.  
- In finance: Used to measure risk (volatility of returns).  
- In machine learning: Guides normalization and feature scaling.  

---

## 🐍 Python Example (No Built‑ins)

```python
def calc_mean(data):
    total = 0
    for num in data:
        total += num
    return total / len(data)

def calc_variance(data):
    mean = calc_mean(data)
    squared_diff_sum = 0
    for num in data:
        squared_diff_sum += (num - mean) ** 2
    return squared_diff_sum / len(data)   # Population variance

def calc_std_dev(data):
    variance = calc_variance(data)
    return variance ** 0.5   # Square root of variance

# Example usage
data = [10, 50, 90]

print("Mean:", calc_mean(data))
print("Variance:", calc_variance(data))
print("Standard Deviation:", calc_std_dev(data))
```

---

## 🔎 Output
For `data = [10, 50, 90]`:
- **Mean = 50**  
- **Variance = 1066.67**  
- **Standard Deviation ≈ 32.68**  

This shows the scores are **widely spread** around the mean.  

---

## 📊 What Variance (1066.67) Represents
- Variance is the **average of squared deviations** from the mean.  
- In your dataset `{10, 50, 90}`, the mean is **50**.  
- Each point’s deviation from the mean is:  
  - \(10 - 50 = -40\)  
  - \(50 - 50 = 0\)  
  - \(90 - 50 = 40\)  
- Squaring those deviations:  
  - \((-40)^2 = 1600\)  
  - \(0^2 = 0\)  
  - \(40^2 = 1600\)  
- Average of these = \(\frac{1600 + 0 + 1600}{3} = 1066.67\).  

---

## 🧠 Interpretation
- That **1066.67** is telling you: *“On average, the squared distance of each data point from the mean is about 1066.67.”*  
- It’s a **mathematical measure of spread**.  
- The squaring makes sure deviations don’t cancel out (negative vs positive), but it also makes the number less intuitive.  

That’s why we take the square root → **standard deviation ≈ 32.68**.  
Now we can say: *“On average, each data point lies about 33 units away from the mean.”*  

---

## 🎯 Key Takeaway
- **Variance (1066.67):** Spread in squared units, useful for math/statistics.  
- **Standard deviation (32.68):** Spread in original units, useful for interpretation.  

---

# Covariance

Covariance is a statistical measure that tells you **how two variables change together**.  

---

## 📊 Concept
- If two variables **increase together**, covariance is **positive**.  
- If one increases while the other decreases, covariance is **negative**.  
- If they are independent, covariance is close to **zero**.  

Mathematically:

\[
\text{Cov}(X, Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n}
\]

Where:  
- \(x_i, y_i\) = data points  
- \(\bar{x}, \bar{y}\) = means of X and Y  
- \(n\) = number of data points  

---

## 🧠 Intuition
- **Positive covariance:** Taller people tend to weigh more → height ↑, weight ↑.  
- **Negative covariance:** More hours partying → lower exam scores → hours ↑, scores ↓.  
- **Zero covariance:** Shoe size and salary → no relationship.  

---

## 🐍 Python Code (Without Built‑ins)

```python
def calc_mean(data):
    return sum(data) / len(data)

def calc_covariance(x, y):
    if len(x) != len(y):
        raise ValueError("Datasets must be same length")
    
    mean_x = calc_mean(x)
    mean_y = calc_mean(y)
    
    cov_sum = 0
    for i in range(len(x)):
        cov_sum += (x[i] - mean_x) * (y[i] - mean_y)
    
    return cov_sum / len(x)   # Population covariance

# Example usage
X = [2, 4, 6, 8]
Y = [5, 10, 15, 20]

print("Covariance:", calc_covariance(X, Y))
```

---

## 🔎 Example Output
For `X = [2,4,6,8]` and `Y = [5,10,15,20]`:  
- Covariance = **12.5** (positive → they increase together).  

---
# Conditional probability 

Conditional probability is the probability of an event **A** happening given that another event **B** has already occurred.  

---

## 📊 Definition

\[
P(A|B) = \frac{P(A \cap B)}{P(B)}
\]

Where:  
- \(P(A|B)\) → Probability of A given B  
- \(P(A \cap B)\) → Probability that both A and B occur  
- \(P(B)\) → Probability of B  

---

## 🧠 Intuition
- It answers: *“What’s the chance of A happening, knowing that B has already happened?”*  
- Example:  
  - Probability of drawing a red card = 26/52 = 0.5  
  - Probability of drawing a face card = 12/52 ≈ 0.23  
  - Probability of drawing a red face card = 6/52 ≈ 0.115  
  - Then:  
    \[
    P(\text{Red | Face}) = \frac{6/52}{12/52} = 0.5
    \]  
  So, given the card is a face card, the chance it’s red is **50%**.

---

## 🐍 Python Code (Without Built‑ins)

```python
def conditional_probability(event_a, event_b, sample_space):
    # event_a, event_b, sample_space are sets
    intersection = event_a.intersection(event_b)
    prob_b = len(event_b) / len(sample_space)
    prob_a_given_b = len(intersection) / len(event_b)
    return prob_a_given_b

# Example: Deck of cards simplified
sample_space = set(range(1, 53))  # 52 cards
red_cards = set(range(1, 27))     # first 26 = red
face_cards = {11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52}  # 12 face cards

print("P(Red | Face):", conditional_probability(red_cards, face_cards, sample_space))
```

---

## 🔎 Output
- **P(Red | Face) = 0.5**  
Meaning: If you already know the card is a face card, there’s a 50% chance it’s red.  

---

# Bayes’ Theorem

---

## 📊 Bayes’ Theorem Formula

![alt text](Bayes.png)

\[
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
\]

Where:  
- \(P(A|B)\) → Probability of A given B (posterior)  
- \(P(B|A)\) → Probability of B given A (likelihood)  
- \(P(A)\) → Prior probability of A  
- \(P(B)\) → Marginal probability of B  

---

proof Bayes Theoram

![alt text](bayesproof.png)

## 🧠 Intuition
Bayes’ Theorem lets you **update your beliefs** when new evidence arrives.  

- **Prior:** What you believed before seeing evidence.  
- **Likelihood:** How consistent the evidence is with your hypothesis.  
- **Posterior:** Updated belief after considering the evidence.  

---

## 🎯 Example
Suppose:  
- 1% of people have a disease → \(P(Disease) = 0.01\).  
- Test is 95% accurate → \(P(Positive|Disease) = 0.95\).  
- False positive rate = 5% → \(P(Positive|NoDisease) = 0.05\).  

Now, if someone tests positive, what’s the chance they actually have the disease?

\[
P(Disease|Positive) = \frac{0.95 \cdot 0.01}{(0.95 \cdot 0.01) + (0.05 \cdot 0.99)}
\]

\[
= \frac{0.0095}{0.0095 + 0.0495} \approx 0.16
\]

So even with a positive test, the chance of having the disease is only **16%**, because the disease is rare.

---

## 🐍 Python Code (No Built‑ins)

```python
def bayes_theorem(prior_a, likelihood_b_given_a, prob_b):
    return (likelihood_b_given_a * prior_a) / prob_b

# Example: disease test
prior_disease = 0.01
likelihood_positive_given_disease = 0.95
prob_positive = (0.95 * 0.01) + (0.05 * 0.99)

posterior = bayes_theorem(prior_disease, likelihood_positive_given_disease, prob_positive)
print("P(Disease | Positive):", posterior)
```

---

## 🔎 Output
- **P(Disease | Positive) ≈ 0.16**  
Meaning: Even with a positive test, the probability is only 16% because the disease is rare.

---

## 🎯 Example
Conditional probability:
“Given a card is a face card, what’s the chance it’s red?” → direct calculation.

Bayes’ Theorem:
“Given a positive medical test, what’s the chance the person has the disease?”
Here, you don’t know  𝑃(𝐷𝑖𝑠𝑒𝑎𝑠𝑒∣𝑃𝑜𝑠𝑖𝑡𝑖𝑣𝑒) directly, but you know:
- Prior probability of disease
- Likelihood of a positive test if disease is present
- Probability of a positive test overall Bayes’ Theorem combines these to give the posterior probability.

# Independent Event and Mutually Exclusive Events

Let’s carefully distinguish **independent events** and **mutually exclusive events** — two concepts that often get confused but are actually very different.

---

## 🎲 Independent Events
- **Definition:** Two events are independent if the occurrence of one does **not affect** the probability of the other.  
- **Formula:**  
  \[
  P(A \cap B) = P(A) \cdot P(B)
  \]
- **Example:**  
  - Tossing a coin and rolling a die.  
    - Probability of heads = 0.5  
    - Probability of rolling a 4 = 1/6  
    - Probability of both = \(0.5 \times \frac{1}{6} = \frac{1}{12}\).  
  The coin toss doesn’t influence the die roll → independent.

---

## 🚫 Mutually Exclusive Events
- **Definition:** Two events are mutually exclusive if they **cannot happen at the same time**.  
- **Formula:**  
  \[
  P(A \cap B) = 0
  \]
- **Example:**  
  - Drawing a single card:  
    - Event A = card is a heart  
    - Event B = card is a spade  
    - You can’t draw one card that is both a heart and a spade → mutually exclusive.

---

## 🔑 Key Difference
| Aspect | Independent Events | Mutually Exclusive Events |
|--------|--------------------|---------------------------|
| Relationship | One event does not affect the other | Events cannot occur together |
| Formula | \(P(A \cap B) = P(A) \cdot P(B)\) | \(P(A \cap B) = 0\) |
| Example | Coin toss & die roll | Drawing a heart vs spade in one card |

---

## 🧠 Intuition
- **Independent:** Events can both happen, but they don’t influence each other.  
- **Mutually exclusive:** Events cannot both happen at all.  

👉 Important: Mutually exclusive events are **not independent** (except in trivial cases). If two events can’t occur together, knowing one occurred completely determines the other didn’t — so they are dependent.

---

# Law Of Total Probability

The **Law of Total Probability** is a fundamental rule in probability theory that helps you compute the probability of an event by breaking it down across all possible scenarios (or partitions of the sample space).  

---

## 📊 Formal Definition
Suppose the sample space is divided into mutually exclusive and exhaustive events \(B_1, B_2, \dots, B_n\).  
Then for any event \(A\):

\[
P(A) = \sum_{i=1}^{n} P(A|B_i) \cdot P(B_i)
\]

- \(B_1, B_2, \dots, B_n\) → a complete set of scenarios (they cover all possibilities and don’t overlap).  
- \(P(A|B_i)\) → probability of \(A\) given scenario \(B_i\).  
- \(P(B_i)\) → probability of scenario \(B_i\).  

---

## 🧠 Intuition
It says: *“To find the probability of A, consider all the different ways A can happen, weighted by how likely each scenario is.”*  

Think of it as **assembling the whole probability from its parts**.

---

## 🎯 Example: Medical Test
- Population split:  
  - 1% have the disease (\(B_1\))  
  - 99% don’t have the disease (\(B_2\))  

- Probability of a positive test:  
  - If diseased: \(P(Positive|B_1) = 0.95\)  
  - If healthy: \(P(Positive|B_2) = 0.05\)  

By the law of total probability:

\[
P(Positive) = P(Positive|Disease) \cdot P(Disease) + P(Positive|NoDisease) \cdot P(NoDisease)
\]

\[
= (0.95 \cdot 0.01) + (0.05 \cdot 0.99) = 0.059
\]

So overall, **5.9% of tests are positive**.

---

## 🔑 Why It Matters
- It’s the **foundation for Bayes’ Theorem** (since Bayes needs \(P(B)\), which often comes from this law).  
- Used in risk analysis, machine learning, and decision theory.  
- Helps when probabilities are easier to compute in parts than directly.  

---

![alt text](totalprobability.png)

Here’s the diagram you asked for — it shows the **Law of Total Probability** visually, with the sample space split into partitions \(B_1, B_2, B_3, \dots, B_n\), and each branch leading to outcomes \(A\) or \(\neg A\). At the bottom, the formula is summarized as the weighted sum of all scenarios.  

---

## 🧠 How to Read This Diagram
- The **sample space** is divided into mutually exclusive events \(B_1, B_2, B_3, \dots, B_n\).  
- From each partition, you branch into two outcomes: \(A\) (event happens) or \(\neg A\) (event does not happen).  
- Each branch has a conditional probability \(P(A|B_i)\) or \(P(\neg A|B_i)\).  
- To get the total probability of \(A\), you **add up all the weighted contributions**:  
  \[
  P(A) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) + \dots + P(A|B_n)P(B_n)
  \]

---

Here’s how **Bayes’ Theorem** connects directly to the **Law of Total Probability** — they’re two sides of the same reasoning process.

---

## 🔗 Relationship Between the Two

Bayes’ Theorem:
\[
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
\]

But notice that \(P(B)\) — the denominator — is often **hard to compute directly**.  
That’s where the **Law of Total Probability** comes in:

\[
P(B) = \sum_{i=1}^{n} P(B|A_i) \cdot P(A_i)
\]

So Bayes’ Theorem actually *depends* on the Law of Total Probability to find \(P(B)\).  
It’s like the law provides the “normalizing factor” that makes all probabilities add up correctly.

---

## 🧠 Intuitive Connection
Imagine you’re diagnosing a disease based on a test result:
- You want \(P(Disease|Positive)\) → Bayes’ Theorem.
- But to compute it, you need \(P(Positive)\) → Law of Total Probability.

You calculate \(P(Positive)\) by considering **all possible causes** of a positive result:
- Positive because of disease  
- Positive because of false alarm  

Then plug that into Bayes’ formula to get the **posterior probability**.

---

## 🎯 Summary
| Concept | Purpose | Formula |
|----------|----------|----------|
| **Law of Total Probability** | Breaks down overall probability into parts | \(P(B) = \sum P(B|A_i)P(A_i)\) |
| **Bayes’ Theorem** | Updates belief using evidence | \(P(A|B) = \frac{P(B|A)P(A)}{P(B)}\) |

Together, they form the backbone of **statistical inference** — one decomposes probabilities, the other reverses and updates them.

---

![alt text](totalprobability_2.png)

Here’s the combined visual you asked for — it shows how **Bayes’ Theorem** and the **Law of Total Probability** fit together beautifully.  

At the top, Bayes’ Theorem highlights the four components:  
- **Prior** (\(P(A)\)) — your initial belief  
- **Likelihood** (\(P(B|A)\)) — how consistent the evidence is with that belief  
- **Evidence** (\(P(B)\)) — the overall probability of observing the evidence  
- **Posterior** (\(P(A|B)\)) — your updated belief after seeing the evidence  

Then, the lower section illustrates how the **Law of Total Probability** expands \(P(B)\) into all possible causes or partitions (\(A_1, A_2, A_3, \dots, A_n\)).  

So, the law provides the denominator for Bayes’ Theorem — the “normalizing” term that ensures all probabilities sum to 1.  

In short:  
- **Law of Total Probability** → breaks down evidence across all scenarios.  
- **Bayes’ Theorem** → uses that breakdown to update beliefs rationally.  

# What is Center Limit Theory

The **Central Limit Theorem (CLT)** is one of the most powerful and beautiful results in statistics — it explains *why so many real‑world phenomena follow a normal (bell‑shaped) distribution*, even when the underlying data doesn’t.

---

## 📊 Formal Statement
If you take **many independent random samples** from any population (with finite mean and variance), then as the sample size \(n\) grows large:

\[
\text{The distribution of the sample mean } \bar{X} \text{ approaches a normal distribution.}
\]

Mathematically:

\[
\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)
\]

Where:  
- \(\mu\) = population mean  
- \(\sigma^2\) = population variance  
- \(n\) = sample size  

---

## 🧠 Intuition
Imagine drawing repeated samples from any population — even one that’s skewed or irregular (like income, rainfall, or reaction time).  
Each sample has a mean.  
If you plot those means, the shape of that plot becomes **bell‑shaped** as \(n\) increases.

So, the CLT says: *“No matter what the original distribution looks like, the averages of large samples will behave normally.”*

---

## 🎯 Why It Matters
- It allows us to use **normal‑distribution methods** (z‑scores, confidence intervals, hypothesis tests) even when the population isn’t normal.  
- It’s the foundation of **inferential statistics** — the reason we can make predictions and decisions from sample data.  

---

## 🧩 Example
Suppose you measure the daily number of website visits (which might be skewed).  
If you take 100‑day samples and compute their average visits, those averages will form a nearly normal curve — centered around the true mean visits per day.

---

## 🔑 Key Takeaway
- The CLT connects randomness to order.  
- It explains why the **normal distribution** appears everywhere — in heights, test scores, errors, and averages.  

---

Here’s a visual way to understand the **Central Limit Theorem (CLT)**:

![alt text](CLT.png)

Imagine you start with a population that is **not normal** — maybe it’s skewed, like income distribution or daily website visits.  

- 🎲 **Step 1:** Take a small sample (say, 5 observations) and compute its mean. Do this many times. The distribution of those means looks irregular.  
- 🎲 **Step 2:** Increase the sample size (say, 30 observations each). Now the distribution of sample means starts to smooth out.  
- 🎲 **Step 3:** With large samples (say, 100+ observations), the distribution of sample means becomes **bell‑shaped (normal)**, centered around the true population mean.  

So the CLT shows that **averages of samples tend toward a normal distribution**, no matter how the original data looks — as long as the population has a finite mean and variance.

---

## 🔑 Why This Is Powerful
- It explains why the **normal distribution** appears everywhere in statistics.  
- It allows us to use z‑scores, confidence intervals, and hypothesis tests even when the raw data isn’t normal.  
- It’s the backbone of inferential statistics — turning messy real‑world data into something predictable.

---