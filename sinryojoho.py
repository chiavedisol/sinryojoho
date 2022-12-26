import streamlit as st
import pandas as pd
import numpy as np

tegami = ""
atesaki_tegami = ""
sinri = ""
sinri_henka = ""
mri = ""
sindan = ""

st.title("診療情報提供書を作成します")

conclusion = st.multiselect(
    '診断名を入力してください',
    ['アルツハイマー型認知症', '血管性認知症', 'レビー小体型認知症', '正常圧水頭症', '進行性核上性麻痺'],
    ['アルツハイマー型認知症'])


kaisuu = st.text_input("何回目の検査ですか", placeholder="半角数字で入力してください", key="kaisuu")

col1, col2 = st.columns(2)
with col1:
    kensa = st.date_input("今回の検査日程を入力してください", key="kensa")
    kensa_d = kensa.strftime('%Y年%m月%d日')
with col2:
    kensa_before = st.date_input("前回の検査日程を入力してください", key="kensa_before")
    kensa_before_d = kensa_before.strftime('%Y年%m月%d日')

# with col1:
atesaki = st.radio("どこに送付する書類ですか",
("紹介状の返書", "かかりつけ医", "新しい通院先", "その他"), 
horizontal=True)
col1, col2, col3 = st.columns(3)
with col3:
    if atesaki == "かかりつけ医":
        kankei = st.radio("当院との関係性", ("関係性あり", "関係性なし", "施設/訪問医あて"), 
        horizontal=True)

###########################################################################################
########　　　　　　　冒頭のあいさつ文　　　　　　　###########################################
###########################################################################################

if kaisuu == "1":
    if atesaki == "紹介状の返書":
        atesaki_tegami = f"先生にはいつも大変お世話になっており、どうもありがとうございます。{kensa_d}に実施しました認知症の精査の結果を報告いたします。"
    if atesaki == "かかりつけ医":
        if kankei == "関係性なし":
            atesaki_tegami = f"このたびは大変お世話になっており、どうもありがとうございます。認知症の精査目的で当院を受診された方です({kensa_d}初診)。先生がかかりつけと伺いました。唐突にご連絡させていただく失礼をお許しください。当院での検査結果を報告させていただきます。"
        if kankei == "関係性あり":
            atesaki_tegami = f"先生にはいつも大変お世話になっており、どうもありがとうございます。認知症の精査目的で当院を受診された方です({kensa_d}初診)。先生がかかりつけと伺いました。唐突にご連絡させていただく失礼をお許しください。当院での検査結果を報告させていただきます。"
        if kankei == "施設/訪問医あて":
            atesaki_tegami = f"このたびは大変お世話になっており、どうもありがとうございます。認知症の精査目的で当院を受診された方です({kensa_d}初診)。先生がこの方への訪問をされているかかりつけ医と伺いました。当院での検査結果を報告させていただきます。"
    if atesaki == "新しい通院先":
        atesaki_tegami = f"このたびは大変お世話になっており、どうもありがとうございます。認知症の精査目的(新たな脳梗塞・出血の有無確認のためのMRI、抗認知症薬の効果測定のためのADAS神経心理検査等)で当院を受診された方です({kensa_d}初診)。唐突にご連絡させていただく失礼をお許しください。当院での検査結果を報告させていただきます。"

if kaisuu != "1":
    if atesaki == "かかりつけ医":
        if kankei == "関係性なし":
            atesaki_tegami = f"このたびは大変お世話になっており、どうもありがとうございます。認知症の精査目的(新たな脳梗塞・出血の有無確認のためのMRI、抗認知症薬の効果測定のためのADAS神経心理検査等)で当院を受診されている方です。唐突にご連絡させていただく失礼をお許しください。{kensa_d}に{kaisuu}回目の認知症精査を実施しましたので、検査結果を報告させていただきます。"
        if kankei == "関係性あり":
            atesaki_tegami = f"先生にはいつも大変お世話になっており、どうもありがとうございます。{kensa_d}に{kaisuu}回目の認知症精査を実施しましたので、検査結果を報告させていただきます。"
    if atesaki == "新しい通院先":
        atesaki_tegami = f"このたびは大変お世話になっており、どうもありがとうございます。認知症の精査目的(新たな脳梗塞・出血の有無確認のためのMRI、抗認知症薬の効果測定のためのADAS神経心理検査等)で当院を受診されている方です。今後は先生がかかりつけになると伺いました。唐突にご連絡させていただく失礼をお許しください。{kensa_d}に{kaisuu}回目の認知症精査を実施しておりますので、検査結果を報告させていただきます。"

shohou = st.radio("処方依頼について",
("初回", "継続", "減量", "増量", "追加"), 
horizontal=True)

okure = st.checkbox("報告が遅れた場合にはチェックしてください")

if okure == True:
    if atesaki == "紹介状の返書":
        atesaki_tegami += "この度は大変ご丁寧な診療情報提供書をいただいていたにも関わらず、返信が間延びをしてしまい、大変申し訳ありませんでした。心よりお詫び申し上げます。"
    if atesaki == "かかりつけ医":
        atesaki_tegami += "結果の報告が遅くなりましたこと大変申し訳ございません。"

