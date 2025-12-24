import { cn } from '@/utils/cn';

export interface SectionProps {
	id: string;
	children: React.ReactNode;
	className?: string;
}

export function Section({ id, children, className }: SectionProps) {
	return (
		<section
			id={id}
			className={cn('w-full px-4 md:px-8 lg:px-[12vw] pt-20', className)}
		>
			{children}
		</section>
	);
}
