import streamlit as st
import pandas as pd
import numpy as np

pagelist = ["診療情報提供書","精査依頼", "運転免許"]
selector = st.sidebar.radio("ページ選択",pagelist)
if selector=="診療情報提供書":

    tegami = ""
    atesaki_tegami = ""
    sinri = ""
    sinri_cesd = ""
    sinri_sdidlb = ""
    sinri_wmsr = ""
    sinri_tmt = ""
    sinri_henka = ""
    mri_artifact = ""
    mri = ""
    mri_hankaku = ""
    henka_nasi = ""
    mri_follow = ""
    sindan = ""
    sindan_vad = ""
    sindan_lewy = ""
    sindan_nph = ""
    sindan_mci = ""
    sindan_sci = ""
    sindan_psp = ""
    kaishaku = ""
    setumei_naiyou = ""
    shohou_touin = ""
    shohou_irai = ""
    vitamin = ""
    antiplt = ""
    keizoku_soudan = ""
    senmou_soudan = ""
    risperdal_soudan = ""
    gezai_soudan = ""
    ketuatu_tyuui = ""
    dengon = ""
    musubi = ""

    st.title("診療情報提供書を作成します")

    conclusion = st.multiselect(
        '診断名を入力してください',
        ['アルツハイマー型認知症', '血管性認知症', 'レビー小体型認知症', '正常圧水頭症', 'MCI/SCI', '前頭側頭葉変性症','進行性核上性麻痺'],
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
    ("紹介状の返書（初回）", "かかりつけ医", "新しい通院先", "その他"), 
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
        if atesaki == "紹介状の返書（初回）":
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

    shohou_kaisi = st.checkbox("当院で処方を開始した場合にはチェックしてください")
    shokai_kaisi = st.checkbox("他院に初回処方そのものを依頼する場合にはチェックしてください")
    zensoku = st.checkbox("気管支喘息はありますか")

    shohou = st.radio("処方依頼について",
    ("将来", "初回", "継続", "増量", "減量", "追加", "処方依頼なし"), 
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

    # kekka = st.checkbox("MRA結果のみを報告する場合はチェックしてください")

    st.write("")
    st.write("")



    ###########################################################################################
    ########　　　　　　　心理検査の結果　　　　　　　　###########################################
    ###########################################################################################

    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     hdsr = st.text_input("HDS-Rの点数", placeholder="「点」は不要です", key="hdsr")
    # with col2:
    #     hdsr_difference = st.text_input("前回からの変化量", placeholder="「点」は不要です", key="hdsr_difference")
    # with col3:
    #     hdsr_direction = st.selectbox("変動の方向性", ("","上昇", "低下"), key="hdsr_direction")

    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     mmse = st.text_input("MMSEの点数", placeholder="「点」は不要です", key="mmse")
    # with col2:
    #     mmse_difference = st.text_input("前回からの変化量", placeholder="「点」は不要です", key="mmse_difference")
    # with col3:
    #     mmse_direction = st.selectbox("変動の方向性", ("","上昇", "低下"), key="mmse_direction")

    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     adas = st.text_input("ADASの点数", placeholder="「点」は不要です", key="adas")
    # with col2:
    #     adas_difference = st.text_input("前回からの変化量", placeholder="「点」は不要です", key="adas_difference")
    # with col3:
    #     adas_direction = st.selectbox("変動の方向性", ("","改善", "悪化"), key="adas_direction")

    markdown = """
    ### 心理検査の結果について
    """
    st.write(markdown)

    col1, col2, col3 = st.columns(3)
    with col1:
        hdsr = st.text_input("HDS-Rの点数", placeholder="「点」は不要です", key="hdsr")
    with col2:
        hdsr_before = st.text_input("前回HDS-Rの点数", placeholder="「点」は不要です", key="hdsr_difference")
        if hdsr == "":
            hdsr_difference = ""
        elif hdsr_before == "":
            hdsr_difference = ""
        else:
            hdsr_difference = int(hdsr) - int(hdsr_before)
    with col3:
        if hdsr_difference == "":
            hdsr_direction = f""
        elif hdsr_difference < 0:
            hdsr_difference *= -1
            hdsr_direction = f"{hdsr_difference}点の低下"
        elif hdsr_difference == 0:
            hdsr_direction = f"不変です"
        elif hdsr_difference > 0:
            hdsr_direction = f"{hdsr_difference}点の上昇"
        st.write("HDS-Rの変化量")
        st.write(hdsr_direction)

    col1, col2, col3 = st.columns(3)
    with col1:
        mmse = st.text_input("MMSEの点数", placeholder="「点」は不要です", key="mmse")
    with col2:
        mmse_before = st.text_input("前回MMSEの点数", placeholder="「点」は不要です", key="mmse_difference")
        if mmse == "":
            mmse_difference = ""
        elif mmse_before == "":
            mmse_difference = ""
        else:
            mmse_difference = int(mmse) - int(mmse_before)
    with col3:
        if mmse_difference == "":
            mmse_direction = f""
        elif mmse_difference < 0:
            mmse_difference *= -1
            mmse_direction = f"{mmse_difference}点の低下"
        elif mmse_difference == 0:
            mmse_direction = f"不変です"
        elif mmse_difference > 0:
            mmse_direction = f"{mmse_difference}点の上昇"
        st.write("MMSEの変化量")
        st.write(mmse_direction)

    col1, col2, col3 = st.columns(3)
    with col1:
        adas = st.text_input("ADASの点数", placeholder="「点」は不要です", key="adas")
    with col2:
        adas_before = st.text_input("前回adasの点数", placeholder="「点」は不要です", key="adas_difference")
        if adas == "":
            adas_difference = ""
        elif adas_before == "":
            adas_difference = ""
        else:
            adas_difference = float(adas) - float(adas_before)
            adas_difference = round(adas_difference, 1)
    with col3:
        if adas_difference == "":
            adas_direction = f""
        elif adas_difference < 0:
            adas_difference *= -1
            adas_direction = f"{adas_difference}点の改善"
        elif adas_difference == 0:
            adas_direction = f"不変です"
        elif adas_difference > 0:
            adas_direction = f"{adas_difference}点の悪化"
        st.write("ADASの変化量")
        st.write(adas_direction)
    hantei = st.checkbox("上記の検査結果はADAS曲線(natural course)を上回りますか")
    
    st.write("")
    st.write("")

    cesd = st.text_input("CES-Dの点数", placeholder="「点」は不要です", key="cesd")
    sdidlb = st.text_input("SDI-DLBの点数", placeholder="「点」は不要です", key="sdidlb")

    st.write("")
    st.write("")   

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

    wmsr_comment = st.text_area("WMS-RおよびTMTの評価を入力してください", key="wmsr_comment")
    wmsr_comment = wmsr_comment.replace("\n" , "")
    tmt = st.checkbox("TMT実施済みの場合にはチェックしてください")

    if kaisuu == "1":
        sinri = f"神経心理検査では、HDS-R{hdsr}/30、MMSE{mmse}/30で、見当識、記憶、語想起、とりわけ遅延再生領域において認知機能の低下を認めました。"
        if cesd != "":
            if int(cesd) >= 16:
                sinri_cesd = f"CES-D(うつの尺度、cutoff:15/16)は{cesd}/60で気分障害を認めました。"
        if sdidlb != "":
            if int(sdidlb) >= 16:
                sinri_sdidlb = f"また、SDI-DLB(レビー小体型認知症のスケール、cutoff:15/16)は{sdidlb}/80でDLBが疑われました。"

    if wmsr_comment != "":
        if tmt == False:
            sinri = ""
            sinri_wmsr = f"簡易神経心理検査（HDS-R{hdsr}/30、MMSE{mmse}/30）が高得点なためWMS-R記憶検査を実施いたしました。WMS-R指標（平均100, SD15）上、言語性記憶 {gengo}、視覚性記憶 {sikaku}、一般的記憶 {ippan}、注意/集中力 {tyuui}、遅延再生 {tien}で、{wmsr_comment}。"
        if tmt == True:
            sinri = ""
            sinri_wmsr = ""
            sinri_tmt = f"簡易神経心理検査（HDS-R{hdsr}/30、MMSE{mmse}/30）が高得点なためWMS-R記憶検査およびTMT（Trail Making Test：注意機能をみる）を実施いたしました。WMS-R指標（平均100, SD15）上、言語性記憶 {gengo}、視覚性記憶 {sikaku}、一般的記憶 {ippan}、注意/集中力 {tyuui}、遅延再生 {tien}で、●●●●●●●●●●●●●●●●{wmsr_comment}●●●●●●●●●●●●●●●●"

    if kaisuu != "1":
        sinri_henka = f"神経心理検査上、HDS-R{hdsr}/30、MMSE{mmse}/30で、前回実施（{kensa_before_d}）と比べ"
        if hdsr_difference != 0:
            if mmse_difference != 0:
                sinri_henka += f"それぞれ{hdsr_direction}と、{mmse_direction}がみられました。"
            else:
                sinri_henka += f"HDS-Rには{hdsr_direction}がみられ、MMSEについては変化がありませんでした。"
        elif hdsr_difference == 0:
            if mmse_difference != 0:
                sinri_henka += f"HDS-Rについては変化がなく、MMSEには{mmse_direction}がみられました。"
            else:
                sinri_henka += f"HDS-R・MMSEともに変化がありませんでした。"

    st.write("")
    st.write("")

    ###########################################################################################
    ########　　　　　　　MRI検査の結果　 　　　　　　　###########################################
    ###########################################################################################

    markdown = """
    ### MRI所見について
    """
    st.write(markdown)  

    mri = st.text_area("MRI所見を入力してください", key="mri")
    mri_hankaku = mri.replace("\n" , "").replace("１"," 1").replace("２"," 2").replace("３"," 3").replace("４"," 4")\
        .replace("５"," 5").replace("６"," 6").replace("７"," 7").replace("８"," 8").replace("９"," 9").replace("１０"," 10").replace("．",".")
    
    keiji_henka = st.checkbox("MRI画像所見に経時的な変化が「あれば」チェックしてください")
    if keiji_henka == False:
        henka_nasi = f"これら画像所見に経時的変化は明らかではありませんでした。"

    artifact = st.checkbox("MRI画像にアーチファクトの混入はありましたか")
    mri_artifact = f"頭部単純MRIでは、"
    if artifact == True:
        mri_hankaku = mri.replace("\n" , "").replace("１"," 1").replace("２"," 1").replace("３"," 2").replace("４"," 3")\
        .replace("５"," 4").replace("６"," 5").replace("７"," 6").replace("８"," 7").replace("９"," 8").replace("１０"," 9").replace("．",".") 
        mri_artifact = f"頭部単純MRIでは（アーチファクトの混入があり以下参考所見となりますが大変申し訳ありません）、"
        col1, col2 = st.columns(2)
        with col2:
            ugoku_artifact = st.checkbox("頭が動いたことによるアーチファクトの混入ですか")
        if ugoku_artifact == True:
            mri_artifact = f"頭部単純MRIでは（当院の力不足から撮像中に頭位を保つことが難しくアーチファクトが混入してしまい以下参考所見となりますが大変申し訳ありません）、"

    follow_d = ""
    col1, col2, col3 = st.columns(3)
    with col1:
        mri_shukketu = st.checkbox(f"出血フォロー有り")
    with col2:
        mri_kousoku = st.checkbox(f"梗塞フォロー有り")
    with col3:
        mri_koumakuka = st.checkbox(f"硬膜下血腫フォロー有り")
    if mri_shukketu or mri_kousoku or mri_koumakuka is True:
        with col3:
            follow = st.date_input("フォロー検査日程", key="follow")
            follow_d = follow.strftime('%Y年%m月%d日')

    if follow_d != "":
        if mri_shukketu == True:
            mri_follow = f"上記の通り新規に微小脳出血を指摘したため、"
            if mri_kousoku == True:
                mri_follow = f"上記の通り新規に微小脳出血と梗塞を指摘したため、"
                if mri_koumakuka == True:
                    mri_follow = f"上記の通り新規に微小脳出血と梗塞を指摘し、また硬膜下血腫が認められるため、"
        elif mri_kousoku == True:
            mri_follow = f"上記の通り新規に梗塞を指摘したため、"
            if mri_koumakuka == True:
                mri_follow = f"上記の通り新規に梗塞を指摘し、また硬膜下血腫が認められるため、"
        elif mri_koumakuka == True:
            mri_follow = f"上記の通り硬膜下血腫が認められるため、"           

        mri_follow += f"{follow_d}に再度頭部頭部単純MRIを実施いたしましたが、変化や増悪は認められず経過観察としております。" 

    ###########################################################################################
    ########　　　　　　　MRA検査の結果　 　　　　　　　###########################################
    ###########################################################################################

    st.write("")
    st.write("")

    markdown = """
    ### MRA所見について
    """
    st.write(markdown)  

    mra = st.text_area("MRA所見を入力してください", key="mra")
    mra_hankaku = mra.replace("\n" , "").replace("１"," 1").replace("２"," 2").replace("３"," 3").replace("４"," 4")\
        .replace("５"," 5").replace("６"," 6").replace("７"," 7").replace("８"," 8").replace("９"," 9").replace("１０"," 10").replace("．",".")
    
    keiji_henka_mra = st.checkbox("MRA画像所見に経時的な変化が「あれば」チェックしてください")
    if keiji_henka_mra == False:
        henka_nasi_mra = f"これら画像所見に経時的変化は明らかではありませんでした。"

    is_artifact = st.checkbox("MRA画像にアーチファクトの混入はありましたか")
    mra_artifact = f"頭部MRAでは、"
    if is_artifact == True:
        mra_hankaku = mri.replace("\n" , "").replace("１"," 1").replace("２"," 1").replace("３"," 2").replace("４"," 3")\
        .replace("５"," 4").replace("６"," 5").replace("７"," 6").replace("８"," 7").replace("９"," 8").replace("１０"," 9").replace("．",".") 
        mra_artifact = f"頭部MRAでは（アーチファクトの混入があり以下参考所見となりますが大変申し訳ありません）、"
        col1, col2 = st.columns(2)
        with col2:
            ugoku_artifact_mra = st.checkbox("頭が動いたことによるアーチファクトの混入ですか")
        if ugoku_artifact_mra == True:
            mra_artifact = f"頭部MRAでは（当院の力不足から撮像中に頭位を保つことが難しくアーチファクトが混入してしまい以下参考所見となりますが大変申し訳ありません）、"

    ###########################################################################################
    ########　　　　　　　診断名の説明文　　　　　　　　###########################################
    ###########################################################################################

    # '血管性認知症', 'レビー小体型認知症', '正常圧水頭症', 'MCI/SCI','進行性核上性麻痺'],

    if kaisuu == "1":

        if 'アルツハイマー型認知症' in conclusion:
            markdown = """
            ### アルツハイマー型認知症について
            """
            st.write(markdown)

            left, right = st.columns(2)
            with left:
                ishuku = st.checkbox("側頭葉内側の萎縮はありますか")
            with right:
                higai_ishuku = st.checkbox("中脳被蓋の萎縮や第三脳室拡大・第四脳室拡大はありますか")
            if ishuku == True:
                sindan = f"従いまして、神経心理検査では近時記憶の機能低下が指摘され、画像上もアルツハイマー型認知症及び高齢者タウオパチーとして矛盾ありませんでした。現時点ではその他の疾患に特異的な症候を見出せておりませんので、アルツハイマー型認知症と診断させていただきました。"
            if ishuku == False:
                if higai_ishuku == True:
                    sindan = f"従いまして、神経心理検査では近時記憶の機能低下が指摘され、画像上は中脳被蓋の萎縮や第三脳室拡大、第四脳室拡大もある印象です。進行性核上性麻痺、基底核変性症なども疑えますが、現時点では特異的な症候を見出せておりませんので、アルツハイマー型認知症と診断させていただきました。"
                else:
                    sindan = f"従いまして、画像上は海馬を含む側頭葉の萎縮は明瞭ではありませんが、神経心理検査では近時記憶の機能低下が指摘され、現時点ではその他の疾患に特異的な症候を見出せておりませんので、アルツハイマー型認知症と診断させていただきました。"

        if '血管性認知症' in conclusion:
            markdown = """
            ### 血管性認知症について
            """
            st.write(markdown)
            kyoketu = st.checkbox("基底核に慢性虚血性変化が目立ちますか")
            # col1, col2, col3, col4 = st.columns(4)
            # with col1:
            #     vad_situgo = st.checkbox(f"失語あり")
            #     st.markdown('<p class="small-font">　　　言語の障害</p>', unsafe_allow_html=True)
            # with col2:
            #     vad_sikkou = st.checkbox(f"失行あり")
            #     st.markdown('<p class="small-font">　　　運動機能は障害されていないのに、運動行為が障害される</p>', unsafe_allow_html=True)
            # with col3:
            #     vad_situnin = st.checkbox(f"失認あり")
            #     st.markdown('<p class="small-font">　　　感覚機能は障害されていないのに、対象を認識または同定できない</p>', unsafe_allow_html=True)
            # with col4:
            #     vad_jikkou = st.checkbox(f"実行機能の障害あり")
            #     st.markdown('<p class="small-font">　　　計画を立てる、組織化する、順序だてる、抽象化する</p>', unsafe_allow_html=True)

            if kyoketu == True:
                if 'アルツハイマー型認知症' in conclusion:
                    sindan_vad = f"また基底核に慢性虚血性変化が目立ち血管性認知症の合併もあると愚考しております。"
                else:
                    sindan_vad = f"従いまして、認知機能の変化と、基底核の慢性虚血性変化を考慮し、血管性認知症と診断させていただきました。"
            else:
                vad_mri = st.text_area("血管性認知症の診断に至ったMRI所見を入力してください", placeholder="「両側性視床梗塞」など体言止めで入力してください", key="vad_mri")
                if 'アルツハイマー型認知症' in conclusion:
                    sindan_vad = f"また上記の通り{vad_mri}が指摘され血管性認知症の合併もあると愚考しております。"
                else:
                    sindan_vad = f"従いまして、認知機能の変化と、{vad_mri}を考慮し、血管性認知症と診断させていただきました。"

        if 'レビー小体型認知症' in conclusion:
            markdown = """
            ### レビー小体型認知症について
            """
            st.write(markdown)
            dlb_shoujou = ""
            col1, col2, col3, col4= st.columns(4)
            with col1:
                dlb_hokou = st.checkbox(f"認知の変動")
                if dlb_hokou == True:
                    dlb_shoujou += "注意力低下を伴う認知の変動・"
            with col2:
                dlb_gensi = st.checkbox(f"明らかな幻視")
                if dlb_gensi == True:
                    dlb_shoujou += "明らかな幻視・"
            with col3:
                dlb_rem = st.checkbox(f"レム睡眠行動異常")
                if dlb_rem == True:
                    dlb_shoujou += "レム睡眠行動異常・"
            with col4:
                dlb_parkinson = st.checkbox(f"パーキンソン症状")
                if dlb_parkinson == True:
                    dlb_shoujou += "パーキンソン症状・"
            dlb_jiritu = st.checkbox(f"自律神経症状（便秘・寝汗・起立性低血圧など）")
            if dlb_jiritu == True:
                dlb_shoujou += "自律神経症状"
            dlb_shoujou = dlb_shoujou.strip("・")
            if 'アルツハイマー型認知症' in conclusion:
                if '血管性認知症' in conclusion:
                    sindan_vad = f"また基底核に慢性虚血性変化が目立ち血管性認知症と、"
                    sindan_lewy = f"さらに{dlb_shoujou}が認められ、レビー小体型認知症の合併もあると愚考しております。"
                else:
                    sindan_lewy = f"また{dlb_shoujou}が認められ、レビー小体型認知症の合併もあると愚考しております。"
            else:
                if '血管性認知症' in conclusion:
                    sindan_lewy = f"また{dlb_shoujou}が認められ、レビー小体型認知症の合併もあると愚考しております。"
                else:
                    sindan_lewy = f"上記の神経心理検査、画像所見、および{dlb_shoujou}が認められることを考慮して、レビー小体型認知症と診断させていただきました。"

        if '正常圧水頭症' in conclusion:
            markdown = """
            ### 正常圧水頭症について
            """
            st.write(markdown)
            nph_merkmal = st.checkbox(f"歩行障害や失禁がありタップテストが推奨されますか")
            if nph_merkmal == True:
                sindan_nph = f"上記に示した画像所見の通り、正常圧水頭症の可能性を否定できず、また現時点でタップテストのメルクマールとなるような認知機能低下以外の特異的症状（歩行障害や失禁など）がうかがわれます。そのため正常圧水頭症疑いについてタップテストのご説明をさせていただきました。"
            else: 
                sindan_nph = f"上記に示した画像所見の通り、正常圧水頭症の可能性を否定できませんが、現時点でタップテストのメルクマールとなるような認知機能低下以外の特異的症状（歩行障害や失禁など）の出現に乏しく判断に窮します。そのため正常圧水頭症の疑いについては経過観察とさせていただきました。"

        if 'MCI/SCI' in conclusion:
            markdown = """
            ### MCI/SCIについて
            """
            st.write(markdown)
            mci_sci = st.checkbox(f"神経心理検査から軽度認知障害が示唆されますか")
            if mci_sci == True:
                sindan_mci = f"従いまして、今回の検査では、積極的に認知症であることを支持する所見は得られませんでしたが、WMS-R結果および自覚的な認知機能低下を考慮して軽度認知障害（MCI）の診断としております。"
            else:
                sindan_sci = f"従いまして、今回の検査では、神経心理検査および画像所見においても積極的に認知症であることを支持する所見は得られませんでした。そのため自覚的な認知機能低下のみということで、現時点ではSCI（主観的認知機能低下、subjective coginitive impairment）ということに留まると愚考いたしました。"
                
        if '進行性核上性麻痺' in conclusion:
            # markdown = """
            # ### 進行性核上性麻痺について
            # """
            # st.write(markdown) 
            sindan_psp = f"従いまして、歩行時の易転倒性、眼球運動障害、構音障害や嚥下障害、注意力の低下や反応の遅さ等の臨床所見を踏まえまして、現時点では進行性核上性麻痺と診断させていただきました。"

    ###########################################################################################
    ########　　　　　　　内服について　　　　　　　　　###########################################
    ###########################################################################################

    st.write("")
    st.write("")


    markdown = """
    ### 内服について
    """
    st.write(markdown)
    shohou_henkou = st.checkbox("処方内容に変更がある場合にはチェックしてください")
    shohou_updown = ""
    if shohou_henkou == True:
        col1, col2= st.columns(2)
        with col2:
            shohou_updown = st.radio("どのような変更ですか",
            ("増量", "減量", "抗精神病薬の追加"), horizontal=True)
            st.write("下記には変更後の内服量を記載してください")

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

    naifuku_genkou = ""
    if alicept != "":
        naifuku_genkou += f"アリセプト{alicept}mgおよび"
    if donepezil != "":
        naifuku_genkou += f"ドネペジル{donepezil}mgおよび"
    if memary != "":
        naifuku_genkou += f"メマリー{memary}mg"
    if memantine != "":
        naifuku_genkou += f"メマンチン{memantine}mg"
    naifuku_genkou = naifuku_genkou.rstrip("および")

    is_alicept = ""
    if alicept != "":
        naifuku_genkou += f"アリセプト{alicept}mgおよび"
    if donepezil != "":
        naifuku_genkou += f"ドネペジル{donepezil}mgおよび"
    is_alicept = is_alicept.rstrip("および")

    is_memary = ""
    if memary != "":
        naifuku_genkou += f"メマリー{memary}mgおよび"
    if memantine != "":
        naifuku_genkou += f"メマンチン{memantine}mgおよび"
    is_alicept = is_alicept.rstrip("および")

    st.write("")
    st.write("")

    ###########################################################################################
    ########　　　　　　　検査結果の解釈　　　　　　　　###########################################
    ###########################################################################################
    markdown = """
    ### 検査結果の解釈について
    """
    st.write(markdown)

    if kaisuu != "1":
        # （抗認知症薬当院で同量継続）
        if hantei == True:
            if shohou == "処方依頼なし":
                kaishaku = f"神経心理検査では前回と比較して、ADAS曲線のnatural course（抗認知症薬を服用していない群）を上回っており、{naifuku_genkou}の効果がみられていると愚考し、次回認知症精査まで同量を継続していく予定でおります。"
            # （抗認知症薬同量処方依頼）
            if shohou == "初回":
                kaishaku = f"神経心理検査では前回と比較して、ADAS曲線のnatural course（抗認知症薬を服用していない群）を上回っており、{naifuku_genkou}の効果はみられていると愚考いたします。ご本人ご家族の希望があり、今後は貴院にて抗認知症薬のご処方をご検討いただけますと幸甚です。大変お忙しいところに、また誠に厚かましいお願いとなり恐縮ではございますが、どうかご高配のほど何卒よろしくお願い申し上げます。"
            # （他院にてすでに処方開始されていた場合）
            if shohou == "継続":
                kaishaku = f"神経心理検査では前回と比較して、ADAS曲線のnatural course（抗認知症薬を服用していない群）を上回っており、{naifuku_genkou}の効果はみられていると愚考いたします。差し出がましく誠に恐縮ですが、先生にすでにご処方いただいております抗認知症薬の継続処方をご検討いただけますと幸甚です。大変お忙しいところに、また誠に厚かましいお願いとなり恐縮ではございますが、どうかご高配のほど何卒よろしくお願い申し上げます。"
            # （抗認知症薬当院で増量）
        if hantei == False:
            if shohou_henkou == False:
                if shohou == "処方依頼なし":
                    kaishaku = f"神経心理検査では前回と比較して、ADAS曲線のnatural course(抗認知症薬を服用していない群）と有意差が認められませんが、ご本人ご家族と話し合い、今しばらくは{naifuku_genkou}の継続を希望されました。次回認知症精査まで同量を継続していく予定でおります。"
                if shohou == "継続":
                    kaishaku = f"神経心理検査では前回と比較して、ADAS曲線のnatural course(抗認知症薬を服用していない群）と有意差が認められませんが、ご本人ご家族と話し合い、今しばらくは{naifuku_genkou}の継続を希望されました。差し出がましく誠に恐縮ですが、抗認知症薬の継続処方をご検討賜れますと幸甚です。大変お忙しいところに、また誠に厚かましいお願いとなり恐縮ではございますが、どうかご高配のほど何卒よろしくお願い申し上げます。"
            if shohou_henkou == True:
                if keiji_henka == False:
                    if shohou == "処方依頼なし":
                        kaishaku = f"従いまして、画像上は経時的な認めませんでしたが、神経心理検査では前回と比較して悪化がみられます。ご本人ご家族の診察においても生活上の変化が報告され、抗認知症薬を増量する時期に来ていると愚考し、{naifuku_genkou}まで増量いたしました。"
            # （認知症薬増量処方依頼）
                    if shohou == "増量":
                        kaishaku = f"従いまして、画像上は経時的な認めませんでしたが、神経心理検査では前回と比較して悪化がみられます。ご本人ご家族の診察においても生活上の変化が報告され、抗認知症薬を増量する時期に来ていると愚考され、誠に厚かましいお願いとなり恐縮ではございますが、{naifuku_genkou}に増量することをご検討いただけますか。どうかご高配のほど何卒よろしくお願い申し上げます。"




    ###########################################################################################
    ########　　　　　　　処方内容の説明　　　　　　　　###########################################
    ###########################################################################################

    st.write("")
    st.write("")

    markdown = """
    ### 結果説明について
    """
    st.write(markdown)

    setumei = st.date_input("結果説明の日程を入力してください", key="setumei")
    setumei_d = setumei.strftime('%Y年%m月%d日')
    setumei_irai = st.checkbox("当院で検査結果を説明しておらず他院に説明依頼をする場合はチェックしてください")
    if setumei_irai == True:
        setumei_naiyou = f"当院へは遠方のため来院の負担があり、ご本人ご家族の希望もあり、上記の検査結果については先生からお伝えいただけますと誠にありがたく存じます。大変お手を煩わせて申し訳ありません。なにかご不明な点がございましたら、ご連絡いただければ誠にありがたく存じます。"
    
    if naifuku_genkou == "":
        kaishaku = f"{setumei_d}に、上記検査結果をご説明し、また半年後に改めて認知機能の推移をチェックさせていただくこととしました。誠に恐縮ですが、引き続きご高診を賜りますようお願い申し上げます。"

    if shohou_kaisi == True:
        if is_alicept != "":
            shohou_touin = f"{setumei_d}に、ご本人とご家族へ上記検査結果と抗認知症薬の効果（認知機能の低下の遅延、ADAS検査で効果を測定することなど）・副作用（コリン作用など）についてお伝えしました。ご本人ご家族が抗認知症薬の服薬を希望されましたので、本日{naifuku_genkou}を処方させていただきました。食欲不振・下痢など消化器症状の副作用のモニタリングを行い、問題がないようであれば5mgまでの増量を予定しております。"
            if zensoku == True:
                shohou_touin = f"{setumei_d}に、ご本人とご家族へ上記検査結果と抗認知症薬の効果（認知機能の低下の遅延、ADAS検査で効果を測定することなど）・副作用（コリン作用など）についてお伝えしました。ご本人とご家族が抗認知症薬の服薬を希望されましたので、気管支喘息の状況を考慮しつつ、アリセプト3mg1錠を処方させていただきました（アリセプトは気管支喘息において慎重投与になっております）。コリン作用に伴う食欲不振・下痢などの消化器症状の他、気管支狭窄による喘息発作などの副作用のモニタリングを行う予定です。"
            if shohou == "将来":
                shohou_irai = f"服薬が安定しましたところで、改めてご連絡させていただきます。その際には、アリセプト等の抗認知症薬の処方につきまして、先生からご処方をご検討賜れますと誠にありがたく存じます。大変お忙しいところに、また誠に厚かましいお願いとなり恐縮ではございますが、どうかご高配のほど何卒よろしくお願い申し上げます。"
            if shohou == "初回":
                shohou_irai = f"{naifuku_genkou}につきまして、食欲不振・下痢などの消化器症状の副作用もなく服薬は安定されております。今後につきましては、ご本人ご家族の希望もあり、先生から抗認知症薬のご処方をご検討賜れますと幸甚です。大変お忙しいところに、また誠に厚かましいお願いとなり恐縮ではございますが、どうかご高配のほど何卒よろしくお願い申し上げます。"
            if shokai_kaisi == True:
                shohou_touin = ""
                shohou_irai = f"{setumei_d}に、ご本人とご家族へ上記検査結果と抗認知症薬の効果（認知機能の低下の遅延、ADAS検査で効果を測定することなど）・副作用（コリン作用など）についてお伝えしました。当院ではなく先生から抗認知症薬の開始をいただくことを希望されております。大変お忙しいところに、また誠に厚かましいお願いとなり恐縮ではございますが、アリセプト等の抗認知症薬の処方（たとえばアリセプトであれば血中の半減期が70-80時間であるため、副作用のチェックに3mg錠1T1Xで2-3週間、問題なければ5mg錠に増量など）についてご高配を賜れますと誠にありがたく存じます。"
            
    ###########################################################################################
    ########　　　　　　　抗認知症薬以外の説明　　　　　###########################################
    ###########################################################################################

    sonota_naifuku = st.multiselect(
    '抗認知症薬以外の処方を入力してください',
    ['アリナミン', 'メチコバール', 'フォリアミン', 'シロスタゾール', 'バイアスピリン','プラビックス', 'その他'],
    [])

    vitamin_naifuku = ""
    if 'アリナミン' in sonota_naifuku:
        vitamin_naifuku += f"アリナミン・"
    if 'メチコバール' in sonota_naifuku:
        vitamin_naifuku += f"メチコバール・"
    if 'フォリアミン' in sonota_naifuku:
        vitamin_naifuku += f"フォリアミン"
    vitamin_naifuku = vitamin_naifuku.rstrip("・")

    antiplt_naifuku = ""
    if 'シロスタゾール' in sonota_naifuku:
        antiplt_naifuku += f"シロスタゾール・"
    if 'バイアスピリン' in sonota_naifuku:
        antiplt_naifuku += f"バイアスピリン・"
    if 'プラビックス' in sonota_naifuku:
        antiplt_naifuku += f"プラビックス"
    antiplt_naifuku = antiplt_naifuku.rstrip("・")


    if vitamin_naifuku != "":
        vitamin = f"また血液検査において認知機能に関連するビタミンの欠乏が認められましたので、{vitamin_naifuku}を処方しております。"

    if antiplt_naifuku != "":
        antiplt = f"頭部単純MRA上では主幹動脈の広狭不整があり、動脈硬化性変化が疑われました。頭部MRIのFLAIRでは慢性虚血性変化が目立ち、またT2*において出血性変化はなく、その観点から（たとえば{antiplt_naifuku}等の）抗血小板薬が再梗塞予防に益するかもしれないと愚考いたしました。"
    

    ###########################################################################################
    ########　　　　　　　他院処方の調整依頼　　　　　　###########################################
    ###########################################################################################

    markdown = """
    ### その他の依頼について
    """
    st.write(markdown)

    naifuku_keizoku = st.checkbox("抗認知症薬の継続可否をご相談する")
    if naifuku_keizoku == True:
        # （アリセプト服用継続をかかりつけ医に検討してもらう場合）
        fukusayou = ""
        if is_alicept != "":
            fukusayou += "食欲低下、下痢（アリセプト）、"
        if is_memary != "":
            fukusayou += "ふらつき、めまい(メマリー）"
        fukusayou = fukusayou.rstrip("、")
        keizoku_soudan = f"ご本人の体力が衰えもあり抗認知症薬継続の可否についてお尋ねがありました。{fukusayou}などがなければ、認知機能低下遅延の一助になるかもしれず（明確なエビデンスがないのですが）そういう意味で抗認知症薬の継続をしていくこともできようとも思い、服薬が可能であれば継続的に服薬するのも一法であるとお伝えしました。現時点での局面におけるエビデンスが確立されていないために、またADAS神経心理検査で認知機能の遅延効果について具体的に調べることも困難でもあり、誠に悩ましい問題であって、明確な答えはない、ともお伝えしました。ここは直観的な判断にならざるを得ないとも思いますが、先生とご相談くださるようお話し申し上げました。専門医の間でも意見の相違がある局面です。誠に勝手なお願いで恐縮に存じますが、抗認知症薬の継続・中止について、普段ご様子をご高診いただいている先生にご検討をお願い申し上げる次第です。突然のことで誠に恐縮ですが、どうか失礼をご寛恕いただけますならば幸甚です。"

    senmou_yakuzai = st.checkbox("せん妄を生じうる内服の中止をご相談する")
    if senmou_yakuzai == True:
        tyusi_irai = st.text_input("中止を依頼する薬剤名を入力してください", key="tyusi_irai")
        senmou_soudan = f"せん妄が続く場合は対策のひとつに薬剤調整があろうかと愚考いたします。例えば{tyusi_irai}の内服中止によって改善する可能性があるのかもしれません。誠に差し出がましい提案となり恐縮ですが、どうかご寛恕くださいますと幸甚です。"
    
    if shohou_updown == "抗精神病薬の追加":
        risperdal_soudan = f"またご本人の焦燥があり、時には疲弊してしまうことがあると、ご家族から伺いました。焦燥について環境調整ではコントロールできないような状況であると思われたため、リスパダールを処方させていただきました（ただし認知機能の低下、錐体外路症状（手足の出づらさ、飲み込みの悪さ、表情の硬さ、流涎など）の出現を恐れて、落ち着き次第に漸減・中止の予定です。"

    shoukaki_yakuzai = st.checkbox("消化器症状に影響する内服（下剤など）の調整をご相談する")
    if shoukaki_yakuzai == True:
        itukara = st.text_input("服薬何日目で消化器症状が出現しましたか", placeholder="「単位」は不要です", key="itukara")
        tyusi_onegai = st.text_input("中止を依頼する薬剤名を入力してください", key="tyusi_onegai")
        gezai_soudan = f"{setumei_d}に検査結果をご説明のうえアリセプトの投薬を開始いたしました。副作用(食欲不振や下痢などの消化器症状、徐脈など)の有無の確認を行っておりましたところ、服薬{itukara}日後から消化器症状が生じたとご報告がありました。誠に僭越で大変恐縮ですが、先生からご処方の{tyusi_onegai}につきまして、内服を中止していただくようお伝えしました。症状が落ち着きましたら改めて先生にご報告申し上げたく存じます。今後もどうかよろしくご高診のほど何卒よろしくお願い申し上げます。"

    ketuatu_takai = st.checkbox("降圧をご相談する")
    if ketuatu_takai == True:
        ketuatu = st.text_input("来院時の血圧を入力してください", 
        placeholder="例えば「162/86」など単位は不要です", key="ketuatu")
        if mri_shukketu == True:
            ketuatu_tyuui = f"微小脳出血が新たに認められましたので、血圧のコントロールは重要であり（なお服薬のアドヒアランスの問題か、あるいはたまたまかもしれませんが、当院受診時の血圧は{ketuatu}mmHgでした）先生のご診療でよくご相談されるようご本人ご家族へ上記検査結果とあわせて伝えました。"
        else:
            ketuatu_tyuui = f"血圧のコントロールは重要であり（なお服薬のアドヒアランスの問題か、あるいはたまたまかもしれませんが、当院受診時の血圧は{ketuatu}mmHgでした）先生のご診療でよくご相談されるようご本人ご家族へ上記検査結果とあわせて伝えました。"

    

    ###########################################################################################
    ########　　　　　　　その他の事情があれば　　　　　###########################################
    ###########################################################################################

    markdown = """
    ### その他の事情はありますか
    """
    st.write(markdown)

    dengon = st.text_area("医師への伝言があればここに記載をお願いします", key="dengon")
    if dengon == "":
        dengon = dengon
    else:
        dengon = "★★★★★★★★★★★★★★★★" + dengon + "★★★★★★★★★★★★★★★★" 

    ###########################################################################################
    ########　　　　　　　結びのことば　　　　　　　　　###########################################
    ###########################################################################################

    # #（紹介状あり、当院へは精査のみ）
    # musubi = f"当院ではアリセプト（メマリー）の効果（ADAS神経心理検査による非投薬群との経時的な変化を比較することで判定します）、脳の形態変化を含む病変のチェックなど半年ごとに行っております。先生のご判断の下ご指示いただければそのようにいたします。誠に恐縮ですがご高診賜りますようお願い申し上げます。何かご不明な点がございましたら、ご連絡いただければ誠に有難く存じます。この度はご紹介賜り誠にありがとうございます。今後ともご指導賜りますようお願い申し上げます。"
    
    # #（紹介状なし、当院へは精査のみ）
    # musubi = f"当院ではアリセプト（メマリー）の効果（ADAS神経心理検査による非投薬群との経時的な変化を比較することで判定します）、脳の形態変化を含む病変のチェックなど半年ごとに行っております。先生のご判断の下ご指示いただければそのようにいたします。誠に恐縮ですがご高診賜りますようお願い申し上げます。何かご不明な点がございましたら、ご連絡いただければ誠に有難く存じます。今後ともご指導賜りますようお願い申し上げます。"

    #（今後も定期的に当院受診の場合）
    if is_alicept != "":
        if is_memary != "":
            musubi = f"当院ではアリセプトおよびメマリーの効果（ADAS神経心理検査による非投薬群との経時的な変化を比較することで判定します）、脳の形態変化を含む病変のチェックなど半年ごとに行っております。実施しました際には、改めてご報告させていただきます。何かご不明な点がございましたら、ご連絡いただければ誠に有難く存じます。今後ともご指導をいただけますと幸いです。"
        else:
            musubi = f"当院ではアリセプトの効果（ADAS神経心理検査による非投薬群との経時的な変化を比較することで判定します）、脳の形態変化を含む病変のチェックなど半年ごとに行っております。実施しました際には、改めてご報告させていただきます。何かご不明な点がございましたら、ご連絡いただければ誠に有難く存じます。今後ともご指導をいただけますと幸いです。"
    else:
        if is_memary != "":
            musubi = f"当院ではメマリーの効果（ADAS神経心理検査による非投薬群との経時的な変化を比較することで判定します）、脳の形態変化を含む病変のチェックなど半年ごとに行っております。実施しました際には、改めてご報告させていただきます。何かご不明な点がございましたら、ご連絡いただければ誠に有難く存じます。今後ともご指導をいただけますと幸いです。"
        else:
            musubi = f"当院では認知症の精査（新たな脳梗塞・出血の有無確認のためのMRI、認知機能の推移をみるADAS神経心理検査等）を実施しております。また何らかの脳のイベントが疑われる時には、MRIをご指示いただければ実施致します。実施しました際には、改めてご報告させていただきます。何かご不明な点がございましたら、ご連絡いただければ誠に有難く存じます。今後ともご指導をいただけますと幸いです。"


    ###########################################################################################
    ########　　　　　　　最終出力　　　　　　　　　　　###########################################
    ###########################################################################################

    tegami = atesaki_tegami + "\n" + "\n"

    if sinri + sinri_cesd + sinri_sdidlb + sinri_wmsr + sinri_tmt + sinri_henka + mri_artifact + mri_hankaku + henka_nasi + mri_follow != "":
        tegami += sinri + sinri_cesd + sinri_sdidlb + sinri_wmsr + sinri_tmt + sinri_henka + "\n"
        
    if mri_hankaku != "":
        tegami += mri_artifact + mri_hankaku + henka_nasi + mri_follow + "\n" 

    if mra_hankaku != "":
        tegami += mra_artifact + mra_hankaku + henka_nasi_mra + "\n"

    if sindan + sindan_vad + sindan_lewy + sindan_nph  + sindan_mci + sindan_sci + sindan_psp != "":
        tegami += sindan + sindan_vad + sindan_lewy + sindan_nph  + sindan_mci + sindan_sci + sindan_psp + "\n"
    
    if kaishaku + setumei_naiyou + shohou_touin + shohou_irai + vitamin + antiplt + keizoku_soudan + senmou_soudan + risperdal_soudan + gezai_soudan + ketuatu_tyuui + dengon != "":
        tegami += kaishaku + setumei_naiyou + shohou_touin + shohou_irai + vitamin + antiplt + keizoku_soudan + senmou_soudan + risperdal_soudan + gezai_soudan + ketuatu_tyuui + dengon

    if musubi != "":
        tegami += "\n" + "\n" + musubi



    st.write("")
    st.write("")


    if st.button("文章を生成します"):
        # latest_iteration = st.empty()
        # bar = st.progress(0)
        # for i in range(100):
        #     latest_iteration.text(f'文章生成中です {i+1}')
        #     bar.progress(i+1)
        #     time.sleep(0.01)
        # st.write("下記の文章を確認のうえ使用してください")
        st.text_area("診療情報提供書", value=tegami, placeholder="診療情報提供書", height=800, label_visibility="hidden", key="tegami")


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
    st.markdown(f"""
    <style>
    .small-font{{
        font-size:10px;
    }}
    </style>
    """, unsafe_allow_html=True)
    st.markdown(button_css, unsafe_allow_html=True)

###########################################################################################
########　　　　　　　他院に精査を依頼　　　　　　　###########################################
###########################################################################################

if selector=="精査依頼":

    st.title("他院に精査を依頼します")
    atesaki = st.radio("精査を依頼する疾患名を入力してください",
    ('レビー小体型認知症', '正常圧水頭症', '脳腫瘍', '脳動脈瘤', '精神科入院依頼', '進行性核上性麻痺'), 
    horizontal=True)

    nph_irai = f"いつも大変お世話になっており、どうもありがとうございます。認知症の精査目的で当院を受診している方です（平成〇年〇月〇日初診）。初診時頭部単純MRI撮影を実施したところ、両側側脳室、第三脳室拡大が目立ち、一方で頭頂部含めて脳溝は狭い印象があり、正常圧水頭症を疑わせる所見がありました。尿失禁、歩行困難も認められました。もともと歩くのが好きな方で、少しでも歩ける可能性があるのであれば、その可能性についてご検討いただきたいと本人、ご家族のご希望がありました。お忙しいところ誠に恐縮ですが、貴科的精査ご高診賜りますようお願いいたします。今後ともどうぞご指導賜りますようお願い申し上げます。"
    shuyou_irai = f"いつも大変お世話になっており、どうもありがとうございます。認知症の精査目的で当院受診されている方です（平成〇年〇月〇日初診）。頭部単純MRI撮影を実施したところ、左側脳室前角の部位に一致して、約〇mm大の腫瘤状構造物疑う所見がありました。お忙しいところ誠に恐縮ですが、貴科的精査ご高診賜りますようお願いいたします。今後ともどうぞご指導賜りますようお願い申し上げます。"
    doumyakuryu_irai = f"いつも大変お世話になっており、どうもありがとうございます。認知症の精査目的で当院を受診されている方です(平成〇年〇月〇日初診)。平成〇年〇月〇日MRA撮像を実施いたしましたところ、〇〇に約〇mm大の瘤状構造があり動脈瘤を疑われました。お忙しいところ急なお願いで誠に恐縮ですが、貴科的精査ご高診賜わりますようお願い申し上げます。今後ともどうぞご指導賜りますようお願い申し上げます。"
    nyuin_irai = f"せん妄があり、リスパダール（一時はアリセプトもあわせて）を調整しつつ自宅療養を続けてまいりました。このところ活動性のせん妄（一日中ベッドの周りをうろうろする（akathisiaかもしれません）、妻や子に殴りかかる、大声で叫ぶなどが頻発し、同居の妻は目が離せない状態で、かなり疲弊し在宅生活が限界にあります。外来通院についても本年に入りご本人と奥さんはこられず、息子さんのみが来られる状況です。このたびは突然のお願いで、大変お忙しい中誠に恐縮に存じます。何卒入院の上ご高診ご加療のご検討を賜れれば幸甚です。今後ともどうかご指導賜りますようお願い申し上げます。"
    nyuin_irai = f"受診される数日前より、急激に記憶障害が出現し、認知症の精査を希望され受診にいたりました。気分障害に対して前医よりデパス、ドグマチール、アーテンが処方されていました。奏功がしていないようで服用を中止しました。本日受診された際、食欲不振、不眠が出現したとの報告がありました。ご家族が、現状の介護について「これ以上もう無理」と強くその限界について訴えておられ、入院加療を強く希望されています。お忙しいところ誠に恐縮ですが、何卒入院の上、貴科的精査ご高診賜りますようお願いいたします。今後ともどうぞご指導賜りますようお願い申し上げます。"

    sankou = f"当院での検査結果をご参考まで添付いたします。神経心理検査上、HDS-R〇/30、MMSE〇/30で、認知機能は見当識、記憶、とりわけ遅延再生領域において明瞭な低下を認めました。頭部単純MRI上、１．〇〇〇。２．〇〇〇。当院では力不足からタップテストは未実施です。"


###########################################################################################
########　　　　　　　運転免許　　　　　　　　　　　###########################################
###########################################################################################

if selector=="運転免許":

    st.title("運転免許の更新が難しい場合")

    menkyo = f"平成〇年〇月〇日、ご本人と奥様に上記の内容と運転免許の更新は難しいことをお伝えしました。運転免許証の自主返納をお勧めしましたが、思いもよらない結果だったご様子で、私の力不足もあり、ご本人は茫然とされ奥様は怒りを露わにされておりました。先生にご迷惑が及ぶことを恐れます。大変申し訳ありませんでした。運転免許証の自主返納（少しだけ特典があるようです）を何度かお勧めしましたが、今後の事をご本人がその場で判断することはできず、診断書を作成してお渡ししました。お渡しした診断書を添付いたします。この度はご紹介賜り誠にありがとうございます。なにかご不明点あればご連絡賜れれば幸甚です。今後ともご指導賜りますようお願い申し上げます。"
    menkyo = f"平成〇年〇月〇日、ご本人に上記の内容と運転免許の更新は不能であることをお伝えしました。診断書を発行するよりも、メリットがあるかもしれない運転免許証の自主返納をお勧めしました。また抗認知症薬の効果・副作用について説明しましたところ抗認知症薬の服薬を希望されましたので、アリセプト3mg1錠１X１朝14日分を処方させていただきました。食欲不振・下痢などの消化器症状などの副作用のモニタリングを行い、問題がないようであれば、5mgへ増量する予定です。服薬が副作用なく安定しましたところで、先生から合わせてご処方いただければ誠にありがたく存じます。"