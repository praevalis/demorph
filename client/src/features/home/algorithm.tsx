import { useTranslation } from 'react-i18next';

import type { FeatureCardData } from '@/types/ui';

import { Section } from '@/components/ui/section';
import BulletCard from '@/components/cards/bullet-card';

export default function Algorithm() {
	const { t } = useTranslation();
	const cards = t('algorithm.cards', {
		returnObjects: true,
	}) as FeatureCardData;
	const bulletCards = Array.isArray(cards) ? cards : [];

	return (
		<Section id='algorithm' className='flex bg-background'>
			<div className='flex flex-col w-full gap-14'>
				<h3 className='max-w-md mx-auto md:mx-0 text-2xl text-white text-center md:text-left font-secondary font-semibold'>
					{t('algorithm.heading')}
				</h3>
				<div className='flex flex-col md:flex-row gap-10 w-full justify-between'>
					{/* Neon Tube */}
					<div className='relative w-64 h-64 md:w-80 md:h-80 mx-auto md:mx-0 rounded-full'>
						{/* Outer Glow */}
						<div className='absolute -inset-1 rounded-full bg-gradient-to-r from-secondary to-accent blur-xl opacity-30'></div>

						<div className='flex h-full w-full items-center justify-center rounded-full bg-gradient-to-r from-secondary to-accent p-4'>
							<div className='relative flex items-center justify-center h-full w-full rounded-full bg-background text-center overflow-hidden'>
								{/* Inner Glow */}
								<div className='absolute -inset-1 rounded-full bg-gradient-to-r from-secondary to-accent blur-lg opacity-30 [mask-image:radial-gradient(transparent_55%,black)]'></div>

								<div className='relative z-10'>
									<h2 className='text-xl md:text-2xl font-semibold font-secondary text-white whitespace-pre-line'>
										{t('algorithm.ring')}
									</h2>
								</div>
							</div>
						</div>
					</div>

					{/* Bullet Cards */}
					<div className='grid grid-cols-1 gap-2'>
						{bulletCards.map((card, idx) => (
							<BulletCard
								key={idx}
								text={card.text}
								className='h-fit'
							></BulletCard>
						))}
					</div>
				</div>
			</div>
		</Section>
	);
}
