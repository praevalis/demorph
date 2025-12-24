import { ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

/**
 * Helper function to merge conditional tailwind classes.
 * @param input - Array of class strings or conditional classes.
 * @returns string - Merged class string.
 */
export function cn(...input: ClassValue[]): string {
	return twMerge(clsx(input));
}
