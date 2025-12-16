# Family Financial Health Scoring Model
This project implements a Family Financial Health Scoring system that evaluates a household’s financial stability based on income, savings, expenses, loans, credit card usage, spending behavior, and financial goal completion.

The project includes:

- Data analysis & scoring logic (Jupyter Notebook)
- FastAPI-based REST API to calculate scores, generate insights, and visualize spending patterns

## Project Overview
The system calculates a composite Financial Health Score using weighted financial indicators and provides:
- Individual metric scores
- Overall financial health score
- Actionable insights & recommendations
- Spending distribution visualization

## Key Financial Factors Used
| Factor                  | Description                            |
| ----------------------- | -------------------------------------- |
| Income                  | Total household income                 |
| Savings                 | Total savings                          |
| Monthly Expenses        | Regular household expenses             |
| Loan Payments           | EMI / loan obligations                 |
| Credit Card Spending    | Monthly credit card usage              |
| Financial Goals Met (%) | Progress toward financial goals        |
| Spending Categories     | Distribution across expense categories |

## Tech Stack
- Python
- Pandas & NumPy (data processing)
- Matplotlib & Seaborn (visualization)
- FastAPI (REST API)
- Pydantic (data validation)
- Excel Dataset (.xlsx)

## Project Structure
```
family-financial-health-scoring/
│
├── model.ipynb                     # Data cleaning, scoring & analysis
├── score_api.py                    # FastAPI scoring service
├── family_financial_and_transactions_data.xlsx
├── spending_distribution.png       # Generated graph
└── README.md
```

## Data Cleaning & Preprocessing (model.ipynb)
Steps Performed
- Missing value handling (median imputation)
- Data type correction (dates, numeric fields)
- Duplicate removal
- Outlier capping (1st–99th percentile)
- Ratio-based feature engineering

Engineered Features
| Feature                    | Formula                       |
| -------------------------- | ----------------------------- |
| Savings-to-Income Ratio    | Savings / Income              |
| Expenses-to-Income Ratio   | Monthly Expenses / Income     |
| Loan-to-Income Ratio       | Loan Payments / Income        |
| Credit Card Spending Ratio | Credit Card Spending / Income |

## Financial Health Scoring Logic (Notebook)
Each family member’s record is scored using weighted components:
| Component                  | Weight |
| -------------------------- | ------ |
| Savings                    | 30%    |
| Expenses                   | 20%    |
| Loan Payments              | 20%    |
| Credit Card Spending       | 10%    |
| Spending Category Behavior | 10%    |
| Financial Goals Met        | 10%    |

Final score is computed as a weighted sum of all components.

## Exploratory Data Analysis
Visualizations included in model.ipynb:
- Spending distribution across categories
- Family-wise average financial health scores
- Member-wise spending trends
- Correlation heatmap of financial metrics

## Financial Scoring API (FastAPI)
File: score_api.py

### API Features
- Accepts financial data as JSON
- Calculates individual and total financial scores
- Generates insights & improvement recommendations
- Creates a spending distribution graph

## Insights & Recommendations Logic
The API automatically detects:
- Low savings
- High expenses
- Excessive loan burden
- High credit card usage
- High discretionary spending
And provides:
- Impact on score
- Exact amount to improve
- Potential score improvement

## How to Run
1- Install Dependencies
```
pip install fastapi uvicorn pandas numpy matplotlib seaborn openpyxl
```
2- Run the API
```
uvicorn score_api:app --reload
```
3- Access API Docs
```
http://127.0.0.1:8000/docs
```

### Limitations
- Rule-based scoring (not ML-based)
- Static weight assignment
- Single-period financial snapshot
- Category penalties are predefined
- No authentication or database integration

### Future Improvements
- ML-based financial risk prediction
- Time-series trend analysis
- Personalized weight tuning
- Frontend dashboard integration
- Secure user authentication
- Database-backed storage

