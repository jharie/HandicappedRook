﻿# Komaochi Theorem

駒落ちに関する理論。

# 基礎知識

## はじめに

- 永らく香、角、飛、飛香、飛角(2枚)、飛角両香(4枚)、飛角両香桂(6枚)…という固定の手合いしかメジャーではなかった。
- もっと一般的な駒落ちに関する理論を深めることを目的とする。
- 駒落ちによるハンディキャップは振り飛車によるハンディキャップの理論に応用できる可能性がある。

## 駒落ちの表記法

- 駒落ちはA(左)B右C両Dと表記する。
- ABCDに入る文字列は飛角金銀桂香の順でソートされている。
- Aには飛、角が入る。
- Bがnullのとき左は書かない。Cがnullのとき右は書かない。Dがnullのとき両は書かない。
- 左は省略してもよい。Bには金、銀、桂、香が入り、それぞれ角側の駒を落とすことを表す。
- 右は省略できない。Cには金、銀、桂、香が入り、それぞれ飛側の駒を落とすことを表す。
- 両は省略できない。Dには金、銀、桂、香が入り、それぞれ両側の駒を落とすことを表す。
- B, C, Dの任意の2つの共通集合はnullである。BとCの共通はDに移せる。BとDの共通からBを消せる。CとDの共通からCを消せる。
- 歩落ちの表記はここでは定義しない

以上のルールにより駒落ちの表記は左を書くか書かないかを除いて一意に定まる。

# 駒落ちに関する仮説

## 駒落ち平等の法則

- 同じ駒落ちなら誰に対しても同じR低下がもたらされるというもの。

## 駒落ち対称性の破れ

(検証中)

## 駒落ち非線形仮説

(検証中)

# 駒落ちR低下関数fを導出する

- f(香)=90のような関数fを作成したい。

非線形仮説から  
f(x, y) = f(x) + f(y) + α  
とかける。
