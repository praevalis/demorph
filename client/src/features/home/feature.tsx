import { useTranslation } from 'react-i18next';

import type { FeatureCardData } from '@/types/ui';

import { cn } from '@/utils/cn';
import { Section } from '@/components/ui/section';
import StepCard from '@/components/cards/step-card';

export default function Feature() {
	const { t } = useTranslation();
	const cards = t('feature.cards', {
		returnObjects: true,
	}) as FeatureCardData[];
	const featureCards = Array.isArray(cards) ? cards : [];

	return (
		<Section id='features' className='bg-background'>
			<h3 className='text-3xl md:text-4xl text-white'>
				{t('feature.heading')}
			</h3>
			<div className='grid grid-cols-1 md:grid-cols-3 gap-4 mt-10'>
				{featureCards.map((card, idx) => (
					<StepCard
						key={idx}
						step={idx + 1}
						text={card.text}
						className={cn({ 'md:col-span-2': idx === 1 || idx === 2 })}
					/>
				))}
			</div>
		</Section>
	);
}
