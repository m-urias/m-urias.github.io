# Money and Banking

**By [Marshall Urias](https://m-urias.github.io) 🚀**

Welcome to my Money and Banking course site.  Included here are lectures and data tutorials presented in a Jupyter Book.  Lectures provide theoretical models related to money, assets, banking, and monetary policy.  Data tutorials are intended to show students what economic databases are publicly available, how to acquire data, and how to analyze the data using Python.  

## Course Overview

This course focuses on monetary theory, financial intermediation, and central bank policy. The first part of the curriculum develops a theoretical framework used to explain the
existence of money and banks. Our theory demonstrates key relationships between the availability of liquid assets, inflation, output, and regulations imposed on banks. Second, we discuss the real world business of banking which includes deposit creation, fractional reserve banking, and the interbank market. Third, we discuss the role of central banks in modern economies and analyze the conduct of monetary policy through tools such as the reserve requirement, lending facilities, short-term interest rates, and quantitative easing.

Below is a table of contents for the course content.  This table of contents can also be conveniently navigated on the left hand panel. 

### Overlapping Generations Model of Money, Inflation, and Assets
- [OLG Model of Money](olg_model.ipynb) – This lecture introduces the overlapping generations (OLG) framework and explores what features of an economy are necessary to give rise to fiat currency.  We then analyze under what conditions fiat currency has value and explore long-run relationships between money, inflation, and interest rates.  We also consider the degree to which fiat currency can coexist with alternative interest-bearing assets and discuss optimal monetary policy. 
    - [Technical Details of our OLG model](olg-model-details.ipynb) - We explore properties of the money demand function derived under our OLG model and provide examples of stationary and non-stationary equilibria. We also discuss the local stability of monetary and non-monetary equilibria.
    - [The Role of Expectations in OLG Dynamics](olg-expectations.ipynb) - We show how our monetary equilibria behaves differently under three different forecasting rules: perfect foresight, adaptive expectations, and rational expectations.
    - [Monetary Aggregates Data Turorial](monetary-aggregates-data-tutorial.ipynb) - We show how to download data from the Federal Reserve Economic Data (FRED) using an API in Python and then provide descriptive statistics for monetary aggregates in the US.
    - [Some Empirical Monetary Facts](monetary-facts.ipynb) - We analyze the empirical relationship between money, inflation, and output using Python. 
- [Government Spending and Monetary Policy](government-money.ipynb) - We introduce a government sector into the OLG model in order to explore the trade-offs between printing money for government revenue and providing public goods.  We also discuss the seminal paper by Sargent and Wallace that explore the degree to which monetary policy remains effective when interacting with a fiscal authority.
    [An Example of a Monetary OLG Model with a Government](olg-government-example.ipynb) - We explore a numerical example of our OLG economy with a government to show a Laffer curve relationship between money creation and government revenue, multiplicity of equilibria, and the dynamics of the economy toward a stable monetary equilibria as well as a monetary collapse. 
- [OLG Model of Banking](olg-banking.ipynb) – Foundational relationships between inside money, outside money, and monetary policy.

- [Empirical Monetary Facts](monetary-facts.ipynb) - We describe how banks provide liquidity to households in our OLG model.  We explore the relationship between bank deposits and fiat currency as well as how central bank policies can effect nominal and real variables in our economy.  
- [Diamond-Dybvig Model of Banking](diamond-dybvig.ipynb) - We discuss liquidity role of banks from the perspective of Diamond and Dybvig.  We identify how banks provide insurance against liquidity shocks and why bank runs can be an equilibrium phenomena.

### Interbank Market and Monetary Policy
- [Bank Balance Sheets](bank-balance-sheets.ipynb) - We review how banks record common transactions in their balance sheet.  We use T-accounts to discuss how a hypothetical bank starts operations, generates profits through creating loans and investing in securities, and engages in open market operations with the central bank.  We also discuss the importance of reserves and capital adequacy standards for maintaining stability in the banking system.  
- [Term Structure of Interest Rates](term-structure-of-interest-rates.ipynb) - An introduction to the term structure of interest rates.  Our primary theory is the liquidity augmented expectations theory of the term structure of interest rates.
    -[Yield Curve Data Tutorial](yield-curve-data-tutorial.ipynb) - We use Python to analyze relationships between short- and long-rates implies by our theory of the term structure.
- [Monetary Policy Systems](monetary-policy-systems.ipynb) - We build a model of the interbank market for reserves and discuss how the US and China conduct monetary policy by interventions in this market.  We also elucidate the different between the floor and corridor monetary policy systems.

### A Simple Model of Monetary Policy Transmission
- [Measuring Business Cycles](measuring-business-cycles.ipynb) - We define the difference between short-run and long-run within an economic context.
    - [Extracting Business Cycles from Time Series](extracting-business-cycles.ipynb) - We review the statistical methods of filtering and use Python to extract business cycles from data on real GDP for the US. 
- [A Macro Model of Monetary Policy Transmission](macro-model.ipynb) - We build a simple three equation macro model (IS-MP-PC) that shows the effects of monetary policy.  Our model is demonstrates the short-run dynamics of the economy and includes an optimal monetary policy rule (e.g. a Taylor rule) which responds to economic conditions in real-time.

---

### Resources
- [Syllabus (PDF)](../money%20and%20banking/syllabus.pdf)  
- [Additional readings](../assets/readings.html)

---