# kekka = st.radio("結果について",
# ("初診", "精査", "MRA"), 
# horizontal=True)

kekka = st.checkbox("MRA結果のみを報告する場合はチェックしてください")
irai = st.checkbox("結果説明を他院に依頼する場合はチェックしてください")


st.text("")
st.text("")

col1, col2 = st.columns(2)
with col1:
    alicept = st.text_input("アリセプトの内服量を入力してください", placeholder="「mg」は不要です", key="alicept")
with col2:
    donepezil = st.text_input("ドネペジルの内服量を入力してください", placeholder="「mg」は不要です", key="donepezil")

col1, col2 = st.columns(2)
with col1:
    memary = st.text_input("メマリーの内服量を入力してください", placeholder="「mg」は不要です", key="memary")
with col2:
    memantine = st.text_input("メマンチンの内服量を入力してください", placeholder="「mg」は不要です", key="memantine")

st.text("")
st.text("")

col1, col2, col3 = st.columns(3)
with col1:
    hdsr = st.text_input("HDS-Rの点数", placeholder="「点」は不要です", key="hdsr")
with col2:
    hdsr_difference = st.text_input("前回からの変化量", placeholder="「点」は不要です", key="hdsr_difference")
with col3:
    hdsr_direction = st.selectbox("変動の方向性", ("","上昇", "低下"), key="hdsr_direction")

col1, col2, col3 = st.columns(3)
with col1:
    mmse = st.text_input("MMSEの点数", placeholder="「点」は不要です", key="mmse")
with col2:
    mmse_difference = st.text_input("前回からの変化量", placeholder="「点」は不要です", key="mmse_difference")
with col3:
    mmse_direction = st.selectbox("変動の方向性", ("","上昇", "低下"), key="mmse_direction")

col1, col2, col3 = st.columns(3)
with col1:
    adas = st.text_input("ADASの点数", placeholder="「点」は不要です", key="adas")
with col2:
    adas_difference = st.text_input("前回からの変化量", placeholder="「点」は不要です", key="adas_difference")
with col3:
    adas_direction = st.selectbox("変動の方向性", ("","改善", "悪化"), key="adas_direction")

cesd = st.text_input("CES-Dの点数", placeholder="「点」は不要です", key="cesd")
sdidlb = st.text_input("SDI-DLBの点数", placeholder="「点」は不要です", key="sdidlb")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    gengo = st.text_input("言語性記憶", placeholder="WMS-R", key="gengo")
with col2:
    sikaku = st.text_input("視覚性記憶", placeholder="WMS-R", key="sikaku")
with col3:
    ippan = st.text_input("一般的記憶", placeholder="WMS-R", key="ippan")
with col4:
    tyuui = st.text_input("注意力", placeholder="WMS-R", key="tyuui")
with col5:
    tien = st.text_input("遅延再生", placeholder="WMS-R", key="tien")

sinri = f"神経心理検査上、HDS-R{hdsr}/30、MMSE{mmse}/30で、認知機能は見当識、記憶、とりわけ遅延再生領域において明瞭な低下を認めました。"
sinri = f"神経心理検査上、HDS-R{hdsr}/30、MMSE{mmse}/30で、認知機能は見当識、記憶、遅延再生、語想起の領域においてそれぞれ少しずつ低下を認めました。"
sinri = f"CES-D(うつの尺度、cutoff:15/16)は{cesd}/60で気分障害を認めました。"
sinri = f"また、SDI-DLB(レビー小体型認知症のスケール、16点以上でDLB疑い)は{sdidlb}/80でDLBが疑われました。"

sinri = f"簡易神経心理検査（HDS-R、MMSE）が高得点なためWMS-R記憶検査を実施いたしました。WMS-R指標（平均100, SD15）上、言語性記憶 {gengo}、視覚性記憶 {sikaku}、一般的記憶 {ippan}、注意/集中力 {tyuui}、遅延再生 {tien}で、【△、△の指標は平均-1SDを下回りました。なかでも△、△の指標は平均-2SDを下回りました。／平均-1SDを下回った指標はありませんでした。】【△と△の指標間乖離がみられました。】【なお、指標算出を70-74歳基準によっており、ご本人の年齢と比較すると値が低く出ている可能性があります。】【そのため認知症と診断しました。／軽度認知障害と診断しました。／積極的に認知症と診断できませんでした。】"

