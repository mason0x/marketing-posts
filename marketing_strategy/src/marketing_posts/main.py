#!/usr/bin/env python
import sys
from marketing_posts.crew import MarketingPostsCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'customer_domain': 'mydailydefense.com',
        'project_description': """
Daily Defense is a USA-based wellness brand offering a comprehensive range of dietary supplements and vitamins manufactured under GMP guidelines in FDA-registered facilities. Founded by Jenna Sabacheuskaya, the company focuses on "boosting defenses from within" through scientifically-formulated supplements targeting various health concerns including immunity, digestion, cognition, joint health, hormone balance, and aging support.
Their product lineup includes both essential supplements (like multivitamins and omega-3s) and specialized formulas (such as berberine complex and hormone support). The brand emphasizes quality control, using pure ingredients without artificial colors, preservatives, or sweeteners. Their development process involves collaboration with nutritionists, chemists, and naturopaths.
Key brand differentiators include:

Free shipping on all US orders
30-day money-back guarantee
Product bundles for cost savings
Focus on natural ingredients
Wide range of health categories (30+ different wellness areas)
Price points typically ranging from $24.95 to $39.95 per product
Strong emphasis on cleanse/detox products as a core offering

The company positions itself as a premium yet accessible wellness brand, targeting health-conscious consumers looking for comprehensive supplementation solutions.
"""
    }
    MarketingPostsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'customer_domain': 'mydailydefense.com',
        'project_description': """
Daily Defense is a USA-based wellness brand offering a comprehensive range of dietary supplements and vitamins manufactured under GMP guidelines in FDA-registered facilities. Founded by Jenna Sabacheuskaya, the company focuses on "boosting defenses from within" through scientifically-formulated supplements targeting various health concerns including immunity, digestion, cognition, joint health, hormone balance, and aging support.
Their product lineup includes both essential supplements (like multivitamins and omega-3s) and specialized formulas (such as berberine complex and hormone support). The brand emphasizes quality control, using pure ingredients without artificial colors, preservatives, or sweeteners. Their development process involves collaboration with nutritionists, chemists, and naturopaths.
Key brand differentiators include:

Free shipping on all US orders
30-day money-back guarantee
Product bundles for cost savings
Focus on natural ingredients
Wide range of health categories (30+ different wellness areas)
Price points typically ranging from $24.95 to $39.95 per product
Strong emphasis on cleanse/detox products as a core offering

The company positions itself as a premium yet accessible wellness brand, targeting health-conscious consumers looking for comprehensive supplementation solutions.
"""
    }
    try:
        MarketingPostsCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def main_function():
    # Example: Call the run function
    run()
    # Or call train() if needed
    # train()
