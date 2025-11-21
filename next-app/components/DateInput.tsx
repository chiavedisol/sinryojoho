"use client";

import * as React from "react";
import { format, parse } from "date-fns";
import { Calendar as CalendarIcon } from "lucide-react";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover";
import { Input } from "@/components/ui/input";

interface DateInputProps {
    value?: Date;
    onChange: (date?: Date) => void;
    label?: string;
}

export function DateInput({ value, onChange, label }: DateInputProps) {
    const [inputValue, setInputValue] = React.useState("");

    // Sync input value when prop value changes
    React.useEffect(() => {
        if (value) {
            setInputValue(format(value, "yyyyMMdd"));
        } else {
            setInputValue("");
        }
    }, [value]);

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const val = e.target.value;
        setInputValue(val);

        // Try to parse 8 digit number
        if (val.length === 8 && /^\d{8}$/.test(val)) {
            const date = parse(val, "yyyyMMdd", new Date());
            if (!isNaN(date.getTime())) {
                onChange(date);
            }
        } else if (val === "") {
            onChange(undefined);
        }
    };

    const handleCalendarSelect = (date?: Date) => {
        onChange(date);
        // Input value will update via useEffect
    };

    return (
        <div className="flex items-center gap-2">
            <Input
                type="text"
                placeholder="YYYYMMDD"
                value={inputValue}
                onChange={handleInputChange}
                className="w-[140px]"
                maxLength={8}
            />
            <Popover>
                <PopoverTrigger asChild>
                    <Button
                        variant={"outline"}
                        className={cn(
                            "w-[40px] px-0 text-left font-normal",
                            !value && "text-muted-foreground"
                        )}
                    >
                        <CalendarIcon className="h-4 w-4" />
                    </Button>
                </PopoverTrigger>
                <PopoverContent className="w-auto p-0" align="start">
                    <Calendar
                        mode="single"
                        selected={value}
                        onSelect={handleCalendarSelect}
                        initialFocus
                    />
                </PopoverContent>
            </Popover>
        </div>
    );
}
