import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime

# CSV 파일 로드
users = pd.read_csv("/mnt/data/dummy_users.csv")
wishlist = pd.read_csv("/mnt/data/dummy_wishlist.csv")

# 1. 사용자 벡터 생성
def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

users["age"] = users["birth_date"].apply(calculate_age)

# 필요한 필드만 추출 + work_type은 원-핫 인코딩
X_numeric = users[["age", "salary", "assets"]]
X_categorical = users[["work_type"]]

# 원-핫 인코딩
encoder = OneHotEncoder(sparse=False)
X_categorical_encoded = encoder.fit_transform(X_categorical)

# 수치형 스케일링
scaler = StandardScaler()
X_numeric_scaled = scaler.fit_transform(X_numeric)

# 전체 사용자 벡터 조합
user_vectors = np.hstack((X_numeric_scaled, X_categorical_encoded))

# 2. 예시 사용자 선택 (예: user_id = 10)
target_user_id = 10
target_index = users[users["user_id"] == target_user_id].index[0]
target_vector = user_vectors[target_index].reshape(1, -1)

# 3. 코사인 유사도 계산
similarities = cosine_similarity(target_vector, user_vectors).flatten()
users["similarity"] = similarities

# 4. 유사한 사용자 상위 10명 (자기 자신 제외)
top_k_users = users[users["user_id"] != target_user_id].sort_values(by="similarity", ascending=False).head(10)
top_k_ids = top_k_users["user_id"].tolist()

# 5. 유사한 사용자들의 찜한 상품 수집
recommended_products = (
    wishlist[wishlist["user_id"].isin(top_k_ids)]
    .groupby("financial_product_id")
    .size()
    .sort_values(ascending=False)
    .reset_index(name="count")
)

# 사용자가 이미 찜한 상품 제외
user_own_products = wishlist[wishlist["user_id"] == target_user_id]["financial_product_id"].tolist()
recommended_products = recommended_products[~recommended_products["financial_product_id"].isin(user_own_products)]

# 상위 10개 추천 결과
import ace_tools as tools; tools.display_dataframe_to_user(name="추천 상품 목록", dataframe=recommended_products.head(10))


# Goal 데이터 로드
goals = pd.read_csv("/mnt/data/dummy_goals.csv")

# 목표 기간 계산
goals["start_date"] = pd.to_datetime(goals["start_date"])
goals["end_date"] = pd.to_datetime(goals["end_date"])
goals["duration_months"] = (goals["end_date"] - goals["start_date"]).dt.days // 30

# product_type 원-핫 인코딩
product_type_dummies = pd.get_dummies(goals["product_type"], prefix="ptype")

# 사용자별로 목표 데이터 평균 집계
goal_features = pd.concat([goals[["user_id", "total_target_amount", "duration_months"]], product_type_dummies], axis=1)
goal_agg = goal_features.groupby("user_id").mean().reset_index()

# 유저 테이블과 병합
merged_users = pd.merge(users, goal_agg, on="user_id", how="left").fillna(0)

# 벡터 구성: 프로필 + 목표
X_numeric = merged_users[["age", "salary", "assets", "total_target_amount", "duration_months"]]
X_categorical = merged_users[["work_type", "ptype_A", "ptype_D", "ptype_S"]]

# 원-핫 인코딩 for work_type
X_categorical_encoded = encoder.fit_transform(X_categorical)

# 수치형 스케일링
X_numeric_scaled = scaler.fit_transform(X_numeric)

# 최종 사용자 벡터
final_user_vectors = np.hstack((X_numeric_scaled, X_categorical_encoded))

# 다시 target user = 10으로 유사도 계산
target_index = merged_users[merged_users["user_id"] == target_user_id].index[0]
target_vector = final_user_vectors[target_index].reshape(1, -1)

# 코사인 유사도
similarities = cosine_similarity(target_vector, final_user_vectors).flatten()
merged_users["similarity"] = similarities

# 상위 10명 유사 사용자
top_k_users = merged_users[merged_users["user_id"] != target_user_id].sort_values(by="similarity", ascending=False).head(10)
top_k_ids = top_k_users["user_id"].tolist()

# 추천 상품 추출
recommended_products = (
    wishlist[wishlist["user_id"].isin(top_k_ids)]
    .groupby("financial_product_id")
    .size()
    .sort_values(ascending=False)
    .reset_index(name="count")
)

# 기존 찜한 상품 제외
recommended_products = recommended_products[~recommended_products["financial_product_id"].isin(user_own_products)]

# 결과 출력
tools.display_dataframe_to_user(name="목표 기반 추천 상품 목록", dataframe=recommended_products.head(10))
