<script lang="ts">
    import type { FullAutoFill } from "svelte/elements";

    const defaultClass = 'max-w-54 border border-gray-300 rounded-md p-2 w-full outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent';

    const {
        class: className = '',
        id = '',
        type = 'text' as const,
        name = '',
        value = undefined,
        required = false,
        placeholder = '',
        disabled = false,
        readonly = false,
        autocomplete = undefined,
        min = undefined,
        max = undefined,
        title = '',
        autocapitalize = 'off' as const,
        onInput = undefined,
        onChange = undefined,
        onFocus = undefined,
        onKeyDown = undefined,
        onKeyUp = undefined,
        onClick = undefined,
    }: {
        class?: string;
        id?: string;
        type?: 'text' | 'password' | 'email' | 'number' | 'date' | 'time' | 'url' | 'tel' | 'search' | 'color' | 'file' | 'range' | 'checkbox' | 'radio' | 'submit' | 'reset' | 'button' | 'hidden';
        name?: string;
        value?: string | number;
        required?: boolean;
        placeholder?: string;
        disabled?: boolean;
        readonly?: boolean;
        autocomplete?: FullAutoFill;
        min?: number;
        max?: number;
        title?: string;
        autocapitalize?: "off" | "on" | "characters" | "none" | "sentences" | "words" | null;
        onInput?: (event: Event) => void;
        onChange?: (event: Event) => void;
        onFocus?: (event: Event) => void;
        onKeyDown?: (event: Event) => void;
        onKeyUp?: (event: Event) => void;
        onClick?: (event: Event) => void;
    } = $props();

    let combinedClasses = $derived(`${defaultClass} ${className}`.trim());
</script>

<input 
    class={combinedClasses}
    id={id}
    type={type}
    name={name}
    value={value}
    placeholder={placeholder}
    disabled={disabled}
    readonly={readonly}
    required={required}
    autocomplete={autocomplete}
    min={min}
    max={max}
    title={title}
    autocapitalize={autocapitalize}
    oninput={onInput}
    onchange={onChange}
    onfocus={onFocus}
    onkeydown={onKeyDown}
    onkeyup={onKeyUp}
    onclick={onClick}
/>