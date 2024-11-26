# Family-Financial-Health-Scoring-Model
This project provides a FastAPI-based service to:
1-Calculate financial health scores for families based on provided financial data.
2-Generate and serve spending distribution graphs as PNG images.
3-Offer insights into financial performance and suggest improvements.

## Dependencies:
1-FastAPI: Web framework for building APIs.
2-Uvicorn: ASGI server for running FastAPI.
3-Matplotlib: For generating graphs.
4-NumPy: Numerical operations for scoring calculations.
5-Pydantic: Data validation and type enforcement.

Installation:
1-Install dependencies
2-Run application-
  Open terminal in the directory and type "uvicorn score_api:app --reload".
  Open the API documentation for interactive Swagger UI.

Steps for model creation:
1-Load and preprocess the dataset-
  Ensure data types are correct.
  Handle missing values if any.
2-Analyze patterns and correlations-
  Summarize spending by category and calculate savings-to-income ratios.
3-Build a scoring model-
  Normalize key metrics (e.g., savings-to-income ratio, goal achievement).
  Assign weights to each metric and compute a composite score (range: 0–100).
4-Visualize insights-
  Visualize Spending distribution across categories, Family-wise financial score distributions, Member-wise spending trends and Correlation   of financial metrics.

Features of Model
1-Data Analysis:
  Family-level and member-level spending patterns.
  Correlations between financial metrics.
2-Financial Health Score:
  Factors: Savings-to-income ratio, monthly expenses, loan payments, credit card spending, spending categories, and financial goals met.
  Normalized to a 0–100 range for easy interpretation.
3-Visualizations:
  Spending distribution by category to identify expense patterns.
  Family-level financial health scores to compare overall financial wellness.
  Member-level spending trends to pinpoint outliers or high spenders.

Scoring weights
1-Savings-to-Income Ratio (30%): Indicates the ability to save, a crucial factor in financial health.
2-Monthly Expenses (20%): High expenses relative to income lower the score, emphasizing budgeting.
3-Loan Payments (20%): A high loan burden impacts financial health negatively.
4-Credit Card Spending (10%): Excessive reliance on credit suggests poor financial habits.
5-Spending Categories (10%): Excessive spending on discretionary categories (e.g., travel, entertainment) reduces the score.
6-Financial Goals Met (10%): Indicates progress toward planned objectives.

Features of Scoring API:
Financial Score Calculation-
  1-Scores are computed based on savings, expenses, loans, credit card spending, and financial goals.
  2-Insights highlight areas of concern or confirm good financial health.

Recommendation Calculation-
  1-If savings are less than 20% of income, the function suggests increasing savings and calculates how much to save to meet the threshold.
  2-If expenses exceed 50% of income, the function suggests reducing expenses and calculates the potential score improvement.
  3-If loan payments exceed 30% of income, the function suggests reducing loan payments and estimates the impact on the score.
  4-If credit card spending exceeds 20% of income, it suggests lowering spending and calculates the potential score increase.

Spending Visualization-
  1-Generates a bar chart visualizing spending across categories.
  2-Graphs are served as downloadable PNG files.

Endpoints-
  1-POST /calculate-financial-score-and-graph/: Computes financial scores and returns insights along with the graph.
  2-GET /get-graph/: Returns the most recently generated spending graph.
  
