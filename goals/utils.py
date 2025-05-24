# 적금 >> 단리S, 복리M
def simulate_precise_savings(
    monthly_amount: int,
    annual_interest_rate: float,
    save_type: str,  # 'S' or 'M'
    target_amount: int,
    max_months: int = 120
):
    deposits = []  # 각 납입액 저장
    months = 0
    current_amount = 0
    monthly_rate = annual_interest_rate / 100 / 12

    # 목표치에 도달할 때까지 계산하기
    while current_amount < target_amount and months < max_months:
        deposits.append(monthly_amount)
        months += 1
        total = 0

        for i, amount in enumerate(deposits):
            months_remaining = months - i
            if save_type == 'S':
                interest = amount * monthly_rate * months_remaining
                total += amount + interest
            elif save_type == 'M':  # 복리
                compound = amount * ((1 + monthly_rate) ** months_remaining)
                total += compound

        current_amount = total

    return months, round(current_amount)
