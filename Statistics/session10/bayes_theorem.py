# Task 1: Bayes' Posterior Function
def bayes_posterior(prior, likelihood, evidence):
    return (likelihood * prior) / evidence

# Example verification: prior = 0.01, likelihood = 0.9, evidence = 0.05
example_posterior = bayes_posterior(0.01, 0.9, 0.05)
print(f"Posterior Probability: {example_posterior:.4f}")


# Task 2: Swiggy Premium Restaurant Discount
# Prior: P(Premium) = 0.10, P(Regular) = 0.90
prior_premium = 0.10
prior_regular = 0.90

# Likelihood: P(Discount | Premium) = 0.80, P(Discount | Regular) = 0.20
likelihood_discount_given_premium = 0.80
likelihood_discount_given_regular = 0.20

# Evidence: Total probability of seeing a discount P(Discount)
evidence_discount = (likelihood_discount_given_premium * prior_premium) + (likelihood_discount_given_regular * prior_regular)

# Posterior: P(Premium | Discount) using Bayes' Theorem
posterior_premium_given_discount = (likelihood_discount_given_premium * prior_premium) / evidence_discount

print(f"P(Premium | Discount): {posterior_premium_given_discount:.4f}")


# Task 3: Spam Detection Filter for Word 'free'
emails = [
    ("win free cash now", "spam"),
    ("project meeting tomorrow", "ham"),
    ("get free coupon inside", "spam"),
    ("quarterly financial report", "ham"),
    ("claim your free gift", "spam"),
    ("lunch plans for friday", "ham"),
    ("free trial expires soon", "spam"),
    ("team sprint updates", "ham"),
    ("exclusive free spins bonus", "spam"),
    ("code review notes attached", "ham"),
    ("free sample delivery today", "spam"),
    ("flight ticket confirmation", "ham"),
    ("urgent free investment guide", "spam"),
    ("doctor appointment reminder", "ham"),
    ("get access to free movies", "spam"),
    ("weekly engineering sync", "ham"),
    ("collect your free reward", "spam"),
    ("monthly electricity bill", "ham"),
    ("free entry pass inside", "spam"),
    ("interview schedule details", "ham")
]

total_emails = len(emails)
spam_emails = [text for text, label in emails if label == "spam"]
ham_emails = [text for text, label in emails if label == "ham"]

# Prior probabilities
prior_spam = len(spam_emails) / total_emails
prior_ham = len(ham_emails) / total_emails

# Likelihoods: P('free' | Spam) and P('free' | Ham)
p_free_given_spam = sum(1 for text in spam_emails if "free" in text.lower()) / len(spam_emails)
p_free_given_ham = sum(1 for text in ham_emails if "free" in text.lower()) / len(ham_emails)

# Total Evidence: P('free')
evidence_free = (p_free_given_spam * prior_spam) + (p_free_given_ham * prior_ham)

# Posterior: P(Spam | 'free')
posterior_spam_given_free = (p_free_given_spam * prior_spam) / evidence_free

print(f" P(Spam | 'free'): {posterior_spam_given_free:.4f}")


# Task 4: Real-World Scenario (Instagram Ad Click / Bot Detection)
"""
Prompt Used:
"Generate a real-world numerical problem based on Bayes' Theorem related to Instagram account engagement, and provide the exact values for prior, likelihood, and false positive rates."

Scenario Generated:
On Instagram, 5% of registered profiles are automated bots.
A bot has an 85% chance of following more than 100 accounts in a single day.
A regular human user has only a 2% chance of following more than 100 accounts in a day.
Calculate the probability that an account is a bot given that it followed more than 100 accounts today.
"""

# Prior: P(Bot) = 0.05, P(Human) = 0.95
prior_bot = 0.05
prior_human = 0.95

# Likelihood: P(>100 follows | Bot) = 0.85, P(>100 follows | Human) = 0.02
likelihood_follow_given_bot = 0.85
likelihood_follow_given_human = 0.02

# Evidence: P(>100 follows)
evidence_follow = (likelihood_follow_given_bot * prior_bot) + (likelihood_follow_given_human * prior_human)

# Posterior: P(Bot | >100 follows)
posterior_bot_given_follow = (likelihood_follow_given_bot * prior_bot) / evidence_follow

print(f"P(Bot | >100 follows): {posterior_bot_given_follow:.4f}")