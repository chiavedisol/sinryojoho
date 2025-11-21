import { FormData } from "./types";

export function generateText(data: Partial<FormData>): string {
    if (!data) return "";

    const formatDate = (date?: Date) => {
        if (!date) return "";
        return date.toLocaleDateString("ja-JP", { year: "numeric", month: "long", day: "numeric" });
    };

    const today = new Date();
    const todayStr = formatDate(today);
    const kensaDate = formatDate(data.kensaDate);
    const kensaBeforeDate = formatDate(data.kensaBeforeDate);
    const setumeiDate = formatDate(data.setumeiDate);

    // ========================================
    // ヘッダー
    // ========================================
    let header = `診療情報提供書\n\n${todayStr}\n\n`;

    // 宛先
    let recipient = "";
    if (data.atesaki === "紹介状あり") {
        recipient = "紹介元医療機関 御机下\n\n";
    } else if (data.atesaki === "紹介状なし") {
        recipient = "かかりつけ医 御机下\n\n";
    } else if (data.atesaki === "新しい通院先") {
        recipient = "主治医 御机下\n\n";
    }

    header += recipient;

    // 挨拶
    let greeting = "平素より大変お世話になっております。\n";
    if (data.atesaki === "紹介状あり") {
        greeting += "この度はご紹介いただき、誠にありがとうございます。\n";
    }
    greeting += "\n";

    // ========================================
    // ブロック1: 診断名
    // ========================================
    let block1 = "【診断名】\n";
    if (data.conclusion && data.conclusion.length > 0) {
        block1 += data.conclusion.join("、") + "\n";
    } else {
        block1 += "（診断名未記入）\n";
    }
    block1 += "\n";

    // ========================================
    // ブロック2: 目的
    // ========================================
    let block2 = "【ご報告の趣旨】\n";

    if (data.kaisuu === "1") {
        block2 += `${kensaDate || "先日"}に当院にて実施いたしました認知症精査の結果をご報告申し上げます。`;
    } else {
        block2 += `${kensaDate || "先日"}に当院にて${data.kaisuu}回目の認知症精査を実施いたしました。`;
        if (data.shohou === "初回依頼" || data.shohou === "継続" || data.shohou === "増量" || data.shohou === "切り替え") {
            block2 += "治療方針につきまして、ご高診を賜りたく存じます。";
        } else {
            block2 += "検査結果をご報告申し上げます。";
        }
    }
    block2 += "\n\n";

    // ========================================
    // ブロック3: 本文
    // ========================================
    let block3 = "【検査結果および考察】\n\n";

    // --- 神経心理検査 ---
    block3 += "■ 神経心理検査所見\n";

    const hdsr = data.hdsr ? parseInt(data.hdsr) : null;
    const hdsrBefore = data.hdsrBefore ? parseInt(data.hdsrBefore) : null;
    const mmse = data.mmse ? parseInt(data.mmse) : null;
    const mmseBefore = data.mmseBefore ? parseInt(data.mmseBefore) : null;
    const adas = data.adas ? parseFloat(data.adas) : null;
    const adasBefore = data.adasBefore ? parseFloat(data.adasBefore) : null;

    // 初回または前回データなし
    if (data.kaisuu === "1" || (!hdsrBefore && !mmseBefore)) {
        block3 += `HDS-R ${data.hdsr || "-"}/30点、MMSE ${data.mmse || "-"}/30点でございました。`;
        if (hdsr !== null && hdsr < 24) {
            block3 += "見当識、記憶、注意機能において認知機能の低下が認められました。";
        }
    } else {
        // 2回目以降で比較可能
        const hdsrDiff = hdsr !== null && hdsrBefore !== null ? hdsr - hdsrBefore : null;
        const mmseDiff = mmse !== null && mmseBefore !== null ? mmse - mmseBefore : null;

        block3 += `前回（${kensaBeforeDate}）と比較いたしますと、`;

        const changes: string[] = [];
        if (hdsrDiff !== null) {
            if (hdsrDiff > 0) changes.push(`HDS-Rは${hdsrDiff}点の改善`);
            else if (hdsrDiff < 0) changes.push(`HDS-Rは${Math.abs(hdsrDiff)}点の低下`);
            else changes.push("HDS-Rは横ばい");
        }
        if (mmseDiff !== null) {
            if (mmseDiff > 0) changes.push(`MMSEは${mmseDiff}点の改善`);
            else if (mmseDiff < 0) changes.push(`MMSEは${Math.abs(mmseDiff)}点の低下`);
            else changes.push("MMSEは横ばい");
        }

        if (changes.length > 0) {
            block3 += changes.join("、") + "という結果でございました。";
        }
    }
    block3 += "\n";

    // ADAS
    if (adas !== null) {
        block3 += `ADAS神経心理検査は${adas}/70点`;
        if (adasBefore !== null) {
            const adasDiff = adas - adasBefore;
            if (adasDiff > 0) {
                block3 += `で、前回より${adasDiff.toFixed(1)}点の悪化`;
            } else if (adasDiff < 0) {
                block3 += `で、前回より${Math.abs(adasDiff).toFixed(1)}点の改善`;
            } else {
                block3 += "で、前回と変化なし";
            }
        }
        block3 += "でございました。\n";
    }

    // CES-D, SDI-DLB
    if (data.cesd && parseInt(data.cesd) >= 16) {
        block3 += `CES-D（うつ尺度）は${data.cesd}/60点で、気分の落ち込みが示唆されました。\n`;
    }
    if (data.sdidlb && parseInt(data.sdidlb) >= 16) {
        block3 += `SDI-DLB（レビー小体型スケール）は${data.sdidlb}/80点で、レビー小体型認知症が疑われました。\n`;
    }

    // WMS-R
    if (data.wmsrComment) {
        block3 += `\nWMS-R記憶検査では、`;
        if (data.gengo) block3 += `言語性記憶${data.gengo}、`;
        if (data.sikaku) block3 += `視覚性記憶${data.sikaku}、`;
        if (data.ippan) block3 += `一般的記憶${data.ippan}、`;
        if (data.tyuui) block3 += `注意/集中力${data.tyuui}、`;
        if (data.tien) block3 += `遅延再生${data.tien}、`;
        block3 = block3.replace(/、$/, "");
        block3 += `という結果でございました。${data.wmsrComment}\n`;
    }

    block3 += "\n";

    // --- 画像検査 ---
    block3 += "■ 画像検査所見\n";

    // MRI
    if (data.mriPmi) {
        block3 += "ペースメーカー植込み術後のため、MRI検査は実施しておりません。";
    } else if (data.mriFindings) {
        let mriPrefix = "頭部MRIでは、";
        if (data.mriArtifact) {
            if (data.mriUgokuArtifact) {
                mriPrefix = "頭部MRIでは（誠に申し訳ございませんが、撮像中の体動によりアーチファクトが混入しており、以下参考所見となります）、";
            } else {
                mriPrefix = "頭部MRIでは（誠に申し訳ございませんが、アーチファクトの混入があり、以下参考所見となります）、";
            }
        }
        block3 += mriPrefix + data.mriFindings.replace(/\n/g, " ");

        if (data.mriKeijiHenka) {
            block3 += "これらの所見に経時的変化は明らかではございませんでした。";
        }
        block3 += "\n";
    }

    // MRA
    if (data.mraFindings) {
        let mraPrefix = "頭部MRAでは、";
        if (data.mraArtifact) {
            if (data.mraUgokuArtifact) {
                mraPrefix = "頭部MRAでは（誠に申し訳ございませんが、撮像中の体動によりアーチファクトが混入しており、以下参考所見となります）、";
            } else {
                mraPrefix = "頭部MRAでは（誠に申し訳ございませんが、アーチファクトの混入があり、以下参考所見となります）、";
            }
        }
        block3 += mraPrefix + data.mraFindings.replace(/\n/g, " ");

        if (data.mraKeijiHenka) {
            block3 += "これらの所見に経時的変化は明らかではございませんでした。";
        }
        block3 += "\n";
    }

    block3 += "\n";

    // --- 診断に至った所見 ---
    let diagnosisDetails = "";
    if (data.ishuku) diagnosisDetails += "・海馬の萎縮が認められました\n";
    if (data.kyoketu) diagnosisDetails += "・基底核に虚血性変化が認められました\n";
    if (data.vadMri) diagnosisDetails += `・${data.vadMri}\n`;
    if (data.dlbHenDou) diagnosisDetails += "・認知機能の変動がみられました\n";
    if (data.dlbGensi) diagnosisDetails += "・幻視が認められました\n";
    if (data.dlbParkinson) diagnosisDetails += "・パーキンソン症状が認められました\n";
    if (data.nphTriad) diagnosisDetails += "・正常圧水頭症の3徴（認知機能低下、歩行障害、尿失禁）が認められました\n";
    if (data.wmsrRef) diagnosisDetails += "・WMS-R結果もご参照ください\n";
    if (data.higaiIshuku) diagnosisDetails += "・中脳被蓋の萎縮が認められました\n";

    if (diagnosisDetails) {
        block3 += "■ 診断に至った所見\n";
        block3 += diagnosisDetails + "\n";
    }

    // --- 解釈と依頼 ---
    block3 += "■ 考察とお願い\n";

    // 結果が良好か懸念かを判断
    let isGood = false;
    let isConcerning = false;

    if (data.hantei) {
        // ADAS良好と判定されている
        isGood = true;
    } else if (data.shohouHenkou) {
        // 処方変更が必要
        isConcerning = true;
    }

    // 良好な場合
    if (isGood && data.kaisuu !== "1") {
        block3 += "幸いなことに、神経心理検査の結果は前回と比較して良好に推移しております。";

        if (data.shohou === "処方依頼なし") {
            block3 += "現在の治療方針を継続させていただく所存でございます。";
        } else if (data.shohou === "継続") {
            block3 += "誠に恐縮ではございますが、現在ご処方いただいております治療の継続をお願い申し上げます。";
        }
    }
    // 懸念がある場合
    else if (isConcerning) {
        block3 += "誠に恐縮ではございますが、神経心理検査の結果では前回と比較して若干の変化が認められました。";

        if (data.shohou === "増量") {
            block3 += "大変僭越ながら、抗認知症薬の増量をご検討賜れますと誠に幸甚に存じます。";
        } else if (data.shohou === "切り替え") {
            let reason = "";
            if (data.kirikaeWhy === "消化器症状") reason = "消化器症状がみられるため";
            else if (data.kirikaeWhy === "焦燥") reason = "焦燥や不安感が懸念されるため";
            else if (data.kirikaeWhy === "徐脈") reason = "徐脈傾向がみられるため";
            else if (data.kirikaeWhy === "その他" && data.kirikaeSonota) reason = data.kirikaeSonota;

            block3 += `${reason}、抗認知症薬の切り替えをご検討賜れますと誠に幸甚に存じます。`;
        }
    }
    // 初回の場合
    else if (data.kaisuu === "1") {
        block3 += "以上の検査結果を踏まえ、上記診断に至りました。";

        if (data.shohou === "初回依頼" || data.shokaiKaisi) {
            block3 += "誠に恐縮ではございますが、抗認知症薬の導入につきまして、ご高配を賜りますようお願い申し上げます。";
        }
    }

    // 処方内容の記載
    const medications: string[] = [];
    if (data.alicept) medications.push(`アリセプト${data.alicept}mg`);
    if (data.donepezil) medications.push(`ドネペジル${data.donepezil}mg`);
    if (data.memary) medications.push(`メマリー${data.memary}mg`);
    if (data.memantine) medications.push(`メマンチン${data.memantine}mg`);

    if (medications.length > 0) {
        block3 += `\n（参考：当院での処方　${medications.join("、")}）`;
    }

    block3 += "\n\n";

    // 伝言
    if (data.dengon) {
        block3 += "■ その他ご連絡事項\n";
        block3 += data.dengon + "\n\n";
    }

    // ======================================
    // ブロック4: 締めの挨拶
    // ========================================
    let block4 = "【結び】\n";
    block4 += "ご多忙のところ誠に恐縮ではございますが、引き続きご高診を賜りますよう、謹んでお願い申し上げます。\n";
    block4 += "今後とも変わらぬご指導ご鞭撻のほど、何卒よろしくお願い申し上げます。\n";

    // ========================================
    // 全体を組み立て
    // ========================================
    return header + greeting + block1 + block2 + block3 + block4;
}
