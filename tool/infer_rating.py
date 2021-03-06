import numpy as np
from scipy.stats import beta
import sys
args = sys.argv
max_delta_rating = 2**13 # レーティング差の最大値を表す定数

def infer_rating(win, lose, draw=0, draw_half=True): # レーティングの区間推定を行う
    def elorating(winrate): # 勝率からレーティング差を計算する
        if winrate == 1:
            return max_delta_rating
        if winrate == 0:
            return -max_delta_rating
        return 400.0 * np.log10(winrate / (1 - winrate))

    def clopper_pearson(k, n, alpha): # clopper_pearson法による二項分布近似
        alpha2 = (1 - alpha) / 2
        lower = beta.ppf(alpha2, k, n - k + 1)
        upper = beta.ppf(1 - alpha2, k + 1, n - k)
        return (lower, upper, alpha)
 
    def print_result(result, sigma): # 結果の出力
        lowerrate = 0 if result[0] != result[0] else 100 * result[0]
        lower = -max_delta_rating if result[0] != result[0] else elorating(result[0])
        upperrate = 100 if result[1] != result[1] else 100 * result[1]
        upper = max_delta_rating if result[1] != result[1] else elorating(result[1])
        print(f"{sigma}σ: R({100 * result[2]:.4f}%) {lower:+8.2f} ({lowerrate:5.2f}%) ～ {upper:+8.2f} ({upperrate:5.2f}%), Range: {upper - lower:6.2f}")

    if draw_half: # 引き分けを0.5勝として計算する場合
        draw2 = draw // 2 # 小数点以下は切り捨てる
        win2 = win + draw2
        lose2 = lose + draw2
        match = win + lose + draw2 * 2
    else:
        win2 = win
        lose2 = lose
        match = win + lose

    print(f"有効試合数: {match}, 勝ち: {win2}, 負け: {lose2}")
    winrate = np.nan if match == 0 else 100 * win2 / match
    deltarate = np.nan if match == 0 else elorating(win2 / match)
    drawrate = np.nan if match == 0 else 100 * draw / match
    print(f"勝率: {winrate:.2f}%, ⊿R: {deltarate:+.2f}, 引分率: {drawrate:.2f}%")
    print_result(clopper_pearson(win2, match, 0.38292492254802624), 0.5)
    print_result(clopper_pearson(win2, match, 0.68268949213708585), 1.0)
    print_result(clopper_pearson(win2, match, 0.86638559746228383), 1.5)
    print_result(clopper_pearson(win2, match, 0.95449973610364158), 2.0)
    print_result(clopper_pearson(win2, match, 0.98758066934844768), 2.5)
    print_result(clopper_pearson(win2, match, 0.99730020393673979), 3.0)
    print_result(clopper_pearson(win2, match, 0.99953474184192892), 3.5)
    print_result(clopper_pearson(win2, match, 0.99993665751633376), 4.0)
    print_result(clopper_pearson(win2, match, 0.99999320465375052), 4.5)
    print_result(clopper_pearson(win2, match, 0.99999942669685615), 5.0)

draw = int(args[3] if len(args) >= 4 else 0)
draw_half = False if (len(args) >= 5 and args[4] == "False") else True
infer_rating(int(args[1]), int(args[2]), draw, draw_half)
