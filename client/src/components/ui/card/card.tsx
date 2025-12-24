import * as React from 'react';
import { Slot } from '@radix-ui/react-slot';
import { cva, type VariantProps } from 'class-variance-authority';

import { cn } from '@/utils/cn';

const cardVariants = cva(
	'block text-white/90 text-xs font-secondary p-5 rounded-lg transition-colors',
	{
		variants: {
			theme: {
				lightGray: 'bg-foreground',
				darkGray: 'bg-dark-gray',
				gradient: 'bg-gradient-to-br from-primary via-foreground to-foreground',
			},
		},
		defaultVariants: {
			theme: 'lightGray',
		},
	},
);

export type CardProps = React.HTMLAttributes<HTMLDivElement> &
	VariantProps<typeof cardVariants> & {
		asChild?: boolean;
	};

const Card = React.forwardRef<HTMLDivElement, CardProps>(function (
	{ theme, children, className, asChild, ...props },
	ref,
) {
	const Comp = asChild ? Slot : 'div';

	return (
		<Comp
			ref={ref}
			className={cn(cardVariants({ theme }), className)}
			{...props}
		>
			{children}
		</Comp>
	);
});
Card.displayName = 'Card';

export { Card, cardVariants };
