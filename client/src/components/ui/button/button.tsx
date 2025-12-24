import * as React from 'react';
import { Slot } from '@radix-ui/react-slot';
import { cva, type VariantProps } from 'class-variance-authority';

import { cn } from '@/utils/cn';

const buttonVariants = cva(
	'inline-flex w-fit items-center justify-center whitespace-nowrap text-sm font-medium font-montserrat transition-colors cursor-pointer focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 gap-2',
	{
		variants: {
			intent: {
				primary: 'bg-primary text-white hover:bg-primary/90',
				gray: 'bg-dark-gray text-white',
				white: 'bg-white text-accent hover:bg-white/90',
			},
			size: {
				small: 'h-8 px-3 text-xs',
				medium: 'h-9 px-4 py-2',
				large: 'h-10 px-8',
				icon: 'size-9',
			},
			shape: {
				default: 'rounded-md',
				square: 'rounded-none',
				pill: 'rounded-full',
				social: 'rounded-4xl',
			},
		},
		defaultVariants: {
			intent: 'primary',
			size: 'medium',
			shape: 'default',
		},
	},
);

export type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> &
	VariantProps<typeof buttonVariants> & {
		asChild?: boolean;
		isLoading?: boolean;
		icon?: React.ReactNode;
	};

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(function Button(
	{
		icon,
		size,
		intent,
		children,
		isLoading,
		className,
		asChild = false,
		...props
	},
	ref,
) {
	const Comp = asChild ? Slot : 'button';
	return (
		<Comp
			className={cn(buttonVariants({ intent, size }), className)}
			ref={ref}
			{...props}
		>
			{asChild ? (
				children
			) : (
				<>
					{!isLoading && icon}
					{children}
				</>
			)}
		</Comp>
	);
});
Button.displayName = 'Button';

export { Button, buttonVariants };
