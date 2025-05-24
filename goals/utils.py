# 현재 예상 달성 시점 계산
def simulate_savings(target_amount, current_amount, total_month, interest_rate, save_type):

    # 단리
    if save_type == 'S':
        interest_rate /= 100 * 12
        deposit = (target_amount - current_amount) / (2 + interest_rate * total_month + 1) / total_month
        return deposit
    
    # 복리
    if save_type == 'M':
        pass

# 추가 납입 시 당겨지는 개월 수
# def 