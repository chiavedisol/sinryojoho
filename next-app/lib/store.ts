import { create } from 'zustand';
import { FormData } from './types';

interface FormState {
    formData: Partial<FormData>;
    setFormData: (data: FormData) => void;
}

export const useFormStore = create<FormState>((set) => ({
    formData: {},
    setFormData: (data) => set({ formData: data }),
}));
