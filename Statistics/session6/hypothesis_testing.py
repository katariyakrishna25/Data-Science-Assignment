# Statistics Session 6 - Hypothesis Testing

# Task 1: Null and Alternative Hypothesis

# H0: People do not spend more time on Instagram than on YouTube daily.
# H1: People spend more time on Instagram than on YouTube daily.


# Task 2: Two-Sample T-Test

# Group A: New Zomato home page
# Mean = ₹350, SD = ₹50, n = 30
#
# Group B: Old Zomato home page
# Mean = ₹320, SD = ₹50, n = 30

from scipy.stats import ttest_ind_from_stats

result = ttest_ind_from_stats(
    mean1=350, std1=50, nobs1=30,
    mean2=320, std2=50, nobs2=30,
    equal_var=True
)

print("t-statistic:", result.statistic)
print("p-value:", result.pvalue)

# Since p-value is greater than 0.05, we do not reject H0.
# There is not enough evidence to say that the new home page
# significantly increased the average order value.


# Task 3: A/B Testing

# Feature: New dark mode in WhatsApp

# Control Group: Users using the existing light mode.
# Variant Group: Users using the new dark mode.
# Metric: Daily active usage time.

# H0: Dark mode does not increase daily usage time.
# H1: Dark mode increases daily usage time.


# Task 4: Flipkart Wishlist Button

# New button clicks = 520
# Old button clicks = 480

# The difference is 40 clicks out of 1000 users.
# Without a statistical test, we cannot say for sure that the
# difference is significant.

# The p-value helps decide whether the observed difference is
# likely due to chance. If p-value < 0.05, we reject H0.
# If p-value >= 0.05, we do not reject H0.
