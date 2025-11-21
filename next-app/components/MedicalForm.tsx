"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { formSchema, FormData } from "@/lib/types";
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Checkbox } from "@/components/ui/checkbox";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useFormStore } from "@/lib/store";
import { useEffect } from "react";
import { generateText } from "@/lib/generateText";
import { generatePDF } from "@/lib/generatePDF";
import { DateInput } from "@/components/DateInput";

export default function MedicalForm() {
    const setFormData = useFormStore((state) => state.setFormData);

    const form = useForm({
        resolver: zodResolver(formSchema),
        defaultValues: {
            pageSelector: "診療情報提供書",
            kaisuu: "1",
            atesaki: "紹介状あり",
            kankei: "関係性あり",
            hantei: false,
            // tmt removed
            mriPmi: false,
            mriKeijiHenka: false,
            mriArtifact: false,
            mriUgokuArtifact: false,
            mriShukketu: false,
            mriKousoku: false,
            mriKoumakuka: false,
            mraKeijiHenka: false,
            mraArtifact: false,
            mraUgokuArtifact: false,
            conclusion: ["アルツハイマー型認知症"],
            ishuku: false,
            higaiIshuku: false,
            kyoketu: false,
            dlbHenDou: false,
            dlbGensi: false,
            dlbParkinson: false,
            nphTriad: false,
            wmsrRef: false,
            shohouKaisi: false,
            zensoku: false,
            shokaiKaisi: false,
            zensokuTain: false,
            shohou: "処方依頼なし",
            shohouHenkou: false,
            kouseisinNaifuku: [],
            sonotaNaifuku: [],
            setumeiIrai: false,
            naifukuKeizoku: false,
            senmouYakuzai: false,
            shoukakiYakuzai: false,
            hdsr: "",
            hdsrBefore: "",
            mmse: "",
            mmseBefore: "",
            adas: "",
            adasBefore: "",
            cesd: "",
            sdidlb: "",
            gengo: "",
            sikaku: "",
            ippan: "",
            tyuui: "",
            tien: "",
            wmsrComment: "",
            mriFindings: "",
            mraFindings: "",
            vadMri: "",
            kirikaeSonota: "",
            alicept: "",
            donepezil: "",
            memary: "",
            memantine: "",
            tyusiIrai: "",
            itukara: "",
            tyusiOnegai: "",
            ketuatu: "",
            dengon: "",
            ketuatuTakai: false,
        },
    });

    const watchedData = form.watch();

    useEffect(() => {
        setFormData(watchedData as FormData);
    }, [watchedData, setFormData]);

    async function onSubmit(data: FormData) {
        console.log(data);
        const text = generateText(data);
        await generatePDF(text);
    }

    const conclusion = form.watch("conclusion") || [];
    const mriArtifact = form.watch("mriArtifact");
    const mraArtifact = form.watch("mraArtifact");

    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8 pb-20">

                {/* 基本情報 */}
                <Card className="shadow-md">
                    <CardHeader className="bg-slate-50 dark:bg-slate-900 border-b">
                        <CardTitle className="text-lg font-bold text-slate-800 dark:text-slate-100">基本情報</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-6 pt-6">
                        <FormField
                            control={form.control}
                            name="pageSelector"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>書式選択</FormLabel>
                                    <Select onValueChange={field.onChange} defaultValue={field.value}>
                                        <FormControl>
                                            <SelectTrigger>
                                                <SelectValue placeholder="選択してください" />
                                            </SelectTrigger>
                                        </FormControl>
                                        <SelectContent>
                                            <SelectItem value="診療情報提供書">診療情報提供書</SelectItem>
                                            <SelectItem value="診療情報提供書 木之下先生ver">診療情報提供書 木之下先生ver</SelectItem>
                                        </SelectContent>
                                    </Select>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <FormField
                                control={form.control}
                                name="kensaDate"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>今回の検査日程</FormLabel>
                                        <FormControl>
                                            <DateInput value={field.value} onChange={field.onChange} />
                                        </FormControl>
                                        <FormMessage />
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="kensaBeforeDate"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>前回の検査日程</FormLabel>
                                        <FormControl>
                                            <DateInput value={field.value} onChange={field.onChange} />
                                        </FormControl>
                                        <FormMessage />
                                    </FormItem>
                                )}
                            />
                        </div>

                        <FormField
                            control={form.control}
                            name="kaisuu"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>当院での検査回数</FormLabel>
                                    <FormControl>
                                        <Input type="number" {...field} className="w-24" />
                                    </FormControl>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />

                        <FormField
                            control={form.control}
                            name="atesaki"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>宛先</FormLabel>
                                    <RadioGroup onValueChange={field.onChange} defaultValue={field.value} className="flex flex-col space-y-2">
                                        <FormItem className="flex items-center space-x-3 space-y-0">
                                            <FormControl>
                                                <RadioGroupItem value="紹介状あり" />
                                            </FormControl>
                                            <FormLabel className="font-normal cursor-pointer">紹介状あり</FormLabel>
                                        </FormItem>
                                        <FormItem className="flex items-center space-x-3 space-y-0">
                                            <FormControl>
                                                <RadioGroupItem value="紹介状なし" />
                                            </FormControl>
                                            <FormLabel className="font-normal cursor-pointer">紹介状なし</FormLabel>
                                        </FormItem>
                                        <FormItem className="flex items-center space-x-3 space-y-0">
                                            <FormControl>
                                                <RadioGroupItem value="新しい通院先" />
                                            </FormControl>
                                            <FormLabel className="font-normal cursor-pointer">新しい通院先</FormLabel>
                                        </FormItem>
                                    </RadioGroup>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />

                        {form.watch("atesaki") === "紹介状なし" && (
                            <FormField
                                control={form.control}
                                name="kankei"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>かかりつけ医との関係</FormLabel>
                                        <RadioGroup onValueChange={field.onChange} defaultValue={field.value} className="flex flex-col space-y-1">
                                            <FormItem className="flex items-center space-x-3 space-y-0">
                                                <FormControl>
                                                    <RadioGroupItem value="関係性あり" />
                                                </FormControl>
                                                <FormLabel className="font-normal">関係性あり</FormLabel>
                                            </FormItem>
                                            <FormItem className="flex items-center space-x-3 space-y-0">
                                                <FormControl>
                                                    <RadioGroupItem value="関係性なし" />
                                                </FormControl>
                                                <FormLabel className="font-normal">関係性なし</FormLabel>
                                            </FormItem>
                                            <FormItem className="flex items-center space-x-3 space-y-0">
                                                <FormControl>
                                                    <RadioGroupItem value="施設/訪問医あて" />
                                                </FormControl>
                                                <FormLabel className="font-normal">施設/訪問医あて</FormLabel>
                                            </FormItem>
                                        </RadioGroup>
                                        <FormMessage />
                                    </FormItem>
                                )}
                            />
                        )}
                    </CardContent>
                </Card>

                {/* 神経心理検査 */}
                <Card className="shadow-md">
                    <CardHeader className="bg-slate-50 dark:bg-slate-900 border-b">
                        <CardTitle className="text-lg font-bold text-slate-800 dark:text-slate-100">神経心理検査</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-6 pt-6">
                        <div className="grid grid-cols-2 gap-6">
                            <FormField
                                control={form.control}
                                name="hdsr"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>HDS-R (今回)</FormLabel>
                                        <FormControl>
                                            <Input type="number" {...field} />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="hdsrBefore"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>HDS-R (前回)</FormLabel>
                                        <FormControl>
                                            <Input type="number" {...field} />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="mmse"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>MMSE (今回)</FormLabel>
                                        <FormControl>
                                            <Input type="number" {...field} />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="mmseBefore"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>MMSE (前回)</FormLabel>
                                        <FormControl>
                                            <Input type="number" {...field} />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="adas"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>ADAS (今回)</FormLabel>
                                        <FormControl>
                                            <Input type="number" {...field} />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="adasBefore"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>ADAS (前回)</FormLabel>
                                        <FormControl>
                                            <Input type="number" {...field} />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                        </div>

                        <FormField
                            control={form.control}
                            name="hantei"
                            render={({ field }) => (
                                <FormItem className="flex flex-row items-start space-x-3 space-y-0 rounded-md border p-4 bg-slate-50 dark:bg-slate-900">
                                    <FormControl>
                                        <Checkbox
                                            checked={field.value}
                                            onCheckedChange={field.onChange}
                                        />
                                    </FormControl>
                                    <div className="space-y-1 leading-none">
                                        <FormLabel className="cursor-pointer">
                                            ADAS曲線のnatural courseを上回りますか？
                                        </FormLabel>
                                    </div>
                                </FormItem>
                            )}
                        />

                        <div className="grid grid-cols-2 gap-6">
                            <FormField
                                control={form.control}
                                name="cesd"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>CES-D</FormLabel>
                                        <FormControl>
                                            <Input type="number" {...field} />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                            <FormField
                                control={form.control}
                                name="sdidlb"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>SDI-DLB</FormLabel>
                                        <FormControl>
                                            <Input type="number" {...field} />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                        </div>

                        <div className="space-y-4 border-t pt-4">
                            <h3 className="font-semibold text-slate-700 dark:text-slate-300">WMS-R / TMT</h3>
                            <div className="grid grid-cols-2 gap-4">
                                <FormField control={form.control} name="gengo" render={({ field }) => (<FormItem><FormLabel>言語性記憶</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                                <FormField control={form.control} name="sikaku" render={({ field }) => (<FormItem><FormLabel>視覚性記憶</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                                <FormField control={form.control} name="ippan" render={({ field }) => (<FormItem><FormLabel>一般的記憶</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                                <FormField control={form.control} name="tyuui" render={({ field }) => (<FormItem><FormLabel>注意/集中力</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                                <FormField control={form.control} name="tien" render={({ field }) => (<FormItem><FormLabel>遅延再生</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                            </div>
                            <FormField
                                control={form.control}
                                name="wmsrComment"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>WMS-R コメント</FormLabel>
                                        <FormControl>
                                            <Textarea {...field} />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                        </div>
                    </CardContent>
                </Card>

                {/* 画像検査 */}
                <Card className="shadow-md">
                    <CardHeader className="bg-slate-50 dark:bg-slate-900 border-b">
                        <CardTitle className="text-lg font-bold text-slate-800 dark:text-slate-100">画像検査 (MRI/MRA)</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-6 pt-6">
                        <FormField
                            control={form.control}
                            name="mriPmi"
                            render={({ field }) => (
                                <FormItem className="flex flex-row items-start space-x-3 space-y-0">
                                    <FormControl>
                                        <Checkbox checked={field.value} onCheckedChange={field.onChange} />
                                    </FormControl>
                                    <FormLabel className="cursor-pointer">PMIのためMRI未実施</FormLabel>
                                </FormItem>
                            )}
                        />

                        <FormField
                            control={form.control}
                            name="mriFindings"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>MRI所見</FormLabel>
                                    <FormControl>
                                        <Textarea {...field} placeholder="所見を入力..." />
                                    </FormControl>
                                </FormItem>
                            )}
                        />

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <FormField control={form.control} name="mriKeijiHenka" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">経時的変化なし</FormLabel></FormItem>)} />
                            <FormField control={form.control} name="mriArtifact" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">アーチファクトあり</FormLabel></FormItem>)} />
                            <FormField control={form.control} name="mriUgokuArtifact" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} disabled={!mriArtifact} /></FormControl><FormLabel className={!mriArtifact ? "text-muted-foreground" : "cursor-pointer"}>体動によるアーチファクト</FormLabel></FormItem>)} />
                            <FormField control={form.control} name="mriShukketu" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">微小脳出血</FormLabel></FormItem>)} />
                            <FormField control={form.control} name="mriKousoku" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">脳梗塞</FormLabel></FormItem>)} />
                            <FormField control={form.control} name="mriKoumakuka" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">硬膜下血腫</FormLabel></FormItem>)} />
                        </div>

                        <FormField
                            control={form.control}
                            name="mriFollowDate"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>MRI再検日</FormLabel>
                                    <FormControl>
                                        <DateInput value={field.value} onChange={field.onChange} />
                                    </FormControl>
                                </FormItem>
                            )}
                        />

                        <div className="border-t pt-4 mt-4">
                            <FormField
                                control={form.control}
                                name="mraFindings"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>MRA所見</FormLabel>
                                        <FormControl>
                                            <Textarea {...field} placeholder="所見を入力..." />
                                        </FormControl>
                                    </FormItem>
                                )}
                            />
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                                <FormField control={form.control} name="mraKeijiHenka" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">経時的変化なし</FormLabel></FormItem>)} />
                                <FormField control={form.control} name="mraArtifact" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">アーチファクトあり</FormLabel></FormItem>)} />
                                <FormField control={form.control} name="mraUgokuArtifact" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} disabled={!mraArtifact} /></FormControl><FormLabel className={!mraArtifact ? "text-muted-foreground" : "cursor-pointer"}>体動によるアーチファクト</FormLabel></FormItem>)} />
                            </div>
                        </div>
                    </CardContent>
                </Card>

                {/* 診断 */}
                <Card className="shadow-md">
                    <CardHeader className="bg-slate-50 dark:bg-slate-900 border-b">
                        <CardTitle className="text-lg font-bold text-slate-800 dark:text-slate-100">診断</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-6 pt-6">
                        <FormField
                            control={form.control}
                            name="conclusion"
                            render={() => (
                                <FormItem>
                                    <div className="mb-4">
                                        <FormLabel className="text-base">診断名 (複数選択可)</FormLabel>
                                    </div>
                                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                        {["アルツハイマー型認知症", "血管性認知症", "レビー小体型認知症", "正常圧水頭症", "MCI/SCI", "進行性核上性麻痺"].map((item) => (
                                            <FormField
                                                key={item}
                                                control={form.control}
                                                name="conclusion"
                                                render={({ field }) => {
                                                    return (
                                                        <FormItem
                                                            key={item}
                                                            className="flex flex-row items-start space-x-3 space-y-0"
                                                        >
                                                            <FormControl>
                                                                <Checkbox
                                                                    checked={field.value?.includes(item)}
                                                                    onCheckedChange={(checked) => {
                                                                        return checked
                                                                            ? field.onChange([...(field.value || []), item])
                                                                            : field.onChange(
                                                                                field.value?.filter(
                                                                                    (value) => value !== item
                                                                                )
                                                                            )
                                                                    }}
                                                                />
                                                            </FormControl>
                                                            <FormLabel className="font-normal cursor-pointer">
                                                                {item}
                                                            </FormLabel>
                                                        </FormItem>
                                                    )
                                                }}
                                            />
                                        ))}
                                    </div>
                                </FormItem>
                            )}
                        />

                        {/* 診断に至った所見 */}
                        <div className="border p-6 rounded-md space-y-4 bg-slate-50 dark:bg-slate-900">
                            <p className="text-sm font-bold text-slate-700 dark:text-slate-300">診断に至った所見</p>
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                {conclusion.includes("アルツハイマー型認知症") && (
                                    <FormField control={form.control} name="ishuku" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">海馬萎縮あり</FormLabel></FormItem>)} />
                                )}
                                {conclusion.includes("血管性認知症") && (
                                    <>
                                        <FormField control={form.control} name="kyoketu" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">基底核虚血あり</FormLabel></FormItem>)} />
                                        <FormField control={form.control} name="vadMri" render={({ field }) => (<FormItem><FormLabel>VaD MRI所見</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                                    </>
                                )}
                                {conclusion.includes("レビー小体型認知症") && (
                                    <>
                                        <FormField control={form.control} name="dlbHenDou" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">認知の変動</FormLabel></FormItem>)} />
                                        <FormField control={form.control} name="dlbGensi" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">幻視</FormLabel></FormItem>)} />
                                        <FormField control={form.control} name="dlbParkinson" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">パーキンソン症状</FormLabel></FormItem>)} />
                                    </>
                                )}
                                {conclusion.includes("正常圧水頭症") && (
                                    <FormField control={form.control} name="nphTriad" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">正常圧水頭症の3徴</FormLabel></FormItem>)} />
                                )}
                                {conclusion.includes("MCI/SCI") && (
                                    <FormField control={form.control} name="wmsrRef" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">WMS-R参照</FormLabel></FormItem>)} />
                                )}
                                {conclusion.includes("進行性核上性麻痺") && (
                                    <FormField control={form.control} name="higaiIshuku" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">被蓋萎縮あり</FormLabel></FormItem>)} />
                                )}
                            </div>
                        </div>
                    </CardContent>
                </Card>

                {/* 処方・治療 */}
                <Card className="shadow-md">
                    <CardHeader className="bg-slate-50 dark:bg-slate-900 border-b">
                        <CardTitle className="text-lg font-bold text-slate-800 dark:text-slate-100">処方・治療</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-6 pt-6">
                        <FormField
                            control={form.control}
                            name="shohou"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>処方依頼について</FormLabel>
                                    <Select onValueChange={field.onChange} defaultValue={field.value}>
                                        <FormControl>
                                            <SelectTrigger>
                                                <SelectValue placeholder="選択してください" />
                                            </SelectTrigger>
                                        </FormControl>
                                        <SelectContent>
                                            <SelectItem value="処方依頼なし">処方依頼なし</SelectItem>
                                            <SelectItem value="将来">将来</SelectItem>
                                            <SelectItem value="初回依頼">初回依頼</SelectItem>
                                            <SelectItem value="継続">継続</SelectItem>
                                            <SelectItem value="増量">増量</SelectItem>
                                            <SelectItem value="減量">減量</SelectItem>
                                            <SelectItem value="切り替え">切り替え</SelectItem>
                                        </SelectContent>
                                    </Select>
                                    <FormMessage />
                                </FormItem>
                            )}
                        />

                        {form.watch("shohou") === "切り替え" && (
                            <FormField
                                control={form.control}
                                name="kirikaeWhy"
                                render={({ field }) => (
                                    <FormItem>
                                        <FormLabel>切り替え理由</FormLabel>
                                        <Select onValueChange={field.onChange} defaultValue={field.value}>
                                            <FormControl>
                                                <SelectTrigger>
                                                    <SelectValue placeholder="選択してください" />
                                                </SelectTrigger>
                                            </FormControl>
                                            <SelectContent>
                                                <SelectItem value="消化器症状">消化器症状</SelectItem>
                                                <SelectItem value="焦燥">焦燥</SelectItem>
                                                <SelectItem value="徐脈">徐脈</SelectItem>
                                                <SelectItem value="その他">その他</SelectItem>
                                            </SelectContent>
                                        </Select>
                                        <FormMessage />
                                    </FormItem>
                                )}
                            />
                        )}

                        <div className="grid grid-cols-2 gap-4">
                            <FormField control={form.control} name="alicept" render={({ field }) => (<FormItem><FormLabel>アリセプト (mg)</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                            <FormField control={form.control} name="donepezil" render={({ field }) => (<FormItem><FormLabel>ドネペジル (mg)</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                            <FormField control={form.control} name="memary" render={({ field }) => (<FormItem><FormLabel>メマリー (mg)</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                            <FormField control={form.control} name="memantine" render={({ field }) => (<FormItem><FormLabel>メマンチン (mg)</FormLabel><FormControl><Input {...field} /></FormControl></FormItem>)} />
                        </div>

                        <FormField
                            control={form.control}
                            name="kouseisinNaifuku"
                            render={() => (
                                <FormItem>
                                    <div className="mb-4">
                                        <FormLabel className="text-base">抗精神病薬</FormLabel>
                                    </div>
                                    <div className="grid grid-cols-2 gap-4">
                                        {["クエチアピン", "抑肝散", "リスペリドン", "チアプリド"].map((item) => (
                                            <FormField
                                                key={item}
                                                control={form.control}
                                                name="kouseisinNaifuku"
                                                render={({ field }) => {
                                                    return (
                                                        <FormItem
                                                            key={item}
                                                            className="flex flex-row items-start space-x-3 space-y-0"
                                                        >
                                                            <FormControl>
                                                                <Checkbox
                                                                    checked={field.value?.includes(item)}
                                                                    onCheckedChange={(checked) => {
                                                                        return checked
                                                                            ? field.onChange([...(field.value || []), item])
                                                                            : field.onChange(
                                                                                field.value?.filter(
                                                                                    (value) => value !== item
                                                                                )
                                                                            )
                                                                    }}
                                                                />
                                                            </FormControl>
                                                            <FormLabel className="font-normal cursor-pointer">
                                                                {item}
                                                            </FormLabel>
                                                        </FormItem>
                                                    )
                                                }}
                                            />
                                        ))}
                                    </div>
                                </FormItem>
                            )}
                        />
                        <FormField
                            control={form.control}
                            name="sonotaNaifuku"
                            render={() => (
                                <FormItem>
                                    <div className="mb-4">
                                        <FormLabel className="text-base">その他内服</FormLabel>
                                    </div>
                                    <div className="grid grid-cols-2 gap-4">
                                        {["アリナミン", "メチコバール", "フォリアミン", "シロスタゾール", "バイアスピリン", "プラビックス"].map((item) => (
                                            <FormField
                                                key={item}
                                                control={form.control}
                                                name="sonotaNaifuku"
                                                render={({ field }) => {
                                                    return (
                                                        <FormItem
                                                            key={item}
                                                            className="flex flex-row items-start space-x-3 space-y-0"
                                                        >
                                                            <FormControl>
                                                                <Checkbox
                                                                    checked={field.value?.includes(item)}
                                                                    onCheckedChange={(checked) => {
                                                                        return checked
                                                                            ? field.onChange([...(field.value || []), item])
                                                                            : field.onChange(
                                                                                field.value?.filter(
                                                                                    (value) => value !== item
                                                                                )
                                                                            )
                                                                    }}
                                                                />
                                                            </FormControl>
                                                            <FormLabel className="font-normal cursor-pointer">
                                                                {item}
                                                            </FormLabel>
                                                        </FormItem>
                                                    )
                                                }}
                                            />
                                        ))}
                                    </div>
                                </FormItem>
                            )}
                        />
                    </CardContent>
                </Card>

                {/* 説明・連絡 */}
                <Card className="shadow-md">
                    <CardHeader className="bg-slate-50 dark:bg-slate-900 border-b">
                        <CardTitle className="text-lg font-bold text-slate-800 dark:text-slate-100">説明・連絡</CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-6 pt-6">
                        <FormField
                            control={form.control}
                            name="setumeiDate"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>結果説明日</FormLabel>
                                    <FormControl>
                                        <DateInput value={field.value} onChange={field.onChange} />
                                    </FormControl>
                                </FormItem>
                            )}
                        />
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <FormField control={form.control} name="setumeiIrai" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">他院への説明依頼</FormLabel></FormItem>)} />
                            <FormField control={form.control} name="naifukuKeizoku" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">内服継続の相談</FormLabel></FormItem>)} />
                            <FormField control={form.control} name="senmouYakuzai" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">せん妄薬剤調整</FormLabel></FormItem>)} />
                            <FormField control={form.control} name="shoukakiYakuzai" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">消化器症状による中止</FormLabel></FormItem>)} />
                            <FormField control={form.control} name="ketuatuTakai" render={({ field }) => (<FormItem className="flex flex-row items-center space-x-2 space-y-0"><FormControl><Checkbox checked={field.value} onCheckedChange={field.onChange} /></FormControl><FormLabel className="cursor-pointer">血圧高値</FormLabel></FormItem>)} />
                        </div>

                        <FormField
                            control={form.control}
                            name="dengon"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>伝言</FormLabel>
                                    <FormControl>
                                        <Textarea {...field} placeholder="伝言を入力..." />
                                    </FormControl>
                                </FormItem>
                            )}
                        />
                    </CardContent>
                </Card>

                <Button type="submit" className="w-full py-6 text-lg font-bold shadow-lg">保存 / PDF生成</Button>
            </form>
        </Form>
    );
}
