n_days = int(input())
v_alcohol, v_rest = map(int, input().split())
e_alcohol, e_rest = map(int, input().split())

v_alcohol_after = max(0, v_alcohol - (n_days * e_alcohol))
v_rest_after = max(0, v_rest - (n_days * e_rest))
percentage_alcohol = (v_alcohol_after / (v_alcohol_after + v_rest_after)) * 100
print(min(100, percentage_alcohol))