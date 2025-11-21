"use client";

import { useFormStore } from "@/lib/store";
import { Card, CardContent } from "@/components/ui/card";
import { generateText } from "@/lib/generateText";
import { Button } from "@/components/ui/button";
import { Copy } from "lucide-react";

export default function LivePreview() {
    const formData = useFormStore((state) => state.formData);
    const text = generateText(formData);

    const copyToClipboard = () => {
        navigator.clipboard.writeText(text);
        alert("コピーしました");
    };

    return (
        <Card className="h-full shadow-lg flex flex-col">
            <CardContent className="p-8 font-serif whitespace-pre-wrap leading-relaxed flex-grow overflow-y-auto text-lg">
                {text || <span className="text-gray-400 italic">フォームに入力するとここにプレビューが表示されます...</span>}
            </CardContent>
            <div className="p-4 border-t bg-gray-50 flex justify-end">
                <Button onClick={copyToClipboard} variant="outline" className="gap-2">
                    <Copy size={16} />
                    テキストをコピー
                </Button>
            </div>
        </Card>
    );
}
