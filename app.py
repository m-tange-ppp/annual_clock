import streamlit as st
from datetime import *
import pytz
from decimal import *
import time
from factrization import *

# 年月日時刻を取得する
tz_japan = pytz.timezone("Asia/Tokyo")
dt_now = datetime.now(tz_japan)
this_year = dt_now.year
year_start = tz_japan.localize(datetime(
    this_year, 1, 1))
year_end = tz_japan.localize(datetime(
    this_year, 12, 31, 23, 59, 59, 599999))

# できるだけ誤差少なめに計算する
seconds_year = (year_end - year_start).total_seconds()
seconds_now = (dt_now - year_start).total_seconds()
rate_now_year = (Decimal(f"{seconds_now}") / Decimal(f"{seconds_year}") * 100).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
div_now_year = (Decimal(f"{seconds_year}") - Decimal(f"{seconds_now}")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

# 日時を素因数分解する
def today_factorization(now):
    int_now = now.month * 10 ** 8 + now.day * 10 ** 6 + now.hour * 10 ** 4 + now.minute * 10 ** 2 + now.second
    result = prime_factorization(int_now)
    view = ""
    for p, num in result.items():
        if num != 1:
            view += f"{p}^{num} × "
        else:
            view += f"{p} × "
    return view[:-2]

# いろいろ表示する
st.title("年間時計")
st.write(f"{this_year}年の{rate_now_year}％が終了しました。")
st.progress(float(rate_now_year / 100))
st.write(f"{this_year}年が終了するまであと{div_now_year}秒です。")
if this_year == 2023:
    st.write("# 良いお年を！！")
else:
    st.markdown("# あけましておめでとうございます！！")
if st.button("今を素因数分解する"):
    str_now = dt_now.strftime("%m月%d日%H時%M分%S秒")
    st.write(f"{str_now} を素因数分解すると {today_factorization(dt_now)} になります。")
time.sleep(1)
st.experimental_rerun()