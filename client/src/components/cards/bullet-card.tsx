import { Card, type CardProps } from '@/components/ui/card';

import { cn } from '@/utils/cn';

export interface BulletCardProps extends CardProps {
	text: string;
}

export default function BulletCard({
	text,
	className,
	...props
}: BulletCardProps) {
	return (
		<Card theme='darkGray' className={cn(className)} {...props}>
			<div className='flex items-center gap-3'>
				<div className='shrink-0 h-3 w-3 rounded-full bg-primary'></div>
				<p className='leading-tight'>{text}</p>
			</div>
		</Card>
	);
}
