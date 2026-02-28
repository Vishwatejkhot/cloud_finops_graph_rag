def simulate_reserved_savings(total_cost, discount=0.3):
    savings = total_cost * discount
    return {
        "current_cost": total_cost,
        "estimated_new_cost": round(total_cost - savings, 2),
        "estimated_savings": round(savings, 2)
    }  


    