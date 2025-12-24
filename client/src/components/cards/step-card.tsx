import { Card, CardProps } from '@/components/ui/card';

import { cn } from '@/utils/cn';

export interface StepCardProps extends CardProps {
	step: number;
	text: string;
}

export default function StepCard({
	step,
	text,
	className,
	theme = 'gradient',
	...props
}: StepCardProps) {
	return (
		<Card theme={theme} className={cn(className)} {...props}>
			<div className='flex flex-col gap-6'>
				<div className='w-10 h-10 flex items-center justify-center shrink-0 rounded-full bg-white text-primary'>
					{step}
				</div>
				<p className='text-sm leading-tight'>{text}</p>
			</div>
		</Card>
	);
}