sinri = f"簡易神経心理検査（HDS-R、MMSE）が高得点なためWMS-R記憶検査およびTMT（Trail Making Test：注意機能をみる）を実施いたしました。WMS-R指標（平均100, SD15）上、言語性記憶 {gengo}、視覚性記憶 {sikaku}、一般的記憶 {ippan}、注意/集中力 {tyuui}、遅延再生 {tien}で、【△、△の指標は平均-1SDを下回りました。なかでも△、△の指標は平均-2SDを下回りました。／平均-1SDを下回った指標はありませんでした。】【△と△の指標間乖離がみられました。】【なお、指標算出を70-74歳基準によっており、ご本人の年齢と比較すると値が低く出ている可能性があります。】TMTにおいて、【PartAの遂行がスムーズであったのに対し、より難しいPartBでは自己修正されないエラーが生じ遂行の遅延がみられました。／遂行はスムーズであり問題は認められませんでした。】【そのため認知症と診断しました。／軽度認知障害と診断しました。／積極的に認知症と診断できませんでした。】"

sinri_henka = f"神経心理検査上、HDS-R{hdsr}/30、MMSE{mmse}/30で認知機能は見当識、記憶、とりわけ遅延再生領域において明瞭な低下を認めました。{kensa_before_d}実施と比べそれぞれ、{hdsr_difference}点の{hdsr_direction}、{mmse_difference}点の{mmse_direction}でした。ADAS(抗認知症薬の効果測定)は{adas}/70で{adas_difference}点の{adas_direction}でした。"
sinri_henka = f"神経心理検査上、HDS-R{hdsr}/30、MMSE{mmse}/30で、{kensa_before_d}実施と比べそれぞれ、HDS-Rは{hdsr_difference}点の{hdsr_direction}、MMSEについては変化がありませんでした。ADAS(抗認知症薬の効果測定)は{adas}/70で{adas_difference}点の{adas_direction}でした。"

mri = st.text_area("MRI所見を入力してください", key=mri)
mri = mri.replace("\n" , "").replace("１"," 1").replace("２"," 2").replace("３"," 3").replace("４"," 4")\
    .replace("５"," 5").replace("６"," 6").replace("７"," 7").replace("８"," 8").replace("９"," 9").replace("１０"," 10").replace("．",".")


sindan = f"従いまして、画像上海馬の萎縮は明瞭ではありませんが、神経心理検査上、近時記憶の明瞭な低下を認め、現時点では特異的な症候を見出せず、アルツハイマー型認知症と診断させていただきました。"
sindan = f"中脳被蓋の萎縮や第三脳室拡大、第四脳室拡大もある印象です。進行性核上性麻痺、基底核変性症なども疑えますが、特異的な症候を見いだせておりませんので、現時点ではアルツハイマー型認知症としております。"

sindan_lewy = f"従いまして、画像上アルツハイマー型認知症及び高齢者タウオパチーとして矛盾ありませんでした。また、歩行状態の不安定さ、明らかな幻視、レム睡眠行動障害と思われる報告があり、神経心理検査上からもレビー小体型認知症が疑われ、現時点では、アルツハイマー型認知症とレビー小体型認知症の合併と診断させていただきました。"
sindan_lewy = f"画像上アルツハイマー型認知症及び高齢者タウオパチーとして矛盾ありませんでしたが、現時点では、特異的な症候を見出せず、記憶障害よりアルツハイマー型認知症、神経心理検査の結果、注意力低下と気分障害を中心としたレビー小体型認知症と考えることができます。これらの合併型と診断させていただきました。"

sindan_vad = f"従いまして、画像上アルツハイマー型認知症及び高齢者タウオパチーとして矛盾ありませんでしたが、現時点では特異的な症候を見出せず、アルツハイマー型認知症と、また◯◯に多発する◯◯を考慮し、血管性認知症との混合型と診断させていただきました。"
sindan_vad = f"従いまして、画像上アルツハイマー型認知症及び高齢者タウオパチーとして矛盾ありませんでしたが、現時点では、特異的な症候を見出せず、右被殻、左視床の出血後変化、広範囲にわたる脳梗塞とあわせて、アルツハイマー型認知症と血管性認知症と診断させていただきました。"

sindan_nph = f"頭頂部脳溝が狭く、それに比べて脳室全体が拡大しており、正常圧水頭症の可能性も否定できませんが現時点でタップテストのメルクマールとなるような認知機能低下以外の特異的症状（magnetic gaitやincontinence）や失禁の出現が乏しく判断に窮します。そのため正常圧水頭症疑いとさせていただきました。"

tegami = atesaki_tegami + "\n" + "\n" + sinri + sinri_henka + "\n" + "\n" + mri

st.text("")
st.text("")


if st.button("文章を生成します"):
    # latest_iteration = st.empty()
    # bar = st.progress(0)
    # for i in range(100):
    #     latest_iteration.text(f'文章生成中です {i+1}')
    #     bar.progress(i+1)
    #     time.sleep(0.01)
    # st.write("下記の文章を確認のうえ使用してください")
    st.write(tegami)


button_css = f"""
<style>
  div.stButton > button:first-child  {{
    font-weight  : bold                ;/* 文字：太字                   */
    border       :  5px solid #f36     ;/* 枠線：ピンク色で5ピクセルの実線 */
    border-radius: 10px 10px 10px 10px ;/* 枠線：半径10ピクセルの角丸     */
    background   : #ddd                ;/* 背景色：薄いグレー            */
  }}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)

