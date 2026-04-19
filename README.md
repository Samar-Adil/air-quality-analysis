# 🌫️ Air Quality Analysis

End-to-end data analysis of air quality dataset using Python, including EDA, data visualization, outlier detection, and statistical hypothesis testing.

---

## 📌 Project Objectives

1. Analyse pollution distribution using histogram
2. Compare pollution levels across different states
3. Study relationship between pollutant_max and pollutant_avg
4. Detect outliers using boxplot
5. Analyse pollution variation across cities (Bihar)
6. Identify relationships between variables using correlation heatmap
7. Perform hypothesis testing using Z-test

---

## 📊 Exploratory Data Analysis (EDA)

This section focuses on understanding pollution patterns, distribution, and relationships before applying statistical testing.

---

## 📉 Distribution of Pollution

![Histogram](images/histogram.png)

### 📌 Detailed Analysis

* The histogram shows how pollution values are distributed
* Most values are concentrated in the middle range
* Few values extend toward higher levels → indicates skewness

### 🎯 Insight

> Pollution levels are not evenly distributed, with most observations clustered in a moderate range and some extreme high values.

---

## 📊 Outlier Detection — Boxplot

![Boxplot](images/boxplot.png)

### 📌 Detailed Analysis

* The box represents the interquartile range (middle 50% of data)

* Median line shows central tendency

* Points outside whiskers are outliers

* Presence of outliers indicates:

  * Extreme pollution levels
  * Possible environmental anomalies

### 🎯 Insight

> Outliers highlight locations or conditions where pollution is significantly higher than normal.

---

## 📊 State-wise Pollution Comparison

![Bar Chart](images/bar_chart.png)

### 📌 Detailed Analysis

* Each bar represents a state
* Height shows average pollution level
* Clear variation across states

### 🎯 Insight

> Pollution is unevenly distributed geographically, with some states consistently showing higher levels.

---

## 📈 Relationship — Pollutant Max vs Avg

![Scatter Plot](images/scatter.png)

### 📌 Detailed Analysis

* Points show relationship between maximum and average pollution

* Upward trend indicates strong positive relationship

* As maximum pollution increases:

  * Average pollution also increases

### 🎯 Insight

> pollutant_max is a strong indicator of overall pollution levels.

---

## 📊 Correlation Analysis — Heatmap

![Heatmap](images/heatmap.png)

### 📌 Detailed Analysis

* Shows correlation between numerical variables

* Values close to +1 → strong positive relationship

* Values close to 0 → weak relationship

* pollutant_max and pollutant_avg show strong correlation

### 🎯 Insight

> Pollution variables are interconnected, especially max and average values.

---

## 📍 City-wise Analysis — Bihar

![Bihar Cities](images/bihar_plot.png)

### 📌 Detailed Analysis

* Each point represents a city in Bihar

* Shows variation in pollution across cities

* Some cities have:

  * Significantly higher pollution levels
  * Large variation compared to others

### 🎯 Insight

> Pollution varies even within a single state, highlighting local environmental differences.

---

## 🧪 Hypothesis Testing (Z-Test)

### Hypothesis

* *H0 (Null Hypothesis):* Mean of pollutant_max = Mean of pollutant_avg
* *H1 (Alternative Hypothesis):* Mean of pollutant_max ≠ Mean of pollutant_avg

### 📌 Test Details

* Z-test used to compare means of two variables
* P-value used to determine significance

### 📊 Result

* If p-value < 0.05 → Reject H0
* Indicates significant difference between variables

### 🎯 Insight

> Statistical testing confirms that differences in pollution metrics are meaningful and not due to random variation.

---

## 🧠 Key Analytical Insights

* Pollution levels show clear variation across states
* Outliers represent extreme environmental conditions
* Strong relationship exists between pollutant_max and pollutant_avg
* Pollution distribution is not uniform
* City-level analysis reveals deeper local insights
* Statistical testing validates observed patterns

---

## 🚀 Conclusion

* Pollution is not randomly distributed
* Certain states and cities are more affected
* Maximum pollution strongly influences average levels
* Data analysis and statistical testing provide reliable insights
