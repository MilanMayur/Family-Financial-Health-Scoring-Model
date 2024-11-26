from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import Response, JSONResponse, PlainTextResponse, FileResponse
import matplotlib.pyplot as plt
import numpy as np
import os, io
import base64

app = FastAPI()

# Input data model
class FamilyData(BaseModel):
    income: float
    savings: float
    monthly_expenses: float
    loan_payments: float
    credit_card_spending: float
    financial_goals_met: float  # Percentage
    category_distribution: dict  # Spending distribution (e.g., {"Travel": 5000, "Entertainment": 3000, "Shopping": 4000})

# Scoring logic
def calculate_financial_health(data: FamilyData):
    weights = {
        'savings': 0.3,
        'expenses': 0.2,
        'loan': 0.2,
        'credit_card': 0.1,
        'categories': 0.1,
        'goals': 0.1
    }

    # Calculate ratios
    savings_ratio = data.savings / data.income
    expenses_ratio = data.monthly_expenses / data.income
    loan_ratio = data.loan_payments / data.income
    credit_card_ratio = data.credit_card_spending / data.income

    # Individual scores
    penalized_categories = ['Travel', 'Entertainment', 'Shopping']
    savings_score = min(savings_ratio * 100, 30)
    expenses_score = max(20 - (expenses_ratio * 20), 0)
    loan_score = max(20 - (loan_ratio * 20), 0)
    credit_card_score = max(10 - (credit_card_ratio * 10), 0)
    category_penalty = sum(data.category_distribution.get(key, 0) for key in penalized_categories)
    category_score = max(10 - category_penalty / data.income * 100, 0)
    goals_score = data.financial_goals_met * 0.1

    # Print debug information
    '''print(f"Savings Score: {savings_score}")
    print(f"Expenses Score: {expenses_score}")
    print(f"Loan Score: {loan_score}")
    print(f"Credit Card Score: {credit_card_score}")
    print(f"Category Score: {category_score}")
    print(f"Goals Score: {goals_score}")'''

    # Composite score
    total_score = (
        savings_score + expenses_score + loan_score + 
        credit_card_score + category_score + goals_score
    )

    # Insights & recommendations
    insights = []
    recommendations = []
    if savings_ratio < 0.2:
        insights.append(f"Savings are below recommended levels, affecting your score by {30 - savings_score:.1f} points.")
        improvement = (0.2 - savings_ratio) * data.income
        potential_score_increase = (improvement / data.income) * 30
        recommendations.append(f"Increase savings by at least {improvement:.2f} to improve your score by {potential_score_increase:.1f} points.")
    
    if expenses_ratio > 0.5:
        insights.append(f"High monthly expenses reduce your score by {20 - expenses_score:.1f} points.")
        reduction = (expenses_ratio - 0.5) * data.income
        potential_score_increase = (reduction / data.income) * 20
        recommendations.append(f"Reduce monthly expenses by at least {reduction:.2f} to improve your score by {potential_score_increase:.1f} points.")
    
    if loan_ratio > 0.3:
        insights.append(f"Loan payments are high, reducing your score by {20 - loan_score:.1f} points.")
        reduction = (loan_ratio - 0.3) * data.income
        potential_score_increase = (reduction / data.income) * 20
        recommendations.append(f"Reduce loan payments by {reduction:.2f} to improve your score by {potential_score_increase:.1f} points.")

    if credit_card_ratio > 0.2:
        insights.append(f"High credit card spending lowers your score by {10 - credit_card_score:.1f} points.")
        reduction = (credit_card_ratio - 0.2) * data.income
        potential_score_increase = (reduction / data.income) * 10
        recommendations.append(f"Reduce credit card spending by {reduction:.2f} to improve your score by {potential_score_increase:.1f} points.")

    if not insights:
        insights.append("Everything looks alright.")

    return {
        "savings Score": round(savings_score, 2),
        "expenses Score": round(expenses_score, 2),
        "loan Score": round(loan_score, 2),
        "credit Card Score": round(credit_card_score, 2),
        "category Score": round(category_score, 2),
        "goals Score": round(goals_score, 2),
        "total Score": round(total_score, 2),
        "insights": insights,
        "recommendations": recommendations
        }

# Generate graph
def generate_spending_distribution_graph(category_distribution):
    categories = list(category_distribution.keys())
    spending = list(category_distribution.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, spending, color='skyblue')
    plt.xlabel('Spending Categories')
    plt.ylabel('Amount Spent')
    plt.title('Spending Distribution')
    plt.xticks(rotation=45, ha='right')

    # Annotate values on bars
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f'{int(bar.get_height())}',
            ha='center',
            va='bottom',
        )

    # Save graph to a file
    output_file = "spending_distribution.png"
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    return output_file

# API endpoint
@app.post("/calculate-financial-score-and-graph/")
def calculate_score(data: FamilyData):
    score = calculate_financial_health(data)
    graph = generate_spending_distribution_graph(data.category_distribution)

    response = {
        "Financial Data": score,
        "Graph": f"data:image/png;base64,{graph}"
    }
    return JSONResponse(content=response)

@app.get("/get-graph/")
def get_graph():
    graph_file = "spending_distribution.png"
    if os.path.exists(graph_file):
        return FileResponse(graph_file, media_type="image/png", filename="spending_distribution.png")
    return {"error": "Graph file not found. Please generate it first using /financial-score-and-graph/."}
