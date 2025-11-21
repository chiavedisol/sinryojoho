import { z } from "zod";

export const formSchema = z.object({
  // Basic Info
  pageSelector: z.enum(["診療情報提供書", "診療情報提供書 木之下先生ver"]).default("診療情報提供書"),
  kensaDate: z.date().optional(),
  kensaBeforeDate: z.date().optional(),
  kaisuu: z.string().default("1"),
  atesaki: z.enum(["紹介状あり", "紹介状なし", "新しい通院先"]).default("紹介状あり"),
  kankei: z.enum(["関係性あり", "関係性なし", "施設/訪問医あて"]).optional(),

  // Scores
  hdsr: z.string().optional(),
  hdsrBefore: z.string().optional(),
  mmse: z.string().optional(),
  mmseBefore: z.string().optional(),
  adas: z.string().optional(),
  adasBefore: z.string().optional(),
  hantei: z.boolean().default(false), // ADAS natural course check
  cesd: z.string().optional(),
  sdidlb: z.string().optional(),

  // WMS-R / TMT
  gengo: z.string().optional(),
  sikaku: z.string().optional(),
  ippan: z.string().optional(),
  tyuui: z.string().optional(),
  tien: z.string().optional(),
  wmsrComment: z.string().optional(),
  // tmt removed

  // MRI
  mriPmi: z.boolean().default(false),
  mriFindings: z.string().optional(),
  mriKeijiHenka: z.boolean().default(false),
  mriArtifact: z.boolean().default(false),
  mriUgokuArtifact: z.boolean().default(false),
  mriShukketu: z.boolean().default(false),
  mriKousoku: z.boolean().default(false),
  mriKoumakuka: z.boolean().default(false),
  mriFollowDate: z.date().optional(),

  // MRA
  mraFindings: z.string().optional(),
  mraKeijiHenka: z.boolean().default(false),
  mraArtifact: z.boolean().default(false),
  mraUgokuArtifact: z.boolean().default(false),

  // Diagnosis
  conclusion: z.array(z.string()).default(["アルツハイマー型認知症"]),
  // Alzheimer
  ishuku: z.boolean().default(false), // 海馬萎縮
  // VaD
  kyoketu: z.boolean().default(false), // 基底核虚血
  vadMri: z.string().optional(),
  // DLB
  dlbHenDou: z.boolean().default(false), // 認知の変動 (renamed/new)
  dlbGensi: z.boolean().default(false), // 幻視
  dlbParkinson: z.boolean().default(false), // パーキンソン症状
  // NPH
  nphTriad: z.boolean().default(false), // 3徴 (renamed/new)
  // MCI/SCI
  wmsrRef: z.boolean().default(false), // WMS-R参照 (renamed/new)
  // PSP
  higaiIshuku: z.boolean().default(false), // 被蓋萎縮

  // Unused/Old fields kept just in case or removed if sure?
  // dlbRem, dlbJiritu, nphMerkmal, mciSci removed/replaced as per request to simplify

  // Medication
  shohouKaisi: z.boolean().default(false),
  zensoku: z.boolean().default(false),
  shokaiKaisi: z.boolean().default(false),
  zensokuTain: z.boolean().default(false),
  shohou: z.enum(["処方依頼なし", "将来", "初回依頼", "継続", "増量", "減量", "切り替え"]).default("処方依頼なし"),
  kirikaeWhy: z.enum(["消化器症状", "焦燥", "徐脈", "その他"]).optional(),
  kirikaeSonota: z.string().optional(),
  shohouHenkou: z.boolean().default(false),

  // Meds Amounts
  alicept: z.string().optional(),
  donepezil: z.string().optional(),
  memary: z.string().optional(),
  memantine: z.string().optional(),

  // Other Meds
  kouseisinNaifuku: z.array(z.string()).default([]),
  sonotaNaifuku: z.array(z.string()).default([]),

  // Explanation / Requests
  setumeiDate: z.date().optional(),
  setumeiIrai: z.boolean().default(false),
  naifukuKeizoku: z.boolean().default(false),
  senmouYakuzai: z.boolean().default(false),
  tyusiIrai: z.string().optional(),
  shoukakiYakuzai: z.boolean().default(false),
  itukara: z.string().optional(),
  tyusiOnegai: z.string().optional(),
  ketuatuTakai: z.boolean().default(false),
  ketuatu: z.string().optional(),

  // Message
  dengon: z.string().optional(),
});

export type FormData = z.infer<typeof formSchema>;
