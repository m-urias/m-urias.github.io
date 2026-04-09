# Macroeconomic Analysis

**By [Marshall Urias](https://m-urias.github.io) 🚀**

Welcome to my Macroeconomic Analysis course site.  Included here are lectures and data tutorials presented in a Jupyter Book.  Lectures provide theoretical models quantitative methods for understanding economies with search frictions.  Data tutorials are intended to show students what economic databases are publicly available, how to acquire data, and how to analyze the data using Python.  

## Course Overview

This course studies theoretical and quantitative approaches to understanding economies with search frictions in goods, labor, and financial markets. This departure from classical equilibrium theory generates many interesting phenomena such as unemployment, pricing strategies, production capacity choices, bargaining over financial contracts, insurance, and business cycles. We then develop tools for analyzing the dynamics (both local and global) of macroeconomies characterized by market imperfections, and glean insights for financial and fiscal multipliers, the
formation of prices and wages, the dynamics of the labor market, efficiency, and policies. Underlying all this analysis are implications for how search frictions alter our understanding of the macroeconomy relative to the neoclassical view.

Below is a table of contents for the course content.  This table of contents can also be conveniently navigated on the left hand panel. 

### The Labor Market: Macroeconomics of Search and Unemployment
- [Equilibrium Unemployment](equilibrium-unemployment.ipynb) – This lecture introduces the search theoretic approach to the labor market.  We model how aggregate labor market outcomes, such as unemployment, job vacancies, and wages are determined as equilibrium phenomena.  We then use the model to explain how labor market fluctuations can generate business cycles and long-run growth.
    - [Poisson Process and the Value of an Asset](poisson-process.ipynb) - A derivation of the value functions used in the labor market model based on Poisson processes.
    - [Nash Bargaining and Wage Determination](nash-bargaining.ipyng) - An introduction to bilateral Nash bargaining.  A tool used extensively in search theory.
    - [Labor Search Extensions](model-extensions.ipynb) - Here we present common modeling extensions to the baseline model which can be used to answer complimentary questions as well as enrich the ability of the model to match data moments.
- [Labor Market Dynamics](labor-dynamics.ipynb) - This lecture shows how to qualitatively and quantitatively characterize out-of-steady state dynamics in our search theoretic model of the labor market.  First, we use analytical tools from differential calculus to describe the behavior of the economy away from steady state.  Second, we develop a discrete time version of the model that can be calibrated to US data.
    - [Linearization](linearization.ipynb) - A review of linearization techniques.  Uhlig's method is developed and used as the standard way to log-linearize our model for calibration.
    - [Discretization](discrete-model.ipynb) - A formal derivation of the discrete-time version of the model.
    - [Extracting Business Cycles](extracting-business-cycles.ipynb) - We review the statistical methods of filtering and use Python to extract business cycles from data on real GDP for the US. 

### The Financial Market: Credit Frictions and Financial Multipliers
- [Frictional Credit Market](credit-market.ipynb) - We extend the labor market model to include a credit market subject to similar search frictions as the labor market.  We investigate how these credit frictions amplify shocks to business cycles and measure this amplification by financial multipliers.  
- [Efficiency in Search](market-efficiency.ipynb) - We identify the efficient allocation in an economy with search frictions and show how competitive search can induce such an outcome.  We then investigate how policies can push a search economy toward efficient outcomes.
- [Financial Frictions in Macroeconomics](financial-frictions.ipynb) - We describe common modeling approaches to incorporating financial frictions into macroeconomic models, and investigate their implications for improving business cycle explanations.

---

### Resources
- [Syllabus (PDF)](../money%20and%20banking/syllabus.pdf)  
- [Syllabus (PDF)](../assets/readings.html)

---


